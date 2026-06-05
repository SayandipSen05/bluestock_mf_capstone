-- Top 5 fund houses by AUM
SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV per month
SELECT
strftime('%Y-%m', date) AS month,
AVG(nav)
FROM fact_nav
GROUP BY month;

-- SIP YoY Growth
SELECT
strftime('%Y', transaction_date) AS year,
SUM(amount_inr)
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY year;

-- Transactions by state
SELECT
state,
COUNT(*)
FROM fact_transactions
GROUP BY state
ORDER BY COUNT(*) DESC;

-- Funds with expense ratio below 1%
SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Top 5 funds by 5Y return
SELECT
scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- Average expense ratio by category
SELECT
category,
AVG(expense_ratio_pct)
FROM dim_fund
GROUP BY category;

-- Count investors by KYC status
SELECT
kyc_status,
COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;

-- Transactions by payment mode
SELECT
payment_mode,
COUNT(*)
FROM fact_transactions
GROUP BY payment_mode;

-- Average transaction amount by city tier
SELECT
city_tier,
AVG(amount_inr)
FROM fact_transactions
GROUP BY city_tier;