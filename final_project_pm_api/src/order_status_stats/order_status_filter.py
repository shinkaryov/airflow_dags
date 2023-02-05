from engine import conn
from sqlalchemy.exc import NoSuchTableError
from fastapi import HTTPException


def get_order_status_stats_by_date(date_from, date_to):

    from datetime import date
    date_from = date_from.strftime("%Y-%m-%d")
    date_to = date_to.strftime("%Y-%m-%d")

    sql = f"SELECT * FROM order_status_stats WHERE dt BETWEEN '{date_from}' AND '{date_to}';"
    try:
        return conn.execute(sql)
    except:
        raise HTTPException(status_code=400, detail="Table order_status_stats does not exist")
