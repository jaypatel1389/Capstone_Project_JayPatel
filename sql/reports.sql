Part 1 — SQL Relational Layer & Reporting
Task 3 — Reports (sql/reports.sql) 

-- sql/reports.sql
-- Run after schema.sql and seed_data.sql. Output comments were verified against the supplied CSVs.

-- (a) Order totals; NULL discount is treated as 0%.
-- Output:
-- total_orders | total_revenue | avg_order_value
-- 180 | 99860.20 | 554.78
SELECT COUNT(*) AS total_orders,
ROUND(SUM(o.quantity * p.price * (1 - COALESCE(o.discount_pct, 0) / 100.0)), 2) AS total_revenue,
ROUND(AVG(o.quantity * p.price * (1 - COALESCE(o.discount_pct, 0) / 100.0)), 2) AS avg_order_value
FROM orders o JOIN products p ON o.product_id = p.product_id;

-- (b) COUNT(*) versus COUNT(rating); COUNT(column) ignores NULL.
-- Output:
-- total_rows | rated_orders | unrated_orders
-- 180 | 165 | 15
SELECT COUNT(*) AS total_rows, COUNT(rating) AS rated_orders,
COUNT(*) - COUNT(rating) AS unrated_orders FROM orders;

-- (c1) LEFT JOIN: customers with zero orders.
-- Output:
-- customer_id | name
-- C045 | Vihaan
SELECT c.customer_id, c.name FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name HAVING COUNT(o.order_id) = 0;

-- (c2) Independent NOT IN check.
-- Output:
-- customer_id | name
-- C045 | Vihaan
SELECT customer_id, name FROM customers
WHERE customer_id NOT IN (SELECT DISTINCT customer_id FROM orders);

-- (d) Return rates by city; filter to rates above 20%.
-- Output:
-- city | total_orders | returned_orders | return_rate_pct
-- Jaipur | 19 | 8 | 42.10
-- Lucknow | 49 | 15 | 30.60
-- Bangalore | 33 | 8 | 24.20
SELECT c.city, COUNT(o.order_id) AS total_orders, SUM(o.returned) AS returned_orders,
ROUND(100.0 * SUM(o.returned) / COUNT(o.order_id), 1) AS return_rate_pct
FROM orders o JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.city
HAVING ROUND(100.0 * SUM(o.returned) / COUNT(o.order_id), 1) > 20
ORDER BY return_rate_pct DESC;

-- (e1) Top five customers by spend.
-- Tie-break: customer_id ASC makes the ranking deterministic when spend values tie.
-- Output:
-- customer_id | name | total_spend
-- C043 | Reyansh | 12920.00
-- C026 | Isha | 8371.60
-- C008 | Meera | 4564.60
-- C011 | Arjun | 4111.00
-- C042 | Sanya | 3785.00
SELECT c.customer_id, c.name,
ROUND(SUM(o.quantity * p.price * (1 - COALESCE(o.discount_pct, 0) / 100.0)), 2) AS total_spend
FROM orders o JOIN products p ON o.product_id = p.product_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spend DESC, c.customer_id ASC LIMIT 5;

-- (e2) Ranks 3-5; OFFSET 2 skips the first two rows from the same ordering.
-- Output:
-- customer_id | name | total_spend
-- C008 | Meera | 4564.60
-- C011 | Arjun | 4111.00
-- C042 | Sanya | 3785.00
SELECT c.customer_id, c.name,
ROUND(SUM(o.quantity * p.price * (1 - COALESCE(o.discount_pct, 0) / 100.0)), 2) AS total_spend
FROM orders o JOIN products p ON o.product_id = p.product_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spend DESC, c.customer_id ASC LIMIT 3 OFFSET 2;

-- (f) Three-table JOIN grouped by category.
-- Output:
-- category | order_count | category_revenue
-- Haircare | 54 | 44956.10
-- Skincare | 60 | 27346.00
-- Babycare | 30 | 16805.00
-- PersonalCare | 36 | 10753.10
SELECT p.category, COUNT(o.order_id) AS order_count,
ROUND(SUM(o.quantity * p.price * (1 - COALESCE(o.discount_pct, 0) / 100.0)), 2) AS category_revenue
FROM orders o JOIN products p ON o.product_id = p.product_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY p.category ORDER BY category_revenue DESC;

-- (g) Customers whose names start with A; expected 10 rows.
-- Output:
-- customer_id | name
-- C001 | Aarav
-- C003 | Aditi
-- C004 | Ananya
-- C011 | Arjun
-- C021 | Aryan
-- C030 | Anika
-- C031 | Aditya
-- C036 | Aisha
-- C041 | Ayaan
-- C044 | Aria
SELECT customer_id, name FROM customers WHERE name LIKE 'A%' ORDER BY customer_id;

-- (h) Distinct acquisition sources.
-- Output:
-- acquisition_source
-- Ad
-- Organic
-- Referral
-- Social
SELECT DISTINCT acquisition_source FROM customers ORDER BY acquisition_source;

-- (i) Add loyalty_tier and populate every customer. Run once on a fresh schema.
ALTER TABLE customers ADD COLUMN loyalty_tier VARCHAR(10);
UPDATE customers SET loyalty_tier = CASE
WHEN city_tier = 1 THEN 'Gold' ELSE 'Silver' END;

-- Verification after (i):
-- Output:
-- loyalty_tier | customer_count
-- Gold | 28
-- Silver | 17
SELECT loyalty_tier, COUNT(*) AS customer_count FROM customers
GROUP BY loyalty_tier ORDER BY loyalty_tier;
