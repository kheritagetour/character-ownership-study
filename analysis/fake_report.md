# Ownership Study — Analysis Report

- 입력: `analysis/fake_data.csv`
- 분석 대상 N = 16 (A = 8, B = 8) · 제외: 미완료/테스트 0건, 중복 pid 0건

## 1. 척도 신뢰도

| 척도 | 문항 수 | 신뢰도 |
|---|---|---|
| PO | 5 | α = 0.95 |
| IA | 3 | α = 0.90 |
| CC | 3 | α = 0.87 |
| AU | 2 | r = 0.88, Spearman-Brown = 0.93 |

> N이 작아 α 추정치가 불안정함. 원척도: PO α=.905 (Chung et al.), CC α=.84 (Gong & Chen).

## 2. 조작 점검 — 지각된 창작 통제감 (CC), 기대: B > A

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 3.50 (1.02) | 4.54 (1.10) |

- Welch t(13.9) = 1.96, p(two-sided) = .070, p(one-sided, B>A) = .035
- Hedges' g (B−A) = 0.93, 95% CI [-0.10, 1.96]
- Permutation test (exact, one-sided) p = .035 · Mann-Whitney p = .039

## 3. H1 — 심리적 소유감 (PO), 기대: B > A

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 3.90 (0.94) | 4.27 (1.26) |

- Welch t(12.9) = 0.67, p(two-sided) = .512, p(one-sided, B>A) = .256
- Hedges' g (B−A) = 0.32, 95% CI [-0.67, 1.30]
- Permutation test (exact, one-sided) p = .271 · Mann-Whitney p = .229

## 4. 2차 — 지각된 저자성

### 4a. 자기평가 저자성 (AU, 양측)

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 3.88 (0.95) | 4.75 (1.87) |

- Welch t(10.4) = 1.18, p(two-sided) = .265
- Hedges' g (B−A) = 0.56, 95% CI [-0.44, 1.56]
- Permutation test (exact, two-sided) p = .298 · Mann-Whitney p = .168

### 4b. 공개 시 저자 표기 (declared credit)

| | Myself | Myself+AI | Mainly AI |
|---|---|---|---|
| A | 0 | 6 | 2 |
| B | 4 | 3 | 1 |

- Fisher's exact (2×2: 'Myself' vs. 그 외): p = .077
- 전체 표 permutation χ² test (Freeman-Halton 대응): χ² = 5.33, p ≈ .101
- 소유감 낮음(PO<4)인데 '나 자신'으로 표기: 0명 (ghostwriter 패턴 확인용)
- PO–AU 상관 r = 0.82

### 4c. 결과 만족도 (1–7) · 지각된 AI 기여도 (0 = 전적으로 나 – 100 = 전적으로 AI), 양측

**satisfaction**

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 4.50 (2.07) | 4.38 (0.92) |

- Welch t(9.6) = -0.16, p(two-sided) = .879
- Hedges' g (B−A) = -0.07, 95% CI [-1.05, 0.91]
- Permutation test (exact, two-sided) p = 1.000 · Mann-Whitney p = .956

**ai_contribution**

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 46.88 (13.57) | 55.25 (10.70) |

- Welch t(13.3) = 1.37, p(two-sided) = .193
- Hedges' g (B−A) = 0.65, 95% CI [-0.36, 1.65]
- Permutation test (exact, two-sided) p = .199 · Mann-Whitney p = .141


## 5. RQ2 (탐색) — 의도 일치도(IA)와 소유감(PO)

- 전체 r(IA, PO) = 0.45, p = .083
- 조건 A: r = 0.37, p = .371 (n=8)
- 조건 B: r = 0.48, p = .230 (n=8)

**PO ~ IA + Condition** — R² = 0.21, adj. R² = 0.09, n = 16, df = 13

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 4.25 | 0.42 | 10.14 | < .001 |
| IA (centered) | 0.53 | 0.31 | 1.73 | .107 |
| Condition (B=1) | -0.32 | 0.66 | -0.48 | .638 |

**PO ~ IA × Condition (탐색)** — R² = 0.22, adj. R² = 0.03, n = 16, df = 12

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 4.16 | 0.49 | 8.45 | < .001 |
| IA (centered) | 0.41 | 0.48 | 0.84 | .415 |
| Condition (B=1) | -0.30 | 0.68 | -0.44 | .670 |
| IA × Condition | 0.23 | 0.64 | 0.35 | .732 |

> 의도 일치도가 조건 효과를 설명(매개)하는지 판단하려면 N=16으로는 부족함 — 방향성만 보고.

| | A (n=8) | B (n=8) |
|---|---|---|
| M (SD) | 3.29 (0.84) | 4.58 (0.96) |

- Welch t(13.8) = 2.87, p(two-sided) = .013
- Hedges' g (B−A) = 1.35, 95% CI [0.27, 2.44]
- Permutation test (exact, two-sided) p = .018 · Mann-Whitney p = .020

## 6. 공변량 통제 — PO ~ Condition + Quality + Effort

R² = 0.03, adj. R² = -0.21, n = 16, df = 12

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.87 | 0.54 | 7.11 | < .001 |
| Condition (B=1) | 0.43 | 0.91 | 0.48 | .643 |
| Quality (per 10pt) | 0.01 | 0.16 | 0.03 | .974 |
| Effort (per 10pt) | -0.03 | 0.24 | -0.14 | .889 |

- quality: A 56.6 (23.3) vs B 83.1 (15.5), Welch p = .020, g = 1.27
- effort: A 58.9 (13.5) vs B 79.9 (13.5), Welch p = .008, g = 1.47

## 6b. 시간·길이 통제 점검 (교란 변인)

1차 이미지는 A/B 모두 컨셉 시트(고정 템플릿 프롬프트) + 스케치로 자동 생성 → 참가자 입력량은 컨셉 시트 분량(concept_chars)으로 비교. 1차 결과를 보는 시간을 고정: A는 살펴보기, B는 같은 시간 동안 수정 요청 작성 → image1_view_seconds가 조건 간 같아야 함. 컨셉 시트 분량은 공변량 모형으로도 확인.

| 변수 | A M (SD) | B M (SD) | Welch p | g |
|---|---|---|---|---|
| image1_view_seconds | 120.0 (0.0) | 120.0 (0.0) | — | — |
| concept_chars | 358.6 (108.8) | 352.2 (95.4) | .903 | -0.06 |
| concept_seconds | 374.5 (81.4) | 382.5 (46.8) | .814 | 0.11 |
| auto_prompt_chars | 424.9 (78.0) | 391.9 (73.0) | .397 | -0.41 |
| final_prompt_chars | 424.9 (78.0) | 490.1 (90.4) | .145 | 0.73 |

**B 조건 수정 여부**: 7 / 8명이 수정 요청을 적어 재생성 (나머지는 비워 두어 1차가 최종).
- revision_chars: M = 102.3, SD = 11.5 (n=7)
- revision_input_events: M = 45.0, SD = 22.3 (n=7)
- revision_seconds: M = 120.0, SD = 0.0 (n=7)
- B 내 PO: 수정함 M = 4.34 (n=7) vs 수정 안 함 M = 3.80 (n=1) — 자기선택이라 인과 해석 불가, 기술만

**PO ~ Condition + Concept sheet length** — R² = 0.15, n = 16, df = 13

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.91 | 0.38 | 10.19 | < .001 |
| Condition (B=1) | 0.35 | 0.54 | 0.65 | .529 |
| Concept sheet length (per 100 chars) | -0.37 | 0.28 | -1.32 | .211 |

## 6c. 세계관(자극) 점검

| | academy | city |
|---|---|---|
| A | 4 | 4 |
| B | 4 | 4 |

- academy · A: PO M = 3.95 (n=4)
- academy · B: PO M = 3.90 (n=4)
- city · A: PO M = 3.85 (n=4)
- city · B: PO M = 4.65 (n=4)

**PO ~ Condition + World** — R² = 0.05, n = 16, df = 13

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.74 | 0.49 | 7.56 | < .001 |
| Condition (B=1) | 0.37 | 0.57 | 0.66 | .523 |
| World (city=1) | 0.32 | 0.57 | 0.57 | .579 |

> 조건 효과가 세계관과 무관하게 같은 방향인지 확인용. 셀당 인원이 적어 상호작용 검정은 하지 않음.

## 6d. 창작 경험 층 점검 (E = 있음, N = 없음)

층마다 따로 블록 배정했으므로 층 × 조건 인원이 균형이어야 함.

| | E | N |
|---|---|---|
| A | 4 | 4 |
| B | 4 | 4 |

- E · A: PO M = 3.65 (n=4)
- E · B: PO M = 3.95 (n=4)
- N · A: PO M = 4.15 (n=4)
- N · B: PO M = 4.60 (n=4)

**PO ~ Condition + Stratum** — R² = 0.11, n = 16, df = 13

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 4.19 | 0.48 | 8.71 | < .001 |
| Condition (B=1) | 0.37 | 0.56 | 0.68 | .511 |
| Stratum (경험 있음=1) | -0.58 | 0.56 | -1.04 | .319 |

> 경험 유무에 따라 조건 효과 방향이 같은지 기술적으로만 확인 (셀당 인원이 적어 상호작용 검정은 하지 않음).

## 7. 과정 기록 (기술통계)

| 변수 | A M (SD) | B M (SD) |
|---|---|---|
| n_generations | 1.0 (0.0) | 1.9 (0.4) |
| n_failed_generations | 0.0 (0.0) | 0.0 (0.0) |
| used_sketch | 1.0 (0.0) | 1.0 (0.0) |
| gen_seconds | 156.8 (10.9) | 199.2 (20.6) |
| concept_seconds | 374.5 (81.4) | 382.5 (46.8) |
| sketch_seconds | 188.1 (56.4) | 162.0 (60.1) |
| concept_chars | 358.6 (108.8) | 352.2 (95.4) |
| total_minutes | 22.3 (1.8) | 21.3 (2.8) |

- 총 소요 시간: 최대 24.8분, 30분 초과 0명

## 8. 사전 특성 균형 점검

| 변수 | A M | B M | Welch p |
|---|---|---|---|
| pre_ai_text_freq | 3.88 | 3.00 | .112 |
| pre_ai_image_freq | 2.00 | 2.75 | .201 |
| pre_ai_image_skill | 4.00 | 4.12 | .864 |
| pre_art_exp | 2.38 | 2.12 | .578 |
| pre_char_exp | 2.38 | 1.62 | .095 |
| pre_draw_skill | 3.00 | 3.00 | 1.000 |
| pre_age | 25.88 | 26.75 | .634 |

> n=8/조건(N=16)에서 80% 검정력(α=.05, 단측)을 가지려면 d ≈ 1.31 이상 필요 (양측 ≈ 1.51; d = 0.8을 검출하려면 조건당 약 21명). p값보다 효과크기·CI 중심으로 해석할 것.
