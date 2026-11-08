"""
분석 파이프라인 점검용 가짜 데이터 생성기 (웹앱 CSV와 동일한 열 구조).
실제 결과가 아님 — 보고서/발표에 사용 금지.

사용:  python3 analysis/make_fake_data.py [--n 12] [--effect 0.8] [--seed 1] [--out analysis/fake_data.csv]
"""
import argparse
import csv
import random


def clip7(x):
    return max(1, min(7, round(x)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=12)
    ap.add_argument("--effect", type=float, default=0.8, help="B 조건의 PO 증가분 (7점 척도 기준 원점수)")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--out", default="analysis/fake_data.csv")
    args = ap.parse_args()
    rnd = random.Random(args.seed)

    rows = []
    conds = ["A", "B"] * (args.n // 2) + ["A"] * (args.n % 2)
    rnd.shuffle(conds)
    for i, c in enumerate(conds):
        B = c == "B"
        ia_lat = rnd.gauss(4.2 + (0.7 if B else 0), 1.1)            # 의도 일치도
        po_lat = 2.0 + 0.45 * ia_lat + (args.effect * 0.5 if B else 0) + rnd.gauss(0, 0.8)
        cc_lat = rnd.gauss(4.0 + (1.0 if B else 0), 1.0)
        au_lat = po_lat + rnd.gauss(0.3, 0.7)
        n_gen = rnd.choice([2, 3, 3]) if B else 1
        r = {
            "pid": f"P{i + 1:02d}", "session_id": f"P{i + 1:02d}_fake", "condition": c, "is_test": 0, "completed": 1,
            "provider": "fake", "model": "fake", "started_at": f"2026-11-20T10:{i:02d}:00Z",
            "completed_at": f"2026-11-20T10:{i:02d}:59Z", "total_minutes": round(rnd.uniform(16, 26), 1),
            "pre_ai_text_freq": rnd.randint(2, 5), "pre_ai_image_freq": rnd.randint(1, 4), "pre_ai_image_skill": rnd.randint(2, 6),
            "pre_art_exp": rnd.randint(1, 4), "pre_char_exp": rnd.randint(1, 3), "pre_draw_skill": rnd.randint(1, 6),
            "pre_age": rnd.randint(21, 32), "pre_gender": rnd.choice(["여성", "남성"]), "pre_ai_tools": "ChatGPT",
            "concept_chars": rnd.randint(120, 400), "sketch_strokes": rnd.randint(15, 120), "sketch_source": "canvas",
            "sketch_seconds": rnd.randint(90, 240), "n_generations": n_gen, "n_failed_generations": 0,
            "n_prompt_revisions": n_gen - 1, "final_attempt_n": n_gen if rnd.random() < .8 else 1,
            "gen_seconds": rnd.randint(60, 140) if not B else rnd.randint(150, 330), "gen_timed_out": 0,
            "first_prompt": "fake", "final_prompt": "fake", "first_prompt_chars": rnd.randint(60, 200),
            "final_prompt_chars": rnd.randint(60, 260),
        }
        r["final_is_last"] = 1 if r["final_attempt_n"] == n_gen else 0
        for k, lat, n in [("PO", po_lat, 5), ("IA", ia_lat, 3), ("AU", au_lat, 2), ("CC", cc_lat, 3)]:
            vals = [clip7(lat + rnd.gauss(0, 0.5)) for _ in range(n)]
            for j, v in enumerate(vals, 1):
                r[f"{k}{j}"] = v
            r[f"{k}_mean"] = round(sum(vals) / n, 3)
        r["credit"] = "self" if au_lat > 5 else "joint" if au_lat > 3.5 else "ai_main"
        r["credit_other"] = ""
        r["quality"] = max(0, min(100, round(rnd.gauss(62 + (8 if B else 0), 15))))
        r["effort"] = max(0, min(100, round(rnd.gauss(55 + (12 if B else 0), 15))))
        r["open_ownership"] = r["open_process"] = ""
        rows.append(r)

    with open(args.out, "w", encoding="utf-8-sig", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        wr.writeheader()
        wr.writerows(rows)
    print(f"wrote {len(rows)} fake rows → {args.out}")


if __name__ == "__main__":
    main()
