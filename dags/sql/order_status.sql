-- create order_status_stats table
CREATE TABLE IF NOT EXISTS order_status_stats(
    dt DATE,
    order_status_name VARCHAR(100),
    orders_count INT);