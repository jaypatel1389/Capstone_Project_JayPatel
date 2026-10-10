Part 1 — SQL Relational Layer & Reporting

### Task 2 — Load seed data (sql/seed_data.sql) ###

SELECT 'customers' AS table_name, COUNT(*) AS total
FROM customers
UNION ALL
SELECT 'products', COUNT(*) FROM products
UNION ALL
SELECT 'orders', COUNT(*) FROM orders;
