# Dataset Card: Territorial Risk Synthetic Dataset

## Dataset Details

### Dataset Description
The **Territorial Risk Synthetic Dataset** is a structured, synthetic benchmark designed for binary classification tasks, vulnerability analysis, spatial-temporal risk assessment, and algorithmic fairness evaluations in social or territorial intervention domains.

- **Curated / Created by:** Synthetic Generation Framework
- **Language(s):** English (column headers), Spanish (categorical labels for zones)
- **License:** MIT License
- **Format:** CSV (`territorial_risk_synthetic.csv`)

### Dataset Structure
- **Total Records:** 640
- **Total Columns:** 9
- **Missing Values:** None (0%)

## Attributes & Data Dictionary

| Column Name | Data Type | Description | Range / Values |
| :--- | :--- | :--- | :--- |
| `case_id` | String | Unique identifier for each evaluated case | `CASE-0001` to `CASE-0640` |
| `received_date` | Date (YYYY-MM-DD) | Registration timestamp of the incident report | 2026-01-01 to 2026-12-27 |
| `zone` | Categorical | Geographic or administrative region of the incident | `Sur`, `Este`, `Oeste`, `Norte` |
| `protected_group` | Categorical | Demographically protected class indicator | `G1` (61.9%), `G2` (38.1%) |
| `age_band` | Categorical | Age bracket of the primary subject | `18-29`, `30-44`, `45-59`, `60+` |
| `previous_incidents` | Integer | Count of prior recorded incidents in the area/subject | 0 to 9 (Mean: 3.28) |
| `infrastructure_score` | Float | Normalized quality score of local infrastructure | 0.0316 to 0.9835 (Mean: 0.519) |
| `exposure` | Float | Normalized index measuring environmental/social risk exposure | 0.0000 to 1.0000 (Mean: 0.503) |
| `target` | Binary Integer | Ground truth label indicating risk outcome (1 = High Risk / Intervention Required, 0 = Low Risk) | `0` (44.84%), `1` (55.16%) |

## Statistical Summary

### Numerical Features

| Feature | Mean | Std Dev | Min | Median (50%) | Max |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `previous_incidents` | 3.28 | 1.65 | 0.0 | 3.0 | 9.0 |
| `infrastructure_score` | 0.519 | 0.182 | 0.0316 | 0.5136 | 0.9835 |
| `exposure` | 0.503 | 0.193 | 0.0000 | 0.5130 | 1.0000 |

### Categorical Distributions

- **Zone:** `Sur` (25.63%), `Este` (25.63%), `Oeste` (24.53%), `Norte` (24.22%)
- **Protected Group:** `G1` (396 samples), `G2` (244 samples)
- **Age Band:** `60+` (27.97%), `30-44` (25.47%), `45-59` (23.44%), `18-29` (23.13%)

## Uses & Applications

### Direct Use Cases
1. **Supervised Machine Learning:** Training tabular binary classification models (e.g., Logistic Regression, Random Forests, XGBoost, LightGBM).
2. **Fairness & Ethical AI Auditing:** Evaluating disparate impact or equalized odds across demographic variables (`protected_group` and `age_band`).
3. **Feature Importance & Interpretability:** Assessing feature contributions (SHAP/LIME values) of infrastructure and historical incidents towards risk outcomes.

### Out-of-Scope Use
- Not suitable for real-world deployment or operational decision-making as the data is synthetic.

## Bias, Risks, and Limitations

- **Synthetic Artifacts:** Relationships between features are artificially generated and may not fully mirror complex real-world social dynamics.
- **Demographic Disparities:** Target positive rates vary across demographic segments (e.g., `G2` exhibits a ~63.9% positive target rate vs. ~49.7% in `G1`), making it an ideal candidate for algorithmic bias testing.

## Getting Started

```python
import pandas as pd

# Load dataset
df = pd.read_csv("territorial_risk_synthetic.csv", parse_dates=["received_date"])

# Display basic information
print(df.info())
print(df.head())