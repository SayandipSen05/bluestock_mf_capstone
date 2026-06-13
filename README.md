# Mutual Fund Analytics Platform

## Overview

The Mutual Fund Analytics Platform is an end-to-end Data Engineering, Financial Analytics, and Business Intelligence project developed to analyze mutual fund performance, investor behavior, SIP trends, portfolio risk, and industry growth.

The project uses Python, Pandas, SQLite, SQL, and Power BI to build a complete analytics workflow from raw data ingestion to dashboard visualization.

---

# Project Objectives

- Build a complete ETL pipeline
- Perform Exploratory Data Analysis (EDA)
- Compute financial performance metrics
- Analyze investor behavior
- Develop advanced risk analytics
- Create interactive Power BI dashboards

---

# Technology Stack

- Python
- Pandas
- NumPy
- SQLite
- SQL
- Matplotlib
- Seaborn
- Plotly
- Power BI

---

# Project Structure

```text
bluestock_mf_capstone/

│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── data_ingestion.ipynb
│   ├── data_cleaning.ipynb
│   ├── eda_analysis.ipynb
│   ├── performance_analytics.ipynb
│   └── advanced_analytics.ipynb
│
├── reports/
│   ├── alpha_beta.csv
│   ├── fund_scorecard.csv
│   ├── sector_hhi.csv
│   ├── sip_continuity.csv
│   └── var_cvar.csv
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── README.md
├── run_pipeline.py
└── requirements.txt
```

---

# Datasets

## Fund Master

Contains metadata about mutual fund schemes.

Key Columns:

- amfi_code
- scheme_name
- fund_house
- category
- benchmark
- expense_ratio_pct

---

## NAV History

Contains daily NAV values for mutual fund schemes.

Key Columns:

- amfi_code
- date
- nav

---

## Scheme Performance

Contains return and risk metrics.

Key Columns:

- return_1yr_pct
- return_3yr_pct
- sharpe_ratio
- alpha
- beta
- max_drawdown_pct

---

## Investor Transactions

Contains investor transaction records.

Key Columns:

- investor_id
- transaction_date
- transaction_type
- amount_inr
- state
- age_group

---

## Benchmark Indices

Contains benchmark market index values.

Key Columns:

- date
- index_name
- close_value

---

# ETL Pipeline

## Extract

Read raw CSV datasets using Pandas.

## Transform

- Handle missing values
- Remove duplicates
- Convert data types
- Standardize dates
- Create analytical features

## Load

- Save cleaned CSV files
- Load data into SQLite database

---

# Performance Analytics

Implemented metrics:

- Daily Returns
- CAGR
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
- Historical VaR
- CVaR

---

# Advanced Analytics

Implemented analyses:

- Rolling Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Fund Recommendation Engine
- Sector Concentration (HHI)

---

# Dashboard Pages

## Page 1 – Industry Overview

- Total AUM
- SIP Inflows
- Folios
- Industry AUM Trend
- AUM by AMC

## Page 2 – Fund Performance

- Return vs Risk
- NAV vs Benchmark
- Fund Scorecard

## Page 3 – Investor Analytics

- State-wise Investment
- Transaction Split
- Age Group Analysis

## Page 4 – SIP & Market Trends

- SIP vs Nifty
- Category Heatmap
- Top Categories by Inflow

---

# Installation

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run Complete Pipeline

```bash
python run_pipeline.py
```

---

# Power BI Dashboard

Open:

```text
bluestock_mf_dashboard.pbix
```

using Power BI Desktop.

Refresh data if required.

---

# Deliverables

- SQLite Database
- Cleaned CSV Files
- Analytical Reports
- Power BI Dashboard
- Final PDF Report
- Presentation Slides

---

# Author

Sayandip Sen
