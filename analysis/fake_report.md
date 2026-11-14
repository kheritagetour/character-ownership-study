# Ownership Study — Analysis Report

- 입력: `analysis/fake_data.csv`
- 분석 대상 N = 16 (A = 8, B = 8) · 제외: 미완료/테스트 0건, 중복 pid 0건

## 1. 척도 신뢰도

| 척도 | 문항 수 | 신뢰도 |
|---|---|---|
| PO | 5 | α = 0.92 |
| IA | 3 | α = 0.95 |
| CC | 3 | α = 0.78 |
| AU | 2 | r = 0.66, Spearman-Brown = 0.80 |

> N이 작아 α 추정치가 불안정함. 원척도: PO α=.905 (Chung et al.), CC α=.84 (Gong & Chen).

## 2. 조작 점검 — 지각된 창작 통제감 (CC), 기대: B > A

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 3.29 (0.55) | 4.13 (0.59) |

- Welch t(13.9) = 2.93, p(two-sided) = .011, p(one-sided, B>A) = .006
- Hedges' g (B−A) = 1.39, 95% CI [0.29, 2.48]
- Permutation test (exact, one-sided) p = .008 · Mann-Whitney p = .008

## 3. H1 — 심리적 소유감 (PO), 기대: B > A

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 3.90 (0.89) | 4.60 (0.81) |

- Welch t(13.9) = 1.64, p(two-sided) = .123, p(one-sided, B>A) = .061
- Hedges' g (B−A) = 0.78, 95% CI [-0.24, 1.79]
- Permutation test (exact, one-sided) p = .068 · Mann-Whitney p = .077

## 4. 2차 — 지각된 저자성

### 4a. 자기평가 저자성 (AU, 양측)

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 4.12 (1.30) | 4.81 (0.80) |

- Welch t(11.6) = 1.27, p(two-sided) = .228
- Hedges' g (B−A) = 0.60, 95% CI [-0.40, 1.60]
- Permutation test (exact, two-sided) p = .272 · Mann-Whitney p = .090

### 4b. 공개 시 저자 표기 (declared credit)

| | Myself | Myself+AI | Mainly AI |
|---|---|---|---|
| A | 1 | 4 | 3 |
| B | 5 | 2 | 1 |

- Fisher's exact (2×2: 'Myself' vs. 그 외): p = .119
- 전체 표 permutation χ² test (Freeman-Halton 대응): χ² = 4.33, p ≈ .232
- 소유감 낮음(PO<4)인데 '나 자신'으로 표기: 0명 (ghostwriter 패턴 확인용)
- PO–AU 상관 r = 0.78

### 4c. 결과 만족도 (1–7) · 지각된 AI 기여도 (0 = 전적으로 나 – 100 = 전적으로 AI), 양측

**satisfaction**

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 4.12 (0.99) | 5.38 (1.19) |

- Welch t(13.6) = 2.29, p(two-sided) = .039
- Hedges' g (B−A) = 1.08, 95% CI [0.03, 2.13]
- Permutation test (exact, two-sided) p = .065 · Mann-Whitney p = .068

**ai_contribution**

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 50.75 (17.88) | 46.25 (17.56) |

- Welch t(14.0) = -0.51, p(two-sided) = .619
- Hedges' g (B−A) = -0.24, 95% CI [-1.22, 0.74]
- Permutation test (exact, two-sided) p = .628 · Mann-Whitney p = .430


## 5. RQ2 (탐색) — 의도 일치도(IA)와 소유감(PO)

- 전체 r(IA, PO) = 0.44, p = .085
- 조건 A: r = 0.37, p = .371 (n=8)
- 조건 B: r = 0.05, p = .914 (n=8)

**PO ~ IA + Condition** — R² = 0.21, adj. R² = 0.09, n = 16, df = 13

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 4.10 | 0.37 | 10.95 | < .001 |
| IA (centered) | 0.21 | 0.23 | 0.90 | .383 |
| Condition (B=1) | 0.30 | 0.61 | 0.49 | .630 |

**PO ~ IA × Condition (탐색)** — R² = 0.22, adj. R² = 0.03, n = 16, df = 12

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 4.17 | 0.42 | 10.03 | < .001 |
| IA (centered) | 0.29 | 0.29 | 0.98 | .346 |
| Condition (B=1) | 0.39 | 0.66 | 0.59 | .569 |
| IA × Condition | -0.24 | 0.52 | -0.46 | .657 |

> 의도 일치도가 조건 효과를 설명(매개)하는지 판단하려면 N=16으로는 부족함 — 방향성만 보고.

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 3.38 (1.15) | 5.25 (0.77) |

- Welch t(12.3) = 3.84, p(two-sided) = .002
- Hedges' g (B−A) = 1.81, 95% CI [0.65, 2.98]
- Permutation test (exact, two-sided) p = .005 · Mann-Whitney p = .010

## 6. 공변량 통제 — PO ~ Condition + Quality + Effort

R² = 0.28, adj. R² = 0.10, n = 16, df = 12

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.88 | 0.30 | 12.78 | < .001 |
| Condition (B=1) | 0.74 | 0.43 | 1.73 | .109 |
| Quality (per 10pt) | 0.24 | 0.19 | 1.26 | .231 |
| Effort (per 10pt) | -0.08 | 0.13 | -0.59 | .564 |

- quality: A 67.1 (11.2) vs B 66.5 (12.7), Welch p = .918, g = -0.05
- effort: A 55.6 (16.5) vs B 59.5 (19.0), Welch p = .670, g = 0.21

## 6b. 시간·길이 통제 점검 (교란 변인)

프롬프트 작성 시간 총량을 맞춤 (세션 단위 시간 고정): A는 단일 프롬프트 고정 시간, B는 1차 고정 + 결과를 보며 수정 고정 시간(합 = A). B는 수정하지 않아도 수정 시간을 보냄 → 작성 시간 합(write_seconds_total)이 조건 간 같아야 함. 최종 프롬프트 길이는 조건 간 다를 수 있어 공변량 모형으로 확인.

| 변수 | A M (SD) | B M (SD) | Welch p | g |
|---|---|---|---|---|
| write_seconds_total | 300.0 (0.0) | 300.0 (0.0) | — | — |
| final_prompt_chars | 178.6 (78.6) | 191.0 (30.4) | .687 | 0.20 |
| round1_chars | 178.6 (78.6) | 137.0 (39.1) | .209 | -0.63 |
| round1_input_events | 158.9 (90.9) | 188.6 (70.3) | .477 | 0.35 |
| overtime_seconds | 0.0 (0.0) | 0.0 (0.0) | — | — |

**B 조건 수정 여부**: 6 / 8명이 수정 시간에 프롬프트를 바꿔 재생성 (나머지는 1차가 최종).
- round2_chars: M = 194.5, SD = 34.9 (n=6)
- round2_edit_distance: M = 80.3, SD = 41.9 (n=6)
- round2_input_events: M = 86.7, SD = 46.4 (n=6)
- round2_seconds: M = 120.0, SD = 0.0 (n=6)
- B 내 PO: 수정함 M = 4.80 (n=6) vs 그대로 확정 M = 4.00 (n=2) — 자기선택이라 인과 해석 불가, 기술만

**PO ~ Condition + Final prompt length** — R² = 0.20, n = 16, df = 13

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.88 | 0.31 | 12.65 | < .001 |
| Condition (B=1) | 0.74 | 0.44 | 1.69 | .115 |
| Final prompt length (per 100 chars) | -0.29 | 0.39 | -0.75 | .468 |

## 6c. 세계관(자극) 점검

| | academy | city |
|---|---|---|
| A | 4 | 4 |
| B | 4 | 4 |

- academy · A: PO M = 3.80 (n=4)
- academy · B: PO M = 4.50 (n=4)
- city · A: PO M = 4.00 (n=4)
- city · B: PO M = 4.70 (n=4)

**PO ~ Condition + World** — R² = 0.17, n = 16, df = 13

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.80 | 0.38 | 10.01 | < .001 |
| Condition (B=1) | 0.70 | 0.44 | 1.60 | .134 |
| World (city=1) | 0.20 | 0.44 | 0.46 | .656 |

> 조건 효과가 세계관과 무관하게 같은 방향인지 확인용. 셀당 인원이 적어 상호작용 검정은 하지 않음.

## 6d. 창작 경험 층 점검 (E = 있음, N = 없음)

층마다 따로 블록 배정했으므로 층 × 조건 인원이 균형이어야 함.

| | E | N |
|---|---|---|
| A | 4 | 4 |
| B | 4 | 4 |

- E · A: PO M = 3.95 (n=4)
- E · B: PO M = 4.40 (n=4)
- N · A: PO M = 3.85 (n=4)
- N · B: PO M = 4.80 (n=4)

**PO ~ Condition + Stratum** — R² = 0.17, n = 16, df = 13

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.98 | 0.38 | 10.43 | < .001 |
| Condition (B=1) | 0.70 | 0.44 | 1.59 | .136 |
| Stratum (경험 있음=1) | -0.15 | 0.44 | -0.34 | .739 |

> 경험 유무에 따라 조건 효과 방향이 같은지 기술적으로만 확인 (셀당 인원이 적어 상호작용 검정은 하지 않음).

## 7. 과정 기록 (기술통계)

| 변수 | A M (SD) | B M (SD) |
|---|---|---|
| n_generations | 1.0 (0.0) | 1.8 (0.5) |
| n_failed_generations | 0.0 (0.0) | 0.0 (0.0) |
| used_sketch | 1.0 (0.0) | 1.0 (0.0) |
| gen_seconds | 227.6 (8.7) | 347.5 (81.8) |
| concept_seconds | 340.5 (55.7) | 374.1 (56.2) |
| sketch_seconds | 172.6 (43.1) | 168.8 (42.5) |
| concept_chars | 402.8 (102.3) | 359.9 (78.9) |
| total_minutes | 23.8 (2.2) | 25.4 (2.5) |

- 총 소요 시간: 최대 27.8분, 30분 초과 0명
- 최소 글자 수 미달로 시간 초과한 참가자: 0명

## 8. 사전 특성 균형 점검

| 변수 | A M | B M | Welch p |
|---|---|---|---|
| pre_ai_text_freq | 3.75 | 3.25 | .429 |
| pre_ai_image_freq | 2.88 | 2.38 | .464 |
| pre_ai_image_skill | 4.38 | 4.50 | .887 |
| pre_art_exp | 2.12 | 1.88 | .594 |
| pre_char_exp | 2.62 | 1.88 | .111 |
| pre_draw_skill | 3.88 | 4.00 | .888 |
| pre_age | 27.00 | 27.75 | .654 |

> n=8/조건(N=16)에서 80% 검정력(α=.05, 단측)을 가지려면 d ≈ 1.31 이상 필요 (양측 ≈ 1.51; d = 0.8을 검출하려면 조건당 약 21명). p값보다 효과크기·CI 중심으로 해석할 것.
