"""
Team 2 — Creative involvement & psychological ownership
실험 웹앱(index.html)에서 내보낸 CSV를 분석한다.

사용:  python3 analysis/analyze.py ownership_study_XXXX.csv [--include-test] [--out results.md]

분석 계획 (PDF p.11 / Appendix)
  - 신뢰도: PO, IA, CC Cronbach's α / AU 2문항 Spearman-Brown
  - Check  : CC  B > A  (Welch t, one-sided) + Hedges g + exact permutation
  - H1     : PO  B > A  (Welch t, one-sided / two-sided) + Hedges g + exact permutation + Mann-Whitney
  - 2차    : AU  (Welch t), declared credit (Fisher exact 2x2: 'self' vs 기타, + 전체 표 exact permutation)
  - RQ2    : OLS  PO ~ IA + condition  (+ 상호작용 탐색)
  - 공변량 : OLS  PO ~ condition + quality + effort  (N=12에서는 해석 주의)
  - 통제점검: 프롬프트 길이·작성 시간·수정량이 조건 간 비슷한지 (교수님 피드백: 시간/길이 교란)
            + OLS  PO ~ condition + final prompt length
  - 세계관 : 조건 × 세계관 배정 균형, 세계관별 PO, OLS  PO ~ condition + world
  - 과정   : 생성 횟수, 단계별 길이·입력량·시간 기술통계
의존성: numpy, scipy (pandas/statsmodels 불필요)
"""
import argparse
import csv
import itertools
import math
import sys
from collections import Counter

import numpy as np
from scipy import stats

SCALES = {
    "PO": ["PO1", "PO2", "PO3", "PO4", "PO5"],
    "IA": ["IA1", "IA2", "IA3"],
    "AU": ["AU1", "AU2"],
    "CC": ["CC1", "CC2", "CC3"],
}
CREDIT_LABELS = {"self": "Myself", "joint": "Myself+AI", "ai_main": "Mainly AI", "other": "Other"}


# ---------------------------------------------------------------- loading
def to_num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return np.nan


def load(path, include_test):
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    keep = [r for r in rows if r.get("completed") == "1" and (include_test or r.get("is_test") != "1")]
    dropped = len(rows) - len(keep)
    # 같은 pid가 여러 번 완료된 경우 마지막 세션만 사용
    by_pid = {}
    for r in sorted(keep, key=lambda r: r.get("completed_at", "")):
        by_pid[r["pid"]] = r
    return list(by_pid.values()), dropped, len(keep) - len(by_pid)


def col(rows, name):
    return np.array([to_num(r.get(name)) for r in rows], dtype=float)


# ---------------------------------------------------------------- stats helpers
def cronbach_alpha(items):
    x = np.column_stack(items)
    x = x[~np.isnan(x).any(axis=1)]
    k = x.shape[1]
    if x.shape[0] < 3:
        return np.nan
    item_var = x.var(axis=0, ddof=1).sum()
    total_var = x.sum(axis=1).var(ddof=1)
    return k / (k - 1) * (1 - item_var / total_var) if total_var > 0 else np.nan


def spearman_brown(a, b):
    r = np.corrcoef(a, b)[0, 1]
    return r, 2 * r / (1 + r) if r > -1 else np.nan


def hedges_g(a, b):
    """g for (b - a); 95% CI via normal approx of the sampling variance."""
    na, nb = len(a), len(b)
    sp = math.sqrt(((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1)) / (na + nb - 2))
    if sp == 0:
        return np.nan, (np.nan, np.nan)
    d = (b.mean() - a.mean()) / sp
    j = 1 - 3 / (4 * (na + nb) - 9)
    g = d * j
    se = math.sqrt((na + nb) / (na * nb) + g ** 2 / (2 * (na + nb)))
    return g, (g - 1.96 * se, g + 1.96 * se)


def perm_test(a, b, alternative="greater", max_exact=50000, n_mc=50000, seed=0):
    """Exact (or Monte Carlo) permutation test on mean(b) - mean(a)."""
    pooled = np.concatenate([a, b])
    n, nb = len(pooled), len(b)
    obs = b.mean() - a.mean()
    total = pooled.sum()
    if math.comb(n, nb) <= max_exact:
        diffs = []
        for idx in itertools.combinations(range(n), nb):
            sb = pooled[list(idx)].sum()
            diffs.append(sb / nb - (total - sb) / (n - nb))
        diffs = np.array(diffs)
        kind = "exact"
    else:
        rng = np.random.default_rng(seed)
        diffs = np.empty(n_mc)
        for i in range(n_mc):
            p = rng.permutation(pooled)
            diffs[i] = p[:nb].mean() - p[nb:].mean()
        kind = "MC"
    eps = 1e-12
    if alternative == "greater":
        p = np.mean(diffs >= obs - eps)
    else:
        p = np.mean(np.abs(diffs) >= abs(obs) - eps)
    return p, kind


def compare(rows, var, alternative="greater"):
    cond = np.array([r["condition"] for r in rows])
    y = col(rows, var)
    a, b = y[(cond == "A") & ~np.isnan(y)], y[(cond == "B") & ~np.isnan(y)]
    out = {"var": var, "nA": len(a), "nB": len(b)}
    if len(a) < 2 or len(b) < 2:
        out["error"] = "각 조건에 최소 2명 필요"
        return out
    t2 = stats.ttest_ind(b, a, equal_var=False)
    t1 = stats.ttest_ind(b, a, equal_var=False, alternative="greater")
    g, ci = hedges_g(a, b)
    try:
        mw = stats.mannwhitneyu(b, a, alternative="greater" if alternative == "greater" else "two-sided")
        mw_p = mw.pvalue
    except ValueError:
        mw_p = np.nan
    pp, kind = perm_test(a, b, alternative)
    # Welch df
    va, vb = a.var(ddof=1) / len(a), b.var(ddof=1) / len(b)
    df = (va + vb) ** 2 / (va ** 2 / (len(a) - 1) + vb ** 2 / (len(b) - 1)) if va + vb > 0 else np.nan
    out.update(mA=a.mean(), sdA=a.std(ddof=1), mB=b.mean(), sdB=b.std(ddof=1), t=t2.statistic, df=df,
               p_two=t2.pvalue, p_one=t1.pvalue, g=g, g_ci=ci, mw_p=mw_p, perm_p=pp, perm_kind=kind)
    return out


def ols(y, X, names):
    """OLS with intercept already in X. Returns list of (name, b, se, t, p), R2, adjR2, n."""
    mask = ~np.isnan(y) & ~np.isnan(X).any(axis=1)
    y, X = y[mask], X[mask]
    n, k = X.shape
    if n <= k:
        return None
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    dof = n - k
    sigma2 = resid @ resid / dof
    cov = sigma2 * np.linalg.pinv(X.T @ X)
    se = np.sqrt(np.diag(cov))
    tvals = beta / se
    pvals = 2 * stats.t.sf(np.abs(tvals), dof)
    ss_tot = ((y - y.mean()) ** 2).sum()
    r2 = 1 - (resid @ resid) / ss_tot if ss_tot > 0 else np.nan
    adj = 1 - (1 - r2) * (n - 1) / dof
    return list(zip(names, beta, se, tvals, pvals)), r2, adj, n, dof


def chi2_stat(table):
    table = np.asarray(table, float)
    exp = table.sum(1, keepdims=True) * table.sum(0, keepdims=True) / table.sum()
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.nansum(np.where(exp > 0, (table - exp) ** 2 / exp, 0))


def exact_perm_rxc(labels, groups, seed=0, n_mc=50000):
    """Permutation p for association between group (A/B) and categorical label (Freeman-Halton analogue)."""
    cats = sorted(set(labels))
    gs = ["A", "B"]

    def table(lbl):
        return [[sum(1 for l, g in zip(lbl, groups) if l == c and g == gg) for c in cats] for gg in gs]

    obs = chi2_stat(table(labels))
    rng = np.random.default_rng(seed)
    lab = np.array(labels)
    hits = sum(chi2_stat(table(rng.permutation(lab))) >= obs - 1e-12 for _ in range(n_mc))
    return obs, hits / n_mc, cats, table(labels)


# ---------------------------------------------------------------- report
def fmt_p(p):
    if p is None or (isinstance(p, float) and np.isnan(p)):
        return "—"
    return "< .001" if p < 0.001 else f"{p:.3f}".lstrip("0") if p < 1 else "1.000"


def pe(p):
    """'= .023' / '< .001' — p 앞에 붙여 쓰는 형식"""
    f = fmt_p(p)
    return f if f.startswith("<") else "= " + f


def fmt_cmp(c, one_sided=True):
    if "error" in c:
        return f"- {c['var']}: {c['error']}\n"
    lines = [
        f"| | A (n={c['nA']}) | B (n={c['nB']}) |",
        "|---|---|---|",
        f"| M (SD) | {c['mA']:.2f} ({c['sdA']:.2f}) | {c['mB']:.2f} ({c['sdB']:.2f}) |",
        "",
        f"- Welch t({c['df']:.1f}) = {c['t']:.2f}, p(two-sided) {pe(c['p_two'])}"
        + (f", p(one-sided, B>A) {pe(c['p_one'])}" if one_sided else ""),
        f"- Hedges' g (B−A) = {c['g']:.2f}, 95% CI [{c['g_ci'][0]:.2f}, {c['g_ci'][1]:.2f}]",
        f"- Permutation test ({c['perm_kind']}, {'one' if one_sided else 'two'}-sided) p {pe(c['perm_p'])}"
        f" · Mann-Whitney p {pe(c['mw_p'])}",
        "",
    ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--include-test", action="store_true", help="is_test=1 세션도 포함 (파일럿 데이터 점검용)")
    ap.add_argument("--out", default=None, help="마크다운 보고서 저장 경로")
    args = ap.parse_args()

    rows, dropped, dup = load(args.csv, args.include_test)
    out = []
    w = out.append
    cond = np.array([r["condition"] for r in rows])
    w("# Ownership Study — Analysis Report\n")
    w(f"- 입력: `{args.csv}`")
    w(f"- 분석 대상 N = {len(rows)} (A = {(cond == 'A').sum()}, B = {(cond == 'B').sum()})"
      f" · 제외: 미완료/테스트 {dropped}건, 중복 pid {dup}건\n")
    if len(rows) < 4:
        w("데이터가 너무 적어 분석을 건너뜁니다.")
        print("\n".join(out))
        return

    # ---------------- 1. reliability
    w("## 1. 척도 신뢰도\n")
    w("| 척도 | 문항 수 | 신뢰도 |\n|---|---|---|")
    for k in ["PO", "IA", "CC"]:
        a = cronbach_alpha([col(rows, i) for i in SCALES[k]])
        w(f"| {k} | {len(SCALES[k])} | α = {a:.2f} |")
    r, sb = spearman_brown(col(rows, "AU1"), col(rows, "AU2"))
    w(f"| AU | 2 | r = {r:.2f}, Spearman-Brown = {sb:.2f} |")
    w("\n> N이 작아 α 추정치가 불안정함. 원척도: PO α=.905 (Chung et al.), CC α=.84 (Gong & Chen).\n")

    # ---------------- 2. manipulation check
    w("## 2. 조작 점검 — 지각된 창작 통제감 (CC), 기대: B > A\n")
    w(fmt_cmp(compare(rows, "CC_mean")))

    # ---------------- 3. H1
    w("## 3. H1 — 심리적 소유감 (PO), 기대: B > A\n")
    w(fmt_cmp(compare(rows, "PO_mean")))

    # ---------------- 4. secondary
    w("## 4. 2차 — 지각된 저자성\n")
    w("### 4a. 자기평가 저자성 (AU, 양측)\n")
    w(fmt_cmp(compare(rows, "AU_mean", alternative="two-sided"), one_sided=False))
    w("### 4b. 공개 시 저자 표기 (declared credit)\n")
    credits = [r.get("credit") or "NA" for r in rows]
    groups = list(cond)
    cats = [c for c in ["self", "joint", "ai_main", "other"] if c in credits] + sorted(set(credits) - set(CREDIT_LABELS))
    w("| | " + " | ".join(CREDIT_LABELS.get(c, c) for c in cats) + " |")
    w("|---|" + "---|" * len(cats))
    for g in ["A", "B"]:
        cnt = Counter(c for c, gg in zip(credits, groups) if gg == g)
        w(f"| {g} | " + " | ".join(str(cnt.get(c, 0)) for c in cats) + " |")
    tab = [[sum(1 for c, gg in zip(credits, groups) if gg == g and (c == "self") == s) for s in (True, False)] for g in ["A", "B"]]
    _, p_f = stats.fisher_exact(tab)
    w(f"\n- Fisher's exact (2×2: 'Myself' vs. 그 외): p {pe(p_f)}")
    if len(set(credits)) > 1:
        chi, p_rc, _, _ = exact_perm_rxc(credits, groups)
        w(f"- 전체 표 permutation χ² test (Freeman-Halton 대응): χ² = {chi:.2f}, p ≈ {fmt_p(p_rc)}")
    # ownership–authorship divergence (ghostwriter effect)
    po, au = col(rows, "PO_mean"), col(rows, "AU_mean")
    diverge = sum(1 for p_, c in zip(po, credits) if p_ < 4 and c == "self")
    w(f"- 소유감 낮음(PO<4)인데 '나 자신'으로 표기: {diverge}명 (ghostwriter 패턴 확인용)")
    w(f"- PO–AU 상관 r = {np.corrcoef(po, au)[0, 1]:.2f}\n")

    # ---------------- 5. RQ2
    w("## 5. RQ2 (탐색) — 의도 일치도(IA)와 소유감(PO)\n")
    ia = col(rows, "IA_mean")
    b = (cond == "B").astype(float)
    one = np.ones(len(rows))
    w(f"- 전체 r(IA, PO) = {stats.pearsonr(ia, po)[0]:.2f}, p {pe(stats.pearsonr(ia, po)[1])}")
    for g in ["A", "B"]:
        m = cond == g
        if m.sum() >= 3:
            rr, pp = stats.pearsonr(ia[m], po[m])
            w(f"- 조건 {g}: r = {rr:.2f}, p {pe(pp)} (n={m.sum()})")
    w("")
    ia_c = ia - np.nanmean(ia)
    for title, X, names in [
        ("PO ~ IA + Condition", np.column_stack([one, ia_c, b]), ["Intercept", "IA (centered)", "Condition (B=1)"]),
        ("PO ~ IA × Condition (탐색)", np.column_stack([one, ia_c, b, ia_c * b]),
         ["Intercept", "IA (centered)", "Condition (B=1)", "IA × Condition"]),
    ]:
        res = ols(po, X, names)
        if res is None:
            continue
        coefs, r2, adj, n, dof = res
        w(f"**{title}** — R² = {r2:.2f}, adj. R² = {adj:.2f}, n = {n}, df = {dof}\n")
        w("| term | b | SE | t | p |\n|---|---|---|---|---|")
        for nm, bb, se, t, p in coefs:
            w(f"| {nm} | {bb:.2f} | {se:.2f} | {t:.2f} | {fmt_p(p)} |")
        w("")
    w("> 의도 일치도가 조건 효과를 설명(매개)하는지 판단하려면 N=12로는 부족함 — 방향성만 보고.\n")
    w(fmt_cmp(compare(rows, "IA_mean", alternative="two-sided"), one_sided=False))

    # ---------------- 6. covariates
    w("## 6. 공변량 통제 — PO ~ Condition + Quality + Effort\n")
    q, e = col(rows, "quality"), col(rows, "effort")
    res = ols(po, np.column_stack([one, b, (q - np.nanmean(q)) / 10, (e - np.nanmean(e)) / 10]),
              ["Intercept", "Condition (B=1)", "Quality (per 10pt)", "Effort (per 10pt)"])
    if res:
        coefs, r2, adj, n, dof = res
        w(f"R² = {r2:.2f}, adj. R² = {adj:.2f}, n = {n}, df = {dof}\n")
        w("| term | b | SE | t | p |\n|---|---|---|---|---|")
        for nm, bb, se, t, p in coefs:
            w(f"| {nm} | {bb:.2f} | {se:.2f} | {t:.2f} | {fmt_p(p)} |")
    w("")
    for v in ["quality", "effort"]:
        c = compare(rows, v, alternative="two-sided")
        if "error" not in c:
            w(f"- {v}: A {c['mA']:.1f} ({c['sdA']:.1f}) vs B {c['mB']:.1f} ({c['sdB']:.1f}), "
              f"Welch p {pe(c['p_two'])}, g = {c['g']:.2f}")
    w("")

    # ---------------- 6b. time/length confound check
    w("## 6b. 시간·길이 통제 점검 (교란 변인)\n")
    w("1차 프롬프트 작성은 두 조건이 동일(고정 시간, 같은 글자 수 범위). 1차 지표가 조건 간 비슷해야 이후 차이를 '결과를 보고 수정할 기회'의 효과로 해석 가능.\n")
    w("| 변수 | A M (SD) | B M (SD) | Welch p | g |\n|---|---|---|---|---|")
    for v in ["round1_chars", "round1_input_events", "round1_seconds", "final_prompt_chars", "overtime_seconds"]:
        c = compare(rows, v, alternative="two-sided")
        if "error" not in c and not np.isnan(c["t"]):
            w(f"| {v} | {c['mA']:.1f} ({c['sdA']:.1f}) | {c['mB']:.1f} ({c['sdB']:.1f}) | {fmt_p(c['p_two'])} | {c['g']:.2f} |")
        elif "error" not in c:
            w(f"| {v} | {c['mA']:.1f} ({c['sdA']:.1f}) | {c['mB']:.1f} ({c['sdB']:.1f}) | — | — |")
    bro = [r for r in rows if r["condition"] == "B"]
    rev = [r for r in bro if r.get("b_revised") == "1"]
    w(f"\n**B 조건 수정 여부**: {len(rev)} / {len(bro)}명이 1차 결과를 보고 프롬프트를 수정해 재생성.")
    if rev:
        for v in ["round2_chars", "round2_edit_distance", "round2_input_events", "round2_seconds", "b_decide_seconds"]:
            y = col(rev, v); y = y[~np.isnan(y)]
            if len(y):
                w(f"- {v}: M = {y.mean():.1f}" + (f", SD = {y.std(ddof=1):.1f}" if len(y) > 1 else "") + f" (n={len(y)})")
        po_rev, po_keep = col(rev, "PO_mean"), col([r for r in bro if r.get("b_revised") == "0"], "PO_mean")
        if len(po_keep):
            w(f"- B 내 PO: 수정함 M = {np.nanmean(po_rev):.2f} (n={len(po_rev)}) vs 그대로 확정 M = {np.nanmean(po_keep):.2f} (n={len(po_keep)}) — 자기선택이라 인과 해석 불가, 기술만")
    w("")
    L = col(rows, "final_prompt_chars")
    res = ols(po, np.column_stack([one, b, (L - np.nanmean(L)) / 100]), ["Intercept", "Condition (B=1)", "Final prompt length (per 100 chars)"])
    if res:
        coefs, r2, adj, n, dof = res
        w(f"**PO ~ Condition + Final prompt length** — R² = {r2:.2f}, n = {n}, df = {dof}\n")
        w("| term | b | SE | t | p |\n|---|---|---|---|---|")
        for nm, bb, se, t, p in coefs:
            w(f"| {nm} | {bb:.2f} | {se:.2f} | {t:.2f} | {fmt_p(p)} |")
    w("")

    # ---------------- 6c. world (stimulus) check
    worlds = sorted({r.get("world") or "NA" for r in rows})
    if len(worlds) > 1:
        w("## 6c. 세계관(자극) 점검\n")
        w("| | " + " | ".join(worlds) + " |\n|---|" + "---|" * len(worlds))
        for g in ["A", "B"]:
            w(f"| {g} | " + " | ".join(str(sum(1 for r in rows if r['condition'] == g and (r.get('world') or 'NA') == wd)) for wd in worlds) + " |")
        w("")
        for wd in worlds:
            for g in ["A", "B"]:
                y = col([r for r in rows if (r.get("world") or "NA") == wd and r["condition"] == g], "PO_mean")
                if len(y):
                    w(f"- {wd} · {g}: PO M = {np.nanmean(y):.2f} (n={len(y)})")
        wv = np.array([1.0 if (r.get("world") or "NA") == worlds[1] else 0.0 for r in rows])
        res = ols(po, np.column_stack([one, b, wv]), ["Intercept", "Condition (B=1)", f"World ({worlds[1]}=1)"])
        if res:
            coefs, r2, adj, n, dof = res
            w(f"\n**PO ~ Condition + World** — R² = {r2:.2f}, n = {n}, df = {dof}\n")
            w("| term | b | SE | t | p |\n|---|---|---|---|---|")
            for nm, bb, se, t, p in coefs:
                w(f"| {nm} | {bb:.2f} | {se:.2f} | {t:.2f} | {fmt_p(p)} |")
        w("\n> 조건 효과가 세계관과 무관하게 같은 방향인지 확인용. 셀당 3명이라 상호작용 검정은 하지 않음.\n")

    # ---------------- 7. process
    w("## 7. 과정 기록 (기술통계)\n")
    w("| 변수 | A M (SD) | B M (SD) |\n|---|---|---|")
    for v in ["n_generations", "n_failed_generations", "used_sketch", "gen_seconds", "concept_seconds", "sketch_seconds", "concept_chars", "total_minutes"]:
        y = col(rows, v)
        cell = []
        for g in ["A", "B"]:
            s = y[(cond == g) & ~np.isnan(y)]
            cell.append(f"{s.mean():.1f} ({s.std(ddof=1):.1f})" if len(s) > 1 else "—")
        w(f"| {v} | {cell[0]} | {cell[1]} |")
    tm = col(rows, "total_minutes")
    w(f"\n- 총 소요 시간: 최대 {np.nanmax(tm):.1f}분, 30분 초과 {int(np.nansum(tm > 30))}명")
    w(f"- 최소 글자 수 미달로 시간 초과한 참가자: {sum(1 for r in rows if to_num(r.get('overtime_seconds')) > 0)}명\n")

    # ---------------- 8. covariate balance
    w("## 8. 사전 특성 균형 점검\n")
    w("| 변수 | A M | B M | Welch p |\n|---|---|---|---|")
    for v in ["pre_ai_text_freq", "pre_ai_image_freq", "pre_ai_image_skill", "pre_art_exp", "pre_char_exp", "pre_draw_skill", "pre_age"]:
        c = compare(rows, v, alternative="two-sided")
        if "error" not in c:
            w(f"| {v} | {c['mA']:.2f} | {c['mB']:.2f} | {fmt_p(c['p_two'])} |")
    w("\n> n=6/조건에서 80% 검정력(α=.05, 단측)을 가지려면 d ≈ 1.54 이상 필요 (양측 ≈ 1.8; d = 0.8을 검출하려면 조건당 약 21명). p값보다 효과크기·CI 중심으로 해석할 것.")

    text = "\n".join(out)
    print(text)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        print(f"\n[saved] {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
