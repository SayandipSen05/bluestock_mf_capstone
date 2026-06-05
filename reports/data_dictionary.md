# Mutual Fund Analytics Data Dictionary

## 1. Fund Master Dataset

**Source:** 01_fund_master.csv

| Column             | Data Type | Description                        |
| ------------------ | --------- | ---------------------------------- |
| amfi_code          | INTEGER   | Unique AMFI scheme identifier      |
| fund_house         | TEXT      | Asset Management Company (AMC)     |
| scheme_name        | TEXT      | Name of mutual fund scheme         |
| category           | TEXT      | Mutual fund category               |
| sub_category       | TEXT      | Detailed fund classification       |
| plan               | TEXT      | Direct or Regular plan             |
| launch_date        | DATE      | Scheme launch date                 |
| benchmark          | TEXT      | Benchmark index                    |
| expense_ratio_pct  | REAL      | Annual expense ratio (%)           |
| exit_load_pct      | REAL      | Exit load charged on redemption    |
| min_sip_amount     | REAL      | Minimum SIP investment amount      |
| min_lumpsum_amount | REAL      | Minimum lump-sum investment amount |
| fund_manager       | TEXT      | Fund manager name                  |
| risk_category      | TEXT      | Risk classification                |
| sebi_category_code | TEXT      | SEBI category code                 |

---

## 2. NAV History Dataset

**Source:** nav_history_cleaned.csv

| Column    | Data Type | Description                   |
| --------- | --------- | ----------------------------- |
| amfi_code | INTEGER   | Mutual fund scheme identifier |
| date      | DATE      | NAV reporting date            |
| nav       | REAL      | Net Asset Value per unit      |

---

## 3. Scheme Performance Dataset

**Source:** scheme_performance_cleaned.csv

| Column             | Data Type | Description                            |
| ------------------ | --------- | -------------------------------------- |
| amfi_code          | INTEGER   | Mutual fund scheme identifier          |
| scheme_name        | TEXT      | Name of mutual fund scheme             |
| fund_house         | TEXT      | Asset Management Company               |
| category           | TEXT      | Fund category                          |
| plan               | TEXT      | Direct or Regular plan                 |
| return_1yr_pct     | REAL      | One-year return (%)                    |
| return_3yr_pct     | REAL      | Three-year return (%)                  |
| return_5yr_pct     | REAL      | Five-year return (%)                   |
| benchmark_3yr_pct  | REAL      | Benchmark three-year return (%)        |
| alpha              | REAL      | Risk-adjusted excess return            |
| beta               | REAL      | Volatility relative to benchmark       |
| sharpe_ratio       | REAL      | Risk-adjusted performance metric       |
| sortino_ratio      | REAL      | Downside-risk-adjusted return metric   |
| std_dev_ann_pct    | REAL      | Annualized standard deviation (%)      |
| max_drawdown_pct   | REAL      | Maximum observed loss (%)              |
| aum_crore          | REAL      | Assets Under Management (₹ Crore)      |
| expense_ratio_pct  | REAL      | Expense ratio (%)                      |
| morningstar_rating | INTEGER   | Morningstar rating                     |
| risk_grade         | TEXT      | Risk grade classification              |
| return_anomaly     | BOOLEAN   | Flag indicating abnormal return values |

---

## 4. Investor Transactions Dataset

**Source:** investor_transactions_cleaned.csv

| Column             | Data Type | Description                                  |
| ------------------ | --------- | -------------------------------------------- |
| investor_id        | INTEGER   | Unique investor identifier                   |
| transaction_date   | DATE      | Transaction date                             |
| amfi_code          | INTEGER   | Mutual fund scheme identifier                |
| transaction_type   | TEXT      | SIP, Lumpsum, or Redemption                  |
| amount_inr         | REAL      | Transaction amount in INR                    |
| state              | TEXT      | Investor state                               |
| city               | TEXT      | Investor city                                |
| city_tier          | TEXT      | City classification (Tier 1, Tier 2, Tier 3) |
| age_group          | TEXT      | Investor age category                        |
| gender             | TEXT      | Investor gender                              |
| annual_income_lakh | REAL      | Annual income in lakh rupees                 |
| payment_mode       | TEXT      | Mode of payment                              |
| kyc_status         | TEXT      | KYC verification status                      |

---

## 5. AUM by Fund House Dataset

**Source:** 03_aum_by_fund_house.csv

| Column         | Data Type | Description               |
| -------------- | --------- | ------------------------- |
| date           | DATE      | Reporting date            |
| fund_house     | TEXT      | Asset Management Company  |
| aum_lakh_crore | REAL      | AUM in lakh crore rupees  |
| aum_crore      | REAL      | AUM in crore rupees       |
| num_schemes    | INTEGER   | Number of schemes managed |

---

## Business Definitions

* AMFI Code: Unique identifier assigned to every mutual fund scheme by AMFI.
* NAV: Net Asset Value per mutual fund unit.
* AUM: Assets Under Management.
* SIP: Systematic Investment Plan.
* Expense Ratio: Annual fee charged by the fund.
* Alpha: Excess return generated over benchmark.
* Beta: Measure of volatility compared to benchmark.
* Sharpe Ratio: Risk-adjusted return measure.
* KYC: Know Your Customer verification status.
