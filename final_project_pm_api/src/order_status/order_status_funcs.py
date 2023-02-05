from order_status.order_status_schema import Order
from engine import conn


def get_all_orders():
    row = "SELECT * FROM order_status;"
    return conn.execute(row)


def get_order_by_id(order_status_id):
    row = f"SELECT * FROM order_status WHERE order_status_id = '{order_status_id}';"
    return conn.execute(row)


def new_order(order: Order):
    sql1 = f"SELECT 1 FROM order_status WHERE order_status_id = '{order.order_status_id}';"
    if len(conn.execute(sql1)) == 0:
        sql2 = f"INSERT INTO order_status VALUES ('{order.order_status_id}', " + \
            f"'{order.update_at}', '{order.sale_id}', '{order.status_name_id}');"
        conn.execute_no_result(sql2)
        return get_order_by_id(order.order_status_id)
    else:
        return 'Creation Error: Such order already exists'


def update_order(order: Order):
    sql1 = f"SELECT 1 FROM order_status WHERE order_status_id = '{order.order_status_id}';"
    if len(conn.execute(sql1)) != 0:
        sql2 = f"UPDATE order_status SET update_at = '{order.update_at}', sale_id = '{order.sale_id}', " + \
            f"status_name_id = '{order.status_name_id}' WHERE order_status_id = '{order.order_status_id}';"
        conn.execute_no_result(sql2)
        return get_order_by_id(order.order_status_id)
    else:
        return 'Update Error: Such order does not exist'


def delete_order(order_status_id):
    sql1 = f"SELECT * FROM order_status WHERE order_status_id = '{order_status_id}';"
    result = conn.execute(sql1)
    if len(result) != 0:
        sql2 = f"DELETE FROM order_status WHERE order_status_id = '{order_status_id}';"
        conn.execute_no_result(sql2)
        return "Successfully deleted"
    else:
        return 'Delete Error: Such order does not exist'

