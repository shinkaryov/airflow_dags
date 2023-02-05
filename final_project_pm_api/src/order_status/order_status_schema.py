from pydantic import BaseModel, validator
from engine import conn


class Order(BaseModel):
    order_status_id: str = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
    update_at: str = '2023-02-03 00:00:00.000000'
    sale_id: str = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
    status_name_id: int

    @validator('update_at')
    def check_date_format(cls, v):
        from datetime import datetime
        try:
            datetime.strptime(v, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD HH:MM:SS.mmmmmm")
        return v

    @validator('sale_id')
    def sale_id_must_be_in_table_sale(cls, v):
        result = conn.execute(f"SELECT 1 FROM sale WHERE sale_id = '{v}';")
        if len(result) == 0:
            raise ValueError('sale_id must be in table sale')
        return v

    @validator('status_name_id')
    def status_name_id_must_be_in_table_status_name(cls, v):
        if v <= 0:
            raise ValueError('status_name_id must be positive')
        result = conn.execute(f"SELECT 1 FROM status_name WHERE status_name_id = '{v}';")
        if len(result) == 0:
            raise ValueError('status_name_id must be in table status_name')
        return v
