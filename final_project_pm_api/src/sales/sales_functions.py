from sales.sales_schema import Sale
from engine import conn


def get_all_sales():
    row = "SELECT * FROM sale;"
    return conn.execute(row)


def get_sale_by_id(sale_id):
    row = f"SELECT * FROM sale WHERE sale_id = '{sale_id}';"
    return conn.execute(row)


def new_sale(sale: Sale):
    sql1 = f"SELECT 1 FROM sale WHERE sale_id = '{sale.sale_id}';"
    if len(conn.execute(sql1)) == 0:
        sql2 = f"INSERT INTO sale VALUES ('{sale.sale_id}', " + \
            f"'{sale.amount}', '{sale.date_sale}', '{sale.product_id}', '{sale.user_id}', '{sale.store_id}');"
        conn.execute_no_result(sql2)
        return get_sale_by_id(sale.sale_id)
    else:
        return 'Creation Error: Such sale already exists'


def update_sale(sale: Sale):
    sql1 = f"SELECT 1 FROM sale WHERE sale_id = '{sale.sale_id}';"
    if len(conn.execute(sql1)) != 0:
        sql2 = f"UPDATE sale SET amount = '{sale.amount}', date_sale = '{sale.date_sale}', " + \
            f"product_id = '{sale.product_id}', user_id = '{sale.user_id}', store_id = '{sale.store_id}' " + \
            f"WHERE sale_id = '{sale.sale_id}';"
        conn.execute_no_result(sql2)
        return get_sale_by_id(sale.sale_id)
    else:
        return 'Update Error: Such sale does not exist'


def delete_sale(sale_id):
    sql1 = f"SELECT * FROM sale WHERE sale_id = '{sale_id}';"
    result = conn.execute(sql1)
    if len(result) != 0:
        sql2 = f"SELECT * FROM order_status WHERE sale_id = '{sale_id}';"
        if len(conn.execute(sql2)) != 0:
            return 'Delete Error: Such sale is in order_status'
        sql3 = f"DELETE FROM sale WHERE sale_id = '{sale_id}';"
        conn.execute_no_result(sql3)
        return "Successfully deleted"
    else:
        return 'Delete Error: Such sale does not exist'

