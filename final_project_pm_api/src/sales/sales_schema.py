from pydantic import BaseModel, validator
from engine import conn


class Sale(BaseModel):
    sale_id: str = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
    amount: float
    date_sale: str = '2023-02-03'
    product_id: int
    user_id: int
    store_id: int

    @validator('amount')
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('amount must be positive')
        return v

    @validator('date_sale')
    def check_date_format(cls, v):
        from datetime import datetime
        try:
            datetime.strptime(v, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return v

    @validator('product_id')
    def product_id_must_be_in_table_product(cls, v):
        if v <= 0:
            raise ValueError('product_id must be positive')
        result = conn.execute(f"SELECT 1 FROM product WHERE product_id = '{v}';")
        if len(result) == 0:
            raise ValueError('product_id must be in table product')
        return v

    @validator('user_id')
    def user_id_must_be_in_table_user(cls, v):
        if v <= 0:
            raise ValueError('user_id must be positive')
        result = conn.execute(f"SELECT 1 FROM users WHERE user_id = '{v}';")
        if len(result) == 0:
            raise ValueError('user_id must be in table product')
        return v

    @validator('store_id')
    def store_id_must_be_in_table_store(cls, v):
        if v <= 0:
            raise ValueError('store_id must be positive')
        result = conn.execute(f"SELECT 1 FROM store WHERE store_id = '{v}';")
        if len(result) == 0:
            raise ValueError('store_id must be in table product')
        return v


