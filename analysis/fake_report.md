# Ownership Study — Analysis Report

- 입력: `analysis/fake_data.csv`
- 분석 대상 N = 12 (A = 6, B = 6) · 제외: 미완료/테스트 0건, 중복 pid 0건

## 1. 척도 신뢰도

| 척도 | 문항 수 | 신뢰도 |
|---|---|---|
| PO | 5 | α = 0.96 |
| IA | 3 | α = 0.97 |
| CC | 3 | α = 0.97 |
| AU | 2 | r = 0.82, Spearman-Brown = 0.90 |

> N이 작아 α 추정치가 불안정함. 원척도: PO α=.905 (Chung et al.), CC α=.84 (Gong & Chen).

## 2. 조작 점검 — 지각된 창작 통제감 (CC), 기대: B > A

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 3.72 (1.53) | 4.56 (1.61) |

- Welch t(10.0) = 0.92, p(two-sided) = .380, p(one-sided, B>A) = .190
- Hedges' g (B−A) = 0.49, 95% CI [-0.66, 1.64]
- Permutation test (exact, one-sided) p = .184 · Mann-Whitney p = .211

## 3. H1 — 심리적 소유감 (PO), 기대: B > A

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 3.40 (0.79) | 4.50 (1.72) |

- Welch t(7.0) = 1.42, p(two-sided) = .198, p(one-sided, B>A) = .099
- Hedges' g (B−A) = 0.76, 95% CI [-0.41, 1.93]
- Permutation test (exact, one-sided) p = .101 · Mann-Whitney p = .086

## 4. 2차 — 지각된 저자성

### 4a. 자기평가 저자성 (AU, 양측)

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 4.00 (0.84) | 4.42 (1.83) |

- Welch t(7.0) = 0.51, p(two-sided) = .627
- Hedges' g (B−A) = 0.27, 95% CI [-0.87, 1.41]
- Permutation test (exact, two-sided) p = .714 · Mann-Whitney p = .225

### 4b. 공개 시 저자 표기 (declared credit)

| | Myself | Myself+AI | Mainly AI |
|---|---|---|---|
| A | 0 | 5 | 1 |
| B | 2 | 3 | 1 |

- Fisher's exact (2×2: 'Myself' vs. 그 외): p = .455
- 전체 표 permutation χ² test (Freeman-Halton 대응): χ² = 2.50, p ≈ .696
- 소유감 낮음(PO<4)인데 '나 자신'으로 표기: 0명 (ghostwriter 패턴 확인용)
- PO–AU 상관 r = 0.86

## 5. RQ2 (탐색) — 의도 일치도(IA)와 소유감(PO)

- 전체 r(IA, PO) = 0.62, p = .032
- 조건 A: r = 0.48, p = .332 (n=6)
- 조건 B: r = 0.63, p = .183 (n=6)

**PO ~ IA + Condition** — R² = 0.43, adj. R² = 0.30, n = 12, df = 9

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.65 | 0.49 | 7.38 | < .001 |
| IA (centered) | 0.43 | 0.21 | 2.02 | .074 |
| Condition (B=1) | 0.60 | 0.72 | 0.83 | .429 |

**PO ~ IA × Condition (탐색)** — R² = 0.47, adj. R² = 0.27, n = 12, df = 8

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.54 | 0.52 | 6.76 | < .001 |
| IA (centered) | 0.23 | 0.33 | 0.71 | .496 |
| Condition (B=1) | 0.62 | 0.74 | 0.84 | .424 |
| IA × Condition | 0.36 | 0.44 | 0.82 | .434 |

> 의도 일치도가 조건 효과를 설명(매개)하는지 판단하려면 N=12로는 부족함 — 방향성만 보고.

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 3.17 (1.64) | 4.33 (1.83) |

- Welch t(9.9) = 1.16, p(two-sided) = .272
- Hedges' g (B−A) = 0.62, 95% CI [-0.54, 1.78]
- Permutation test (exact, two-sided) p = .292 · Mann-Whitney p = .336

## 6. 공변량 통제 — PO ~ Condition + Quality + Effort

R² = 0.58, adj. R² = 0.42, n = 12, df = 8

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 2.99 | 0.53 | 5.64 | < .001 |
| Condition (B=1) | 1.91 | 0.86 | 2.21 | .058 |
| Quality (per 10pt) | -0.74 | 0.27 | -2.78 | .024 |
| Effort (per 10pt) | -0.01 | 0.20 | -0.04 | .969 |

- quality: A 67.8 (9.6) vs B 78.5 (15.1), Welch p = .181, g = 0.78
- effort: A 52.7 (21.4) vs B 79.2 (11.9), Welch p = .030, g = 1.42

## 6b. 시간·길이 통제 점검 (교란 변인)

1차 프롬프트 작성은 두 조건이 동일(고정 시간, 같은 글자 수 범위). 1차 지표가 조건 간 비슷해야 이후 차이를 '결과를 보고 수정할 기회'의 효과로 해석 가능.

| 변수 | A M (SD) | B M (SD) | Welch p | g |
|---|---|---|---|---|
| round1_chars | 186.3 (62.0) | 155.3 (52.1) | .371 | -0.50 |
| round1_input_events | 164.0 (42.3) | 146.8 (56.5) | .566 | -0.32 |
| round1_seconds | 180.0 (0.0) | 180.0 (0.0) | — | — |
| final_prompt_chars | 186.3 (62.0) | 200.8 (66.0) | .703 | 0.21 |
| overtime_seconds | 0.0 (0.0) | 0.0 (0.0) | — | — |

**B 조건 수정 여부**: 4 / 6명이 1차 결과를 보고 프롬프트를 수정해 재생성.
- round2_chars: M = 231.8, SD = 58.1 (n=4)
- round2_edit_distance: M = 92.8, SD = 41.0 (n=4)
- round2_input_events: M = 93.2, SD = 31.5 (n=4)
- round2_seconds: M = 105.5, SD = 64.6 (n=4)
- b_decide_seconds: M = 17.2, SD = 10.9 (n=4)
- B 내 PO: 수정함 M = 4.15 (n=4) vs 그대로 확정 M = 5.20 (n=2) — 자기선택이라 인과 해석 불가, 기술만

**PO ~ Condition + Final prompt length** — R² = 0.38, n = 12, df = 9

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.32 | 0.50 | 6.64 | < .001 |
| Condition (B=1) | 1.25 | 0.71 | 1.76 | .112 |
| Final prompt length (per 100 chars) | -1.05 | 0.60 | -1.75 | .114 |

## 7. 과정 기록 (기술통계)

| 변수 | A M (SD) | B M (SD) |
|---|---|---|
| n_generations | 1.0 (0.0) | 1.7 (0.5) |
| n_failed_generations | 0.0 (0.0) | 0.0 (0.0) |
| used_sketch | 1.0 (0.0) | 1.0 (0.0) |
| gen_seconds | 225.8 (10.6) | 343.7 (94.5) |
| sketch_seconds | 144.3 (51.5) | 156.0 (41.3) |
| concept_chars | 257.5 (95.7) | 278.5 (42.9) |
| total_minutes | 22.1 (1.5) | 22.7 (3.0) |

- 최소 글자 수 미달로 시간 초과한 참가자: 0명

## 8. 사전 특성 균형 점검

| 변수 | A M | B M | Welch p |
|---|---|---|---|
| pre_ai_text_freq | 3.83 | 3.50 | .583 |
| pre_ai_image_freq | 2.50 | 2.33 | .828 |
| pre_ai_image_skill | 3.50 | 4.50 | .237 |
| pre_art_exp | 2.50 | 1.50 | .065 |
| pre_char_exp | 2.50 | 1.67 | .111 |
| pre_draw_skill | 2.50 | 3.67 | .237 |
| pre_age | 26.67 | 25.83 | .745 |

> n=6/조건에서 80% 검정력(α=.05, 단측)을 가지려면 d ≈ 1.54 이상 필요 (양측 ≈ 1.8; d = 0.8을 검출하려면 조건당 약 21명). p값보다 효과크기·CI 중심으로 해석할 것.
