from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
import logging
from airflow.models import Variable


def download_data():
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/14898c328f197effcac3375ce0be7dee83063757/data/2021/2021-06-22/parks.csv"
    data = pd.read_csv(url)
    logging.info(msg=data)
    return data.to_dict()

data = pd.DataFrame(download_data())
Variable.set("data", data.to_json())

def mean_benches():
    data_json = Variable.get("data")
    data = pd.read_json(data_json)
    logging.info(msg=data.groupby('year').agg('mean').park_benches)


def sum_median_square():
    data_json = Variable.get("data")
    data = pd.read_json(data_json)
    logging.info(msg=data.groupby('year').agg('sum').med_park_size_data)

def print_next_execution_date(**kwargs):
    execution_date = kwargs['execution_date']
    next_execution_date = kwargs['next_execution_date']
    logging.info(msg=next_execution_date)


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["jdoe@example.com"],
    "email_on_failure": False,
    "execution_timeout": timedelta(minutes=5)
}

dag = DAG(
    dag_id='data_tasks',
    default_args=default_args,
    start_date=datetime(2023, 1, 15),
    schedule_interval="@daily",
    catchup=False
)
t1 = PythonOperator(
    task_id='download_data',
    python_callable=download_data,
    dag=dag
)
t2 = PythonOperator(
    task_id='mean_benches',
    python_callable=mean_benches,
    dag=dag
)
t3 = PythonOperator(
    task_id='sum_median_square',
    python_callable=sum_median_square,
    dag=dag
)
t4 = PythonOperator(
    task_id='print_next_execution_date',
    python_callable=print_next_execution_date,
    dag=dag
)

t1 >> t2
t2 >> t3
t3 >> t4


