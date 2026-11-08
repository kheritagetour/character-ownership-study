# Ownership Study — Analysis Report

- 입력: `analysis/fake_data.csv`
- 분석 대상 N = 12 (A = 6, B = 6) · 제외: 미완료/테스트 0건, 중복 pid 0건

## 1. 척도 신뢰도

| 척도 | 문항 수 | 신뢰도 |
|---|---|---|
| PO | 5 | α = 0.94 |
| IA | 3 | α = 0.97 |
| CC | 3 | α = 0.95 |
| AU | 2 | r = 0.91, Spearman-Brown = 0.95 |

> N이 작아 α 추정치가 불안정함. 원척도: PO α=.905 (Chung et al.), CC α=.84 (Gong & Chen).

## 2. 조작 점검 — 지각된 창작 통제감 (CC), 기대: B > A

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 3.28 (1.00) | 5.00 (1.15) |

- Welch t(9.8) = 2.76, p(two-sided) = .020, p(one-sided, B>A) = .010
- Hedges' g (B−A) = 1.47, 95% CI [0.20, 2.75]
- Permutation test (exact, one-sided) p = .015 · Mann-Whitney p = .018

## 3. H1 — 심리적 소유감 (PO), 기대: B > A

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 3.53 (0.82) | 4.00 (1.44) |

- Welch t(7.9) = 0.69, p(two-sided) = .509, p(one-sided, B>A) = .254
- Hedges' g (B−A) = 0.37, 95% CI [-0.77, 1.51]
- Permutation test (exact, one-sided) p = .266 · Mann-Whitney p = .211

## 4. 2차 — 지각된 저자성

### 4a. 자기평가 저자성 (AU, 양측)

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 4.75 (1.17) | 4.50 (1.87) |

- Welch t(8.4) = -0.28, p(two-sided) = .788
- Hedges' g (B−A) = -0.15, 95% CI [-1.28, 0.99]
- Permutation test (exact, two-sided) p = .872 · Mann-Whitney p = 1.000

### 4b. 공개 시 저자 표기 (declared credit)

| | Myself | Myself+AI | Mainly AI |
|---|---|---|---|
| A | 2 | 4 | 0 |
| B | 2 | 3 | 1 |

- Fisher's exact (2×2: 'Myself' vs. 그 외): p = 1.000
- 전체 표 permutation χ² test (Freeman-Halton 대응): χ² = 1.14, p ≈ 1.000
- 소유감 낮음(PO<4)인데 '나 자신'으로 표기: 1명 (ghostwriter 패턴 확인용)
- PO–AU 상관 r = 0.81

## 5. RQ2 (탐색) — 의도 일치도(IA)와 소유감(PO)

- 전체 r(IA, PO) = 0.66, p = .020
- 조건 A: r = 0.64, p = .167 (n=6)
- 조건 B: r = 0.71, p = .113 (n=6)

**PO ~ IA + Condition** — R² = 0.46, adj. R² = 0.34, n = 12, df = 9

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.59 | 0.38 | 9.46 | < .001 |
| IA (centered) | 0.39 | 0.15 | 2.62 | .028 |
| Condition (B=1) | 0.36 | 0.54 | 0.66 | .523 |

**PO ~ IA × Condition (탐색)** — R² = 0.51, adj. R² = 0.32, n = 12, df = 8

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.57 | 0.38 | 9.28 | < .001 |
| IA (centered) | 0.26 | 0.21 | 1.25 | .246 |
| Condition (B=1) | 0.36 | 0.54 | 0.65 | .532 |
| IA × Condition | 0.27 | 0.31 | 0.89 | .401 |

> 의도 일치도가 조건 효과를 설명(매개)하는지 판단하려면 N=12로는 부족함 — 방향성만 보고.

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 3.56 (1.99) | 3.83 (1.91) |

- Welch t(10.0) = 0.25, p(two-sided) = .810
- Hedges' g (B−A) = 0.13, 95% CI [-1.00, 1.26]
- Permutation test (exact, two-sided) p = .853 · Mann-Whitney p = .809

## 6. 공변량 통제 — PO ~ Condition + Quality + Effort

R² = 0.48, adj. R² = 0.29, n = 12, df = 8

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 2.60 | 0.54 | 4.86 | .001 |
| Condition (B=1) | 2.33 | 0.91 | 2.55 | .034 |
| Quality (per 10pt) | -0.98 | 0.38 | -2.56 | .034 |
| Effort (per 10pt) | -0.03 | 0.19 | -0.15 | .886 |

- quality: A 67.0 (8.2) vs B 85.8 (7.9), Welch p = .002, g = 2.16
- effort: A 60.2 (16.2) vs B 69.7 (16.2), Welch p = .334, g = 0.54

## 6b. 시간·길이 통제 점검 (교란 변인)

1차 프롬프트 작성은 두 조건이 동일(고정 시간, 같은 글자 수 범위). 1차 지표가 조건 간 비슷해야 이후 차이를 '결과를 보고 수정할 기회'의 효과로 해석 가능.

| 변수 | A M (SD) | B M (SD) | Welch p | g |
|---|---|---|---|---|
| round1_chars | 195.7 (50.9) | 153.3 (65.7) | .242 | -0.67 |
| round1_input_events | 155.7 (57.0) | 159.0 (57.9) | .922 | 0.05 |
| round1_seconds | 180.0 (0.0) | 180.0 (0.0) | — | — |
| final_prompt_chars | 195.7 (50.9) | 210.7 (83.1) | .716 | 0.20 |
| overtime_seconds | 0.0 (0.0) | 0.0 (0.0) | — | — |

**B 조건 수정 여부**: 6 / 6명이 1차 결과를 보고 프롬프트를 수정해 재생성.
- round2_chars: M = 210.7, SD = 83.1 (n=6)
- round2_edit_distance: M = 79.7, SD = 48.4 (n=6)
- round2_input_events: M = 68.3, SD = 40.8 (n=6)
- round2_seconds: M = 132.8, SD = 45.9 (n=6)
- b_decide_seconds: M = 23.3, SD = 12.8 (n=6)

**PO ~ Condition + Final prompt length** — R² = 0.07, n = 12, df = 9

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.51 | 0.50 | 7.05 | < .001 |
| Condition (B=1) | 0.51 | 0.71 | 0.72 | .491 |
| Final prompt length (per 100 chars) | -0.27 | 0.56 | -0.49 | .638 |

## 6c. 세계관(자극) 점검

| | academy | city |
|---|---|---|
| A | 3 | 3 |
| B | 3 | 3 |

- academy · A: PO M = 3.13 (n=3)
- academy · B: PO M = 5.07 (n=3)
- city · A: PO M = 3.93 (n=3)
- city · B: PO M = 2.93 (n=3)

**PO ~ Condition + World** — R² = 0.14, n = 12, df = 9

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.87 | 0.58 | 6.61 | < .001 |
| Condition (B=1) | 0.47 | 0.68 | 0.69 | .507 |
| World (city=1) | -0.67 | 0.68 | -0.99 | .349 |

> 조건 효과가 세계관과 무관하게 같은 방향인지 확인용. 셀당 3명이라 상호작용 검정은 하지 않음.

## 7. 과정 기록 (기술통계)

| 변수 | A M (SD) | B M (SD) |
|---|---|---|
| n_generations | 1.0 (0.0) | 2.0 (0.0) |
| n_failed_generations | 0.0 (0.0) | 0.0 (0.0) |
| used_sketch | 1.0 (0.0) | 1.0 (0.0) |
| gen_seconds | 228.2 (8.3) | 399.7 (21.9) |
| sketch_seconds | 145.5 (55.9) | 150.8 (27.0) |
| concept_chars | 314.5 (61.5) | 266.7 (53.7) |
| total_minutes | 23.7 (3.1) | 23.7 (3.2) |

- 최소 글자 수 미달로 시간 초과한 참가자: 0명

## 8. 사전 특성 균형 점검

| 변수 | A M | B M | Welch p |
|---|---|---|---|
| pre_ai_text_freq | 3.17 | 3.17 | 1.000 |
| pre_ai_image_freq | 2.00 | 3.00 | .201 |
| pre_ai_image_skill | 3.33 | 3.83 | .484 |
| pre_art_exp | 2.17 | 1.83 | .526 |
| pre_char_exp | 2.33 | 1.83 | .363 |
| pre_draw_skill | 2.83 | 2.33 | .451 |
| pre_age | 25.67 | 28.67 | .210 |

> n=6/조건에서 80% 검정력(α=.05, 단측)을 가지려면 d ≈ 1.54 이상 필요 (양측 ≈ 1.8; d = 0.8을 검출하려면 조건당 약 21명). p값보다 효과크기·CI 중심으로 해석할 것.
