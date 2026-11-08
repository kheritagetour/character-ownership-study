# Ownership Study — Analysis Report

- 입력: `analysis/fake_data.csv`
- 분석 대상 N = 12 (A = 6, B = 6) · 제외: 미완료/테스트 0건, 중복 pid 0건

## 1. 척도 신뢰도

| 척도 | 문항 수 | 신뢰도 |
|---|---|---|
| PO | 5 | α = 0.95 |
| IA | 3 | α = 0.96 |
| CC | 3 | α = 0.94 |
| AU | 2 | r = 0.70, Spearman-Brown = 0.82 |

> N이 작아 α 추정치가 불안정함. 원척도: PO α=.905 (Chung et al.), CC α=.84 (Gong & Chen).

## 2. 조작 점검 — 지각된 창작 통제감 (CC), 기대: B > A

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 4.17 (1.26) | 5.22 (1.38) |

- Welch t(9.9) = 1.39, p(two-sided) = .196, p(one-sided, B>A) = .098
- Hedges' g (B−A) = 0.74, 95% CI [-0.43, 1.91]
- Permutation test (exact, one-sided) p = .096 · Mann-Whitney p = .130

## 3. H1 — 심리적 소유감 (PO), 기대: B > A

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 3.97 (0.85) | 4.63 (1.58) |

- Welch t(7.7) = 0.91, p(two-sided) = .391, p(one-sided, B>A) = .196
- Hedges' g (B−A) = 0.48, 95% CI [-0.66, 1.63]
- Permutation test (exact, one-sided) p = .206 · Mann-Whitney p = .344

## 4. 2차 — 지각된 저자성

### 4a. 자기평가 저자성 (AU, 양측)

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 4.00 (0.45) | 4.67 (1.47) |

- Welch t(5.9) = 1.06, p(two-sided) = .330
- Hedges' g (B−A) = 0.57, 95% CI [-0.59, 1.72]
- Permutation test (exact, two-sided) p = .374 · Mann-Whitney p = .466

### 4b. 공개 시 저자 표기 (declared credit)

| | Myself | Myself+AI | Mainly AI |
|---|---|---|---|
| A | 0 | 6 | 0 |
| B | 3 | 1 | 2 |

- Fisher's exact (2×2: 'Myself' vs. 그 외): p = .182
- 전체 표 permutation χ² test (Freeman-Halton 대응): χ² = 8.57, p ≈ .015
- 소유감 낮음(PO<4)인데 '나 자신'으로 표기: 0명 (ghostwriter 패턴 확인용)
- PO–AU 상관 r = 0.78

## 5. RQ2 (탐색) — 의도 일치도(IA)와 소유감(PO)

- 전체 r(IA, PO) = 0.87, p < .001
- 조건 A: r = 0.77, p = .072 (n=6)
- 조건 B: r = 0.94, p = .006 (n=6)

**PO ~ IA + Condition** — R² = 0.81, adj. R² = 0.76, n = 12, df = 9

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 4.03 | 0.25 | 16.07 | < .001 |
| IA (centered) | 0.74 | 0.13 | 5.82 | < .001 |
| Condition (B=1) | 0.54 | 0.35 | 1.53 | .160 |

**PO ~ IA × Condition (탐색)** — R² = 0.83, adj. R² = 0.77, n = 12, df = 8

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 4.01 | 0.25 | 16.05 | < .001 |
| IA (centered) | 0.55 | 0.23 | 2.41 | .043 |
| Condition (B=1) | 0.55 | 0.35 | 1.56 | .157 |
| IA × Condition | 0.28 | 0.27 | 1.04 | .328 |

> 의도 일치도가 조건 효과를 설명(매개)하는지 판단하려면 N=12로는 부족함 — 방향성만 보고.

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 4.17 (1.21) | 4.33 (1.79) |

- Welch t(8.8) = 0.19, p(two-sided) = .854
- Hedges' g (B−A) = 0.10, 95% CI [-1.03, 1.23]
- Permutation test (exact, two-sided) p = .851 · Mann-Whitney p = 1.000

## 6. 공변량 통제 — PO ~ Condition + Quality + Effort

R² = 0.24, adj. R² = -0.04, n = 12, df = 8

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.90 | 0.53 | 7.33 | < .001 |
| Condition (B=1) | 0.79 | 0.76 | 1.04 | .329 |
| Quality (per 10pt) | 0.31 | 0.28 | 1.14 | .289 |
| Effort (per 10pt) | -0.29 | 0.30 | -0.99 | .352 |

- quality: A 65.7 (7.5) vs B 67.5 (20.4), Welch p = .843, g = 0.11
- effort: A 49.5 (12.6) vs B 55.8 (16.0), Welch p = .464, g = 0.41

## 6b. 시간·길이 통제 점검 (교란 변인)

설계상 두 조건 모두 2단계 × 고정 시간, 같은 글자 수 범위. 아래가 조건 간 비슷해야 '결과 확인 여부' 효과로 해석 가능.

| 변수 | A M (SD) | B M (SD) | Welch p | g |
|---|---|---|---|---|
| round1_chars | 113.2 (58.5) | 165.8 (57.9) | .148 | 0.84 |
| round2_chars | 145.2 (45.7) | 240.0 (66.9) | .019 | 1.53 |
| final_prompt_chars | 145.2 (45.7) | 240.0 (66.9) | .019 | 1.53 |
| round1_input_events | 214.3 (54.3) | 201.8 (80.0) | .759 | -0.17 |
| round2_input_events | 76.5 (42.5) | 47.0 (34.7) | .218 | -0.70 |
| round2_edit_distance | 33.0 (17.6) | 107.7 (42.9) | .006 | 2.10 |
| round1_seconds | 180.0 (0.0) | 180.0 (0.0) | — | — |
| round2_seconds | 180.0 (0.0) | 180.0 (0.0) | — | — |
| overtime_seconds | 0.0 (0.0) | 0.0 (0.0) | — | — |

> round2_edit_distance는 2단계에서 프롬프트를 얼마나 고쳤는지(문자 편집거리). B에서 크게 나오는 것은 조작의 일부로 해석.

**PO ~ Condition + Final prompt length** — R² = 0.12, n = 12, df = 9

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 4.21 | 0.63 | 6.65 | < .001 |
| Condition (B=1) | 0.19 | 1.02 | 0.18 | .858 |
| Final prompt length (per 100 chars) | 0.51 | 0.72 | 0.70 | .500 |

## 7. 과정 기록 (기술통계)

| 변수 | A M (SD) | B M (SD) |
|---|---|---|
| n_generations | 1.0 (0.0) | 2.0 (0.0) |
| n_failed_generations | 0.0 (0.0) | 0.0 (0.0) |
| gen_seconds | 385.7 (11.4) | 413.3 (13.5) |
| sketch_seconds | 157.0 (54.6) | 169.5 (41.3) |
| concept_chars | 252.8 (89.0) | 291.7 (85.5) |
| total_minutes | 24.1 (2.5) | 24.3 (2.9) |

- 최소 글자 수 미달로 시간 초과한 참가자: 0명

## 8. 사전 특성 균형 점검

| 변수 | A M | B M | Welch p |
|---|---|---|---|
| pre_ai_text_freq | 3.17 | 2.50 | .186 |
| pre_ai_image_freq | 2.50 | 1.67 | .265 |
| pre_ai_image_skill | 4.50 | 4.17 | .695 |
| pre_art_exp | 2.83 | 2.17 | .267 |
| pre_char_exp | 1.83 | 1.33 | .361 |
| pre_draw_skill | 3.33 | 3.50 | .877 |
| pre_age | 25.67 | 27.00 | .512 |

> n=6/조건에서 80% 검정력(α=.05, 단측)을 가지려면 d ≈ 1.54 이상 필요 (양측 ≈ 1.8; d = 0.8을 검출하려면 조건당 약 21명). p값보다 효과크기·CI 중심으로 해석할 것.
