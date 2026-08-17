-- E-Commerce Sales & Customer Analytics
-- Table assumed: ecommerce_sales

-- 1. Overall KPIs
SELECT
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit,
    COUNT(DISTINCT Order_ID) AS total_orders,
    COUNT(DISTINCT Customer_ID) AS total_customers,
    AVG(Sales) AS average_order_value
FROM ecommerce_sales;

-- 2. Monthly sales
SELECT
    EXTRACT(YEAR FROM Order_Date) AS year,
    EXTRACT(MONTH FROM Order_Date) AS month,
    SUM(Sales) AS monthly_sales
FROM ecommerce_sales
GROUP BY EXTRACT(YEAR FROM Order_Date), EXTRACT(MONTH FROM Order_Date)
ORDER BY year, month;

-- 3. Category performance
SELECT Category, SUM(Sales) AS sales, SUM(Profit) AS profit
FROM ecommerce_sales
GROUP BY Category
ORDER BY sales DESC;

-- 4. Top 10 products
SELECT Product, SUM(Sales) AS sales
FROM ecommerce_sales
GROUP BY Product
ORDER BY sales DESC
LIMIT 10;

-- 5. Regional performance
SELECT Region, SUM(Sales) AS sales, SUM(Profit) AS profit
FROM ecommerce_sales
GROUP BY Region
ORDER BY sales DESC;

-- 6. Payment method analysis
SELECT Payment_Method, COUNT(*) AS orders, SUM(Sales) AS sales
FROM ecommerce_sales
GROUP BY Payment_Method
ORDER BY sales DESC;

-- 7. Return/cancellation rates
SELECT
    Order_Status,
    COUNT(*) AS orders,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM ecommerce_sales), 2) AS percentage
FROM ecommerce_sales
GROUP BY Order_Status;
