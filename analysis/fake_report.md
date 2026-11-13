# Ownership Study — Analysis Report

- 입력: `analysis/fake_data.csv`
- 분석 대상 N = 16 (A = 8, B = 8) · 제외: 미완료/테스트 0건, 중복 pid 0건

## 1. 척도 신뢰도

| 척도 | 문항 수 | 신뢰도 |
|---|---|---|
| PO | 5 | α = 0.90 |
| IA | 3 | α = 0.91 |
| CC | 3 | α = 0.94 |
| AU | 2 | r = 0.81, Spearman-Brown = 0.89 |

> N이 작아 α 추정치가 불안정함. 원척도: PO α=.905 (Chung et al.), CC α=.84 (Gong & Chen).

## 2. 조작 점검 — 지각된 창작 통제감 (CC), 기대: B > A

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 3.83 (1.31) | 5.29 (1.08) |

- Welch t(13.5) = 2.43, p(two-sided) = .029, p(one-sided, B>A) = .015
- Hedges' g (B−A) = 1.15, 95% CI [0.09, 2.21]
- Permutation test (exact, one-sided) p = .015 · Mann-Whitney p = .028

## 3. H1 — 심리적 소유감 (PO), 기대: B > A

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 3.90 (0.91) | 4.62 (0.43) |

- Welch t(10.0) = 2.03, p(two-sided) = .070, p(one-sided, B>A) = .035
- Hedges' g (B−A) = 0.96, 95% CI [-0.08, 1.99]
- Permutation test (exact, one-sided) p = .035 · Mann-Whitney p = .033

## 4. 2차 — 지각된 저자성

### 4a. 자기평가 저자성 (AU, 양측)

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 4.25 (1.22) | 4.75 (1.22) |

- Welch t(14.0) = 0.82, p(two-sided) = .428
- Hedges' g (B−A) = 0.39, 95% CI [-0.60, 1.38]
- Permutation test (exact, two-sided) p = .486 · Mann-Whitney p = .367

### 4b. 공개 시 저자 표기 (declared credit)

| | Myself | Myself+AI | Mainly AI |
|---|---|---|---|
| A | 2 | 4 | 2 |
| B | 2 | 4 | 2 |

- Fisher's exact (2×2: 'Myself' vs. 그 외): p = 1.000
- 전체 표 permutation χ² test (Freeman-Halton 대응): χ² = 0.00, p ≈ 1.000
- 소유감 낮음(PO<4)인데 '나 자신'으로 표기: 0명 (ghostwriter 패턴 확인용)
- PO–AU 상관 r = 0.71

### 4c. 결과 만족도 (1–7) · 지각된 AI 기여도 (0 = 전적으로 나 – 100 = 전적으로 AI), 양측

**satisfaction**

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 4.88 (0.99) | 4.50 (1.31) |

- Welch t(13.0) = -0.65, p(two-sided) = .530
- Hedges' g (B−A) = -0.31, 95% CI [-1.29, 0.68]
- Permutation test (exact, two-sided) p = .679 · Mann-Whitney p = .696

**ai_contribution**

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 53.62 (9.62) | 51.00 (12.68) |

- Welch t(13.1) = -0.47, p(two-sided) = .649
- Hedges' g (B−A) = -0.22, 95% CI [-1.20, 0.76]
- Permutation test (exact, two-sided) p = .659 · Mann-Whitney p = .798


## 5. RQ2 (탐색) — 의도 일치도(IA)와 소유감(PO)

- 전체 r(IA, PO) = 0.55, p = .026
- 조건 A: r = 0.49, p = .216 (n=8)
- 조건 B: r = 0.22, p = .609 (n=8)

**PO ~ IA + Condition** — R² = 0.37, adj. R² = 0.27, n = 16, df = 13

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 4.05 | 0.25 | 16.07 | < .001 |
| IA (centered) | 0.27 | 0.16 | 1.71 | .110 |
| Condition (B=1) | 0.43 | 0.38 | 1.15 | .272 |

**PO ~ IA × Condition (탐색)** — R² = 0.39, adj. R² = 0.23, n = 16, df = 12

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 4.08 | 0.26 | 15.45 | < .001 |
| IA (centered) | 0.33 | 0.19 | 1.73 | .110 |
| Condition (B=1) | 0.49 | 0.40 | 1.22 | .245 |
| IA × Condition | -0.21 | 0.37 | -0.57 | .577 |

> 의도 일치도가 조건 효과를 설명(매개)하는지 판단하려면 N=16으로는 부족함 — 방향성만 보고.

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 3.58 (1.38) | 4.67 (0.82) |

- Welch t(11.4) = 1.91, p(two-sided) = .081
- Hedges' g (B−A) = 0.90, 95% CI [-0.12, 1.93]
- Permutation test (exact, two-sided) p = .078 · Mann-Whitney p = .113

## 6. 공변량 통제 — PO ~ Condition + Quality + Effort

R² = 0.41, adj. R² = 0.27, n = 16, df = 12

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.85 | 0.26 | 15.00 | < .001 |
| Condition (B=1) | 0.83 | 0.39 | 2.16 | .052 |
| Quality (per 10pt) | -0.24 | 0.14 | -1.68 | .119 |
| Effort (per 10pt) | 0.13 | 0.14 | 0.93 | .368 |

- quality: A 66.2 (12.9) vs B 75.8 (12.1), Welch p = .151, g = 0.72
- effort: A 58.8 (10.4) vs B 68.1 (15.3), Welch p = .177, g = 0.68

## 6b. 시간·길이 통제 점검 (교란 변인)

프롬프트 작성 시간 총량을 맞춤: A는 단일 프롬프트(고정 시간), B는 1차(고정, A의 절반) + 결과를 본 뒤 선택적 수정(최대 나머지 절반). 생성에 실제로 쓰인 작성 시간 합(write_seconds_total)과 최종 프롬프트 길이가 조건 간 비슷해야 차이를 '결과를 보고 수정할 기회'의 효과로 해석 가능. B에서 수정을 안 하면 작성 시간이 A보다 짧아짐(조작에 포함되는 차이) → 아래 표와 공변량 모형으로 확인.

| 변수 | A M (SD) | B M (SD) | Welch p | g |
|---|---|---|---|---|
| write_seconds_total | 240.0 (0.0) | 183.4 (14.0) | < .001 | -5.42 |
| final_prompt_chars | 194.6 (53.0) | 221.4 (25.3) | .226 | 0.61 |
| round1_chars | 194.6 (53.0) | 155.6 (34.4) | .106 | -0.83 |
| round1_input_events | 180.8 (52.0) | 195.4 (85.1) | .686 | 0.20 |
| overtime_seconds | 0.0 (0.0) | 0.0 (0.0) | — | — |

**B 조건 수정 여부**: 8 / 8명이 1차 결과를 보고 프롬프트를 수정해 재생성.
- round2_chars: M = 221.4, SD = 25.3 (n=8)
- round2_edit_distance: M = 96.8, SD = 40.2 (n=8)
- round2_input_events: M = 92.1, SD = 43.2 (n=8)
- round2_seconds: M = 63.4, SD = 14.0 (n=8)
- b_decide_seconds: M = 20.4, SD = 12.1 (n=8)

**PO ~ Condition + Final prompt length** — R² = 0.30, n = 16, df = 13

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.97 | 0.26 | 15.44 | < .001 |
| Condition (B=1) | 0.58 | 0.37 | 1.56 | .142 |
| Final prompt length (per 100 chars) | 0.52 | 0.45 | 1.15 | .270 |

## 6c. 세계관(자극) 점검

| | academy | city |
|---|---|---|
| A | 4 | 4 |
| B | 4 | 4 |

- academy · A: PO M = 4.00 (n=4)
- academy · B: PO M = 4.80 (n=4)
- city · A: PO M = 3.80 (n=4)
- city · B: PO M = 4.45 (n=4)

**PO ~ Condition + World** — R² = 0.26, n = 16, df = 13

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 4.04 | 0.31 | 12.84 | < .001 |
| Condition (B=1) | 0.72 | 0.36 | 2.00 | .067 |
| World (city=1) | -0.28 | 0.36 | -0.76 | .462 |

> 조건 효과가 세계관과 무관하게 같은 방향인지 확인용. 셀당 인원이 적어 상호작용 검정은 하지 않음.

## 6d. 창작 경험 층 점검 (E = 있음, N = 없음)

층마다 따로 블록 배정했으므로 층 × 조건 인원이 균형이어야 함.

| | E | N |
|---|---|---|
| A | 4 | 4 |
| B | 4 | 4 |

- E · A: PO M = 3.75 (n=4)
- E · B: PO M = 4.70 (n=4)
- N · A: PO M = 4.05 (n=4)
- N · B: PO M = 4.55 (n=4)

**PO ~ Condition + Stratum** — R² = 0.23, n = 16, df = 13

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.94 | 0.32 | 12.28 | < .001 |
| Condition (B=1) | 0.72 | 0.37 | 1.96 | .072 |
| Stratum (경험 있음=1) | -0.08 | 0.37 | -0.20 | .843 |

> 경험 유무에 따라 조건 효과 방향이 같은지 기술적으로만 확인 (셀당 인원이 적어 상호작용 검정은 하지 않음).

## 7. 과정 기록 (기술통계)

| 변수 | A M (SD) | B M (SD) |
|---|---|---|
| n_generations | 1.0 (0.0) | 2.0 (0.0) |
| n_failed_generations | 0.0 (0.0) | 0.0 (0.0) |
| used_sketch | 1.0 (0.0) | 1.0 (0.0) |
| gen_seconds | 225.2 (6.7) | 361.0 (45.8) |
| concept_seconds | 359.5 (59.4) | 335.2 (44.2) |
| sketch_seconds | 180.0 (42.2) | 134.9 (33.5) |
| concept_chars | 450.8 (93.3) | 386.8 (156.6) |
| total_minutes | 24.1 (3.2) | 26.3 (1.5) |

- 총 소요 시간: 최대 27.7분, 30분 초과 0명
- 최소 글자 수 미달로 시간 초과한 참가자: 0명

## 8. 사전 특성 균형 점검

| 변수 | A M | B M | Welch p |
|---|---|---|---|
| pre_ai_text_freq | 3.88 | 3.25 | .340 |
| pre_ai_image_freq | 2.12 | 2.75 | .295 |
| pre_ai_image_skill | 3.50 | 4.62 | .137 |
| pre_art_exp | 2.00 | 2.12 | .759 |
| pre_char_exp | 2.12 | 2.75 | .085 |
| pre_draw_skill | 2.88 | 3.88 | .256 |
| pre_age | 28.12 | 26.50 | .386 |

> n=8/조건(N=16)에서 80% 검정력(α=.05, 단측)을 가지려면 d ≈ 1.31 이상 필요 (양측 ≈ 1.51; d = 0.8을 검출하려면 조건당 약 21명). p값보다 효과크기·CI 중심으로 해석할 것.
