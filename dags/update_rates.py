from airflow.providers.postgres.hooks.postgres import *
from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import date, datetime
import requests
import pandas as pd

default_args = {
    "owner": "airflow",
    "start_date": datetime(2022, 4, 16),
    "retries": 1
}

dag = DAG("update_rates", schedule_interval="0 */3 * * *",
          default_args=default_args)


def extract(**context):
    extract_date = date.today()
    url = f"https://api.exchangerate.host/timeseries?start_date={extract_date}&end_date={extract_date}?base=USD&symbols=BTC"
    response = requests.get(url)
    data = response.json()
    context["ti"].xcom_push(key="data", value=data)


def transform(**context):
    data = context["ti"].xcom_pull(key="data")
    df = pd.DataFrame(data["rates"]).transpose().reset_index().rename(
        columns={"index": "date", "BTC": "btc"})
    context["ti"].xcom_push(key="df", value=df.to_json())


def load(**context):
    pg_hook = PostgresHook(postgres_conn_id="postgres_default")
    df = pd.read_json(context["ti"].xcom_pull(key="df"))
    engine = pg_hook.get_sqlalchemy_engine()
    df.to_sql("exchangerates", engine, index=False,
              method="multi", if_exists="append")


with dag:
    t1 = PythonOperator(task_id="extract",
                        python_callable=extract, provide_context=True)
    t2 = PythonOperator(task_id="transform",
                        python_callable=transform, provide_context=True)
    t3 = PythonOperator(
        task_id="load", python_callable=load, provide_context=True)

    t1 >> t2 >> t3
