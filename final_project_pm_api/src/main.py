from fastapi import FastAPI
import logging
from sales.sales_functions import *
from order_status.order_status_schema import Order
from order_status.order_status_funcs import *
from order_status_stats.order_status_filter import *
from sales.sales_schema import Sale
from datetime import date
from engine import conn, eng

LOGGER = logging.getLogger(__name__)

app = FastAPI()


# ------------------------------------- SALE -------------------------------------

@app.get("/sales", tags=["Sale Methods"], description="Get all sales")
async def get_sales():
    return get_all_sales()


@app.get("/sales/{sale_id}", tags=["Sale Methods"], description="Get sale by id")
def get_sale(sale_id: str):
    return get_sale_by_id(sale_id)


@app.post("/sales/{sale_id}", tags=["Sale Methods"], description="Create new sale")
def post_sale(sale: Sale):
    return new_sale(sale)


@app.put("/sales/{sale_id}", tags=["Sale Methods"], description="Update sale")
def put_sale(sale: Sale):
    return update_sale(sale)


@app.delete("/sales/{sale_id}", tags=["Sale Methods"],
            description="Delete sale by sale, if sale is not in order_status")
def delete_sale_by_id(sale_id: str):
    return delete_sale(sale_id)

# ------------------------------------- SALE -------------------------------------


# ------------------------------------- ORDER STATUS -----------------------------

@app.get("/order_status", tags=["Order Status Methods"], description="Get all order status")
def get_orders():
    return get_all_orders()


@app.get("/order_status/{order_status_id}", tags=["Order Status Methods"], description="Get order status by id")
def get_order(order_status_id: str):
    return get_order_by_id(order_status_id)


@app.post("/order_status/{order_status_id}", tags=["Order Status Methods"], description="Create new order status")
def post_order(order: Order):
    return new_order(order)


@app.put("/order_status/{order_status_id}", tags=["Order Status Methods"], description="Update order status")
def put_order(order: Order):
    return update_order(order)


@app.delete("/order_status/{order_status_id}", tags=["Order Status Methods"],
            description="Delete order status by order_status_id")
def delete_order_by_id(order_status_id: str):
    return delete_order(order_status_id)

# ------------------------------------- ORDER STATUS -----------------------------

# ------------------------------------- ORDER STATUS STATS -----------------------

@app.get("/filter", tags=["Order Status Filter"], description="Get order status stats with dt filter")
def get_order_status_stats(date_from: date = '1970-01-01', date_to: date = '2025-01-01'):
    return get_order_status_stats_by_date(date_from, date_to)

# ------------------------------------- ORDER STATUS STATS -----------------------


# ------------------------------------- SHUTDOWN EVENTS --------------------------
@app.on_event("shutdown")
def shutdown_event():
    LOGGER.info("Shutting down...")
    conn.close()
    eng.dispose()
# ------------------------------------- SHUTDOWN EVENTS --------------------------

