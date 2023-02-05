-- fill order_status_stats table
INSERT INTO order_status_stats
SELECT DATE(sale.date_sale) as dt_sale, status_name.status_name, COUNT(order_status)
    FROM sale
INNER JOIN
		order_status ON
		sale.sale_id=order_status.sale_id
INNER JOIN
		status_name ON
		order_status.status_name_id=status_name.status_name_id
GROUP BY  dt_sale, status_name.status_name;