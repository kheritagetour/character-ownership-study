# Ownership Study — Analysis Report

- 입력: `analysis/fake_data.csv`
- 분석 대상 N = 12 (A = 6, B = 6) · 제외: 미완료/테스트 0건, 중복 pid 0건

## 1. 척도 신뢰도

| 척도 | 문항 수 | 신뢰도 |
|---|---|---|
| PO | 5 | α = 0.93 |
| IA | 3 | α = 0.94 |
| CC | 3 | α = 0.84 |
| AU | 2 | r = 0.91, Spearman-Brown = 0.95 |

> N이 작아 α 추정치가 불안정함. 원척도: PO α=.905 (Chung et al.), CC α=.84 (Gong & Chen).

## 2. 조작 점검 — 지각된 창작 통제감 (CC), 기대: B > A

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 3.50 (0.72) | 4.83 (0.96) |

- Welch t(9.3) = 2.72, p(two-sided) = .023, p(one-sided, B>A) = .012
- Hedges' g (B−A) = 1.45, 95% CI [0.18, 2.72]
- Permutation test (exact, one-sided) p = .014 · Mann-Whitney p = .022

## 3. H1 — 심리적 소유감 (PO), 기대: B > A

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 3.93 (1.06) | 4.17 (0.88) |

- Welch t(9.7) = 0.41, p(two-sided) = .688, p(one-sided, B>A) = .344
- Hedges' g (B−A) = 0.22, 95% CI [-0.91, 1.36]
- Permutation test (exact, one-sided) p = .363 · Mann-Whitney p = .405

## 4. 2차 — 지각된 저자성

### 4a. 자기평가 저자성 (AU, 양측)

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 4.17 (1.21) | 5.17 (0.93) |

- Welch t(9.4) = 1.60, p(two-sided) = .142
- Hedges' g (B−A) = 0.85, 95% CI [-0.33, 2.04]
- Permutation test (exact, two-sided) p = .171 · Mann-Whitney p = .195

### 4b. 공개 시 저자 표기 (declared credit)

| | Myself | Myself+AI | Mainly AI |
|---|---|---|---|
| A | 1 | 3 | 2 |
| B | 3 | 3 | 0 |

- Fisher's exact (2×2: 'Myself' vs. 그 외): p = .545
- 전체 표 permutation χ² test (Freeman-Halton 대응): χ² = 3.00, p ≈ .290
- 소유감 낮음(PO<4)인데 '나 자신'으로 표기: 1명 (ghostwriter 패턴 확인용)
- PO–AU 상관 r = 0.57

## 5. RQ2 (탐색) — 의도 일치도(IA)와 소유감(PO)

- 전체 r(IA, PO) = 0.45, p = .146
- 조건 A: r = 0.99, p < .001 (n=6)
- 조건 B: r = 0.07, p = .888 (n=6)

**PO ~ IA + Condition** — R² = 0.24, adj. R² = 0.07, n = 12, df = 9

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.87 | 0.37 | 10.41 | < .001 |
| IA (centered) | 0.39 | 0.24 | 1.62 | .140 |
| Condition (B=1) | 0.36 | 0.53 | 0.68 | .511 |

**PO ~ IA × Condition (탐색)** — R² = 0.59, adj. R² = 0.43, n = 12, df = 8

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.75 | 0.29 | 12.76 | < .001 |
| IA (centered) | 1.07 | 0.32 | 3.31 | .011 |
| Condition (B=1) | 0.42 | 0.41 | 1.01 | .340 |
| IA × Condition | -1.03 | 0.40 | -2.59 | .032 |

> 의도 일치도가 조건 효과를 설명(매개)하는지 판단하려면 N=12로는 부족함 — 방향성만 보고.

| | A (n=6) | B (n=6) |
|---|---|---|
| M (SD) | 4.28 (0.98) | 3.94 (1.39) |

- Welch t(9.0) = -0.48, p(two-sided) = .642
- Hedges' g (B−A) = -0.26, 95% CI [-1.39, 0.88]
- Permutation test (exact, two-sided) p = .684 · Mann-Whitney p = .517

## 6. 공변량 통제 — PO ~ Condition + Quality + Effort

R² = 0.04, adj. R² = -0.32, n = 12, df = 8

| term | b | SE | t | p |
|---|---|---|---|---|
| Intercept | 4.03 | 0.50 | 8.05 | < .001 |
| Condition (B=1) | 0.03 | 0.79 | 0.04 | .966 |
| Quality (per 10pt) | 0.03 | 0.22 | 0.12 | .904 |
| Effort (per 10pt) | 0.09 | 0.21 | 0.45 | .668 |

- quality: A 67.7 (19.2) vs B 81.2 (11.3), Welch p = .175, g = 0.79
- effort: A 54.3 (20.4) vs B 72.0 (11.5), Welch p = .102, g = 0.99

## 7. 과정 기록 (기술통계)

| 변수 | A M (SD) | B M (SD) |
|---|---|---|
| n_generations | 1.0 (0.0) | 2.3 (0.5) |
| n_prompt_revisions | 0.0 (0.0) | 1.3 (0.5) |
| gen_seconds | 94.3 (18.9) | 216.3 (53.4) |
| first_prompt_chars | 134.8 (47.0) | 123.5 (45.7) |
| final_prompt_chars | 167.5 (46.6) | 187.5 (37.5) |
| sketch_seconds | 140.0 (56.2) | 180.5 (43.1) |
| concept_chars | 276.8 (64.3) | 291.7 (116.6) |
| total_minutes | 19.7 (3.6) | 20.6 (1.9) |

- B 조건에서 마지막이 아닌 이전 생성물을 최종 선택한 참가자: 1명
- 생성 단계 시간 초과: 0명

## 8. 사전 특성 균형 점검

| 변수 | A M | B M | Welch p |
|---|---|---|---|
| pre_ai_text_freq | 3.17 | 3.00 | .804 |
| pre_ai_image_freq | 2.50 | 2.17 | .543 |
| pre_ai_image_skill | 4.50 | 4.00 | .613 |
| pre_art_exp | 2.50 | 2.00 | .473 |
| pre_char_exp | 2.00 | 1.67 | .516 |
| pre_draw_skill | 3.67 | 3.83 | .857 |
| pre_age | 25.17 | 25.50 | .883 |

> n=6/조건에서 80% 검정력(α=.05, 단측)을 가지려면 d ≈ 1.54 이상 필요 (양측 ≈ 1.8; d = 0.8을 검출하려면 조건당 약 21명). p값보다 효과크기·CI 중심으로 해석할 것.
