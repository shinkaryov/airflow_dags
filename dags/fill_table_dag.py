from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime
from helpers.default_args import default_args


with DAG(
    dag_id='fill_order_status_stats_table',
    default_args=default_args,
    start_date=datetime(2022, 8, 24),
    schedule_interval="@once",
    catchup=False
) as dag:
    fill_order_status_stats_table = PostgresOperator(
        task_id="fill_order_status_stats_table",
        postgres_conn_id="postgres_data",
        sql="sql/fill_table.sql"
    )
