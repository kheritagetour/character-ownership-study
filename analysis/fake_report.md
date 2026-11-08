# Ownership Study — Analysis Report

- 입력: `analysis/fake_data.csv`
- 분석 대상 N = 12 (A = 6, B = 6) · 제외: 미완료/테스트 0건, 중복 pid 0건

## 1. 척도 신뢰도

| 척도 | 문항 수 | 신뢰도 |
|---|---|---|
| PO | 5 | α = 0.90 |
| IA | 3 | α = 0.93 |
| CC | 3 | α = 0.50 |
| AU | 2 | r = 0.79, Spearman-Brown = 0.88 |

> N이 작아 α 추정치가 불안정함. 원척도: PO α=.905 (Chung et al.), CC α=.84 (Gong & Chen).

## 2. 조작 점검 — 지각된 창작 통제감 (CC), 기대: B > A

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 4.39 (0.33) | 4.67 (0.42) |

- Welch t(9.4) = 1.27, p(two-sided) = .233, p(one-sided, B>A) = .116
- Hedges' g (B−A) = 0.68, 95% CI [-0.48, 1.84]
- Permutation test (exact, one-sided) p = .117 · Mann-Whitney p = .135

## 3. H1 — 심리적 소유감 (PO), 기대: B > A

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 3.90 (0.65) | 4.90 (0.90) |

- Welch t(9.1) = 2.20, p(two-sided) = .055, p(one-sided, B>A) = .027
- Hedges' g (B−A) = 1.17, 95% CI [-0.05, 2.40]
- Permutation test (exact, one-sided) p = .034 · Mann-Whitney p = .032

## 4. 2차 — 지각된 저자성

### 4a. 자기평가 저자성 (AU, 양측)

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 4.42 (1.07) | 5.58 (0.80) |

- Welch t(9.3) = 2.14, p(two-sided) = .060
- Hedges' g (B−A) = 1.14, 95% CI [-0.08, 2.36]
- Permutation test (exact, two-sided) p = .084 · Mann-Whitney p = .060

### 4b. 공개 시 저자 표기 (declared credit)

| | Myself | Myself+AI |
|---|---|---|
| A | 2 | 4 |
| B | 3 | 3 |

- Fisher's exact (2×2: 'Myself' vs. 그 외): p = 1.000
- 전체 표 permutation χ² test (Freeman-Halton 대응): χ² = 0.34, p ≈ 1.000
- 소유감 낮음(PO<4)인데 '나 자신'으로 표기: 1명 (ghostwriter 패턴 확인용)
- PO–AU 상관 r = 0.49

## 5. RQ2 (탐색) — 의도 일치도(IA)와 소유감(PO)

- 전체 r(IA, PO) = 0.50, p = .099
- 조건 A: r = 0.16, p = .767 (n=6)
- 조건 B: r = 0.43, p = .395 (n=6)

**PO ~ IA + Condition** — R² = 0.40, adj. R² = 0.27, n = 12, df = 9

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 4.02 | 0.34 | 11.91 | < .001 |
| IA (centered) | 0.22 | 0.21 | 1.07 | .311 |
| Condition (B=1) | 0.77 | 0.50 | 1.53 | .161 |

**PO ~ IA × Condition (탐색)** — R² = 0.41, adj. R² = 0.19, n = 12, df = 8

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.96 | 0.39 | 10.15 | < .001 |
| IA (centered) | 0.11 | 0.38 | 0.28 | .787 |
| Condition (B=1) | 0.80 | 0.53 | 1.49 | .174 |
| IA × Condition | 0.18 | 0.46 | 0.38 | .713 |

> 의도 일치도가 조건 효과를 설명(매개)하는지 판단하려면 N=12로는 부족함 — 방향성만 보고.

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 3.39 (0.98) | 4.44 (1.38) |

- Welch t(9.0) = 1.53, p(two-sided) = .160
- Hedges' g (B−A) = 0.82, 95% CI [-0.36, 1.99]
- Permutation test (exact, two-sided) p = .171 · Mann-Whitney p = .295

## 6. 공변량 통제 — PO ~ Condition + Quality + Effort

R² = 0.53, adj. R² = 0.35, n = 12, df = 8

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.79 | 0.31 | 12.36 | < .001 |
| Condition (B=1) | 1.21 | 0.44 | 2.73 | .026 |
| Quality (per 10pt) | 0.05 | 0.13 | 0.38 | .716 |
| Effort (per 10pt) | -0.23 | 0.15 | -1.53 | .166 |

- quality: A 71.0 (14.8) vs B 69.3 (22.3), Welch p = .882, g = -0.08
- effort: A 54.0 (19.6) vs B 63.0 (14.2), Welch p = .386, g = 0.49

## 6b. 시간·길이 통제 점검 (교란 변인)

1차 프롬프트 작성은 두 조건이 동일(고정 시간, 같은 글자 수 범위). 1차 지표가 조건 간 비슷해야 이후 차이를 '결과를 보고 수정할 기회'의 효과로 해석 가능.

| 변수 | A M (SD) | B M (SD) | Welch p | g |
|---|---|---|---|---|
| round1_chars | 138.8 (73.0) | 175.5 (80.4) | .428 | 0.44 |
| round1_input_events | 176.3 (61.2) | 170.8 (81.9) | .898 | -0.07 |
| round1_seconds | 180.0 (0.0) | 180.0 (0.0) | — | — |
| final_prompt_chars | 138.8 (73.0) | 232.7 (114.1) | .126 | 0.90 |
| overtime_seconds | 0.0 (0.0) | 0.0 (0.0) | — | — |

**B 조건 수정 여부**: 5 / 6명이 1차 결과를 보고 프롬프트를 수정해 재생성.
- round2_chars: M = 263.2, SD = 96.4 (n=5)
- round2_edit_distance: M = 81.6, SD = 25.8 (n=5)
- round2_input_events: M = 86.8, SD = 47.0 (n=5)
- round2_seconds: M = 150.4, SD = 17.8 (n=5)
- b_decide_seconds: M = 21.6, SD = 14.3 (n=5)
- B 내 PO: 수정함 M = 4.88 (n=5) vs 그대로 확정 M = 5.00 (n=1) — 자기선택이라 인과 해석 불가, 기술만

**PO ~ Condition + Final prompt length** — R² = 0.33, n = 12, df = 9

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.94 | 0.36 | 10.91 | < .001 |
| Condition (B=1) | 0.93 | 0.54 | 1.71 | .121 |
| Final prompt length (per 100 chars) | 0.08 | 0.27 | 0.29 | .782 |

## 6c. 세계관(자극) 점검

| | academy | city |
|---|---|---|
| A | 3 | 3 |
| B | 3 | 3 |

- academy · A: PO M = 3.73 (n=3)
- academy · B: PO M = 5.40 (n=3)
- city · A: PO M = 4.07 (n=3)
- city · B: PO M = 4.40 (n=3)

**PO ~ Condition + World** — R² = 0.36, n = 12, df = 9

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 4.07 | 0.40 | 10.07 | < .001 |
| Condition (B=1) | 1.00 | 0.47 | 2.15 | .060 |
| World (city=1) | -0.33 | 0.47 | -0.72 | .493 |

> 조건 효과가 세계관과 무관하게 같은 방향인지 확인용. 셀당 3명이라 상호작용 검정은 하지 않음.

## 7. 과정 기록 (기술통계)

| 변수 | A M (SD) | B M (SD) |
|---|---|---|
| n_generations | 1.0 (0.0) | 1.8 (0.4) |
| n_failed_generations | 0.0 (0.0) | 0.0 (0.0) |
| used_sketch | 1.0 (0.0) | 1.0 (0.0) |
| gen_seconds | 222.3 (9.0) | 323.2 (47.9) |
| concept_seconds | 311.5 (61.3) | 292.0 (48.4) |
| sketch_seconds | 170.8 (46.9) | 198.5 (27.1) |
| concept_chars | 234.7 (82.7) | 285.7 (74.6) |
| total_minutes | 24.8 (1.9) | 23.6 (2.2) |

- 총 소요 시간: 최대 27.5분, 30분 초과 0명
- 최소 글자 수 미달로 시간 초과한 참가자: 0명

## 8. 사전 특성 균형 점검

| 변수 | A M | B M | Welch p |
|---|---|---|---|
| pre_ai_text_freq | 3.33 | 4.50 | .085 |
| pre_ai_image_freq | 3.00 | 1.83 | .087 |
| pre_ai_image_skill | 5.00 | 3.67 | .055 |
| pre_art_exp | 1.50 | 1.50 | 1.000 |
| pre_char_exp | 2.33 | 1.67 | .188 |
| pre_draw_skill | 4.00 | 3.83 | .890 |
| pre_age | 25.50 | 27.67 | .227 |

> n=6/조건에서 80% 검정력(α=.05, 단측)을 가지려면 d ≈ 1.54 이상 필요 (양측 ≈ 1.8; d = 0.8을 검출하려면 조건당 약 21명). p값보다 효과크기·CI 중심으로 해석할 것.
