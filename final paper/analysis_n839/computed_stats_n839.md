# Statistical Analysis - Filtered Dataset (N=839)

**Data Source:** `reddit_data_2021_filtered.csv`
**Total Records:** N=839
**Date Range:** January 1, 2021 - December 31, 2021

---

## 1. Data Overview

- **Blue Collar:** n=363 (43.3%)
- **White Collar:** n=476 (56.7%)

- **Posts:** n=153 (18.2%)
- **Comments:** n=686 (81.8%)

## 2. Sentiment by Category

| Category | N | Mean | Std Dev | 95% CI Lower | 95% CI Upper |
|----------|---|------|---------|--------------|---------------|
| blue_collar | 363 | -0.0055 | 0.8981 | -0.0982 | 0.0872 |
| white_collar | 476 | -0.2374 | 0.7542 | -0.3053 | -0.1695 |

## 3. T-Test (Blue vs White Collar)

- **T-statistic:** 3.9669
- **P-value:** 8.0292e-05
- **Result:** Significant (α = 0.05)

## 4. Chi-Square (Category vs Sentiment Label)

**Contingency Table:**
| category     |   negative |   neutral |   positive |
|:-------------|-----------:|----------:|-----------:|
| blue_collar  |        147 |        71 |        145 |
| white_collar |        205 |       179 |         92 |

- **χ² Statistic:** 53.8222
- **P-value:** 2.0543e-12
- **Result:** Significant

## 5. Correlation (Karma vs Sentiment)

| Method | r | P-value |
|--------|---|----------|
| Pearson | 0.0234 | 4.9861e-01 |
| Spearman | 0.0949 | 5.9479e-03 |

## 6. Subreddit-Level Statistics

| Category | Subreddit | N | Mean | Std Dev | 95% CI Lower | 95% CI Upper |
|----------|-----------|---|------|---------|--------------|---------------|
| blue_collar | KitchenConfidential | 190 | 0.1632 | 0.9083 | 0.0332 | 0.2931 |
| blue_collar | Firefighting | 62 | -0.0806 | 0.8926 | -0.3073 | 0.1460 |
| blue_collar | ProtectAndServe | 42 | -0.1667 | 0.8239 | -0.4234 | 0.0901 |
| blue_collar | Machinists | 38 | -0.5526 | 0.6857 | -0.7780 | -0.3273 |
| blue_collar | Construction | 11 | 0.1818 | 0.9816 | -0.4777 | 0.8413 |
| blue_collar | electricians | 10 | -0.1000 | 0.8756 | -0.7264 | 0.5264 |
| blue_collar | Plumbing | 6 | 0.0000 | 0.8944 | -0.9386 | 0.9386 |
| blue_collar | Truckers | 2 | -0.5000 | 0.7071 | -6.8531 | 5.8531 |
| blue_collar | Carpentry | 1 | 1.0000 | nan | nan | nan |
| blue_collar | Welding | 1 | -1.0000 | nan | nan | nan |
| white_collar | law | 199 | -0.3065 | 0.7258 | -0.4080 | -0.2051 |
| white_collar | Accounting | 146 | -0.2740 | 0.8181 | -0.4078 | -0.1402 |
| white_collar | consulting | 71 | -0.1268 | 0.6531 | -0.2814 | 0.0278 |
| white_collar | cscareerquestions | 58 | -0.0517 | 0.7819 | -0.2573 | 0.1539 |
| white_collar | engineering | 2 | 0.0000 | 0.0000 | nan | nan |
