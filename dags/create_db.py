from airflow import DAG
from datetime import datetime
from airflow.operators.postgres_operator import PostgresOperator

"""
DAG for creating the database and the table for loading data.
You should only need to run this once.
"""

default_args = {
    "owner": "airflow",
    "start_date": datetime(2022, 4, 16),
    "retries": 1
}

dag = DAG("create_db", schedule_interval=None,
          default_args=default_args, catchup=False)

with dag:
    t1 = PostgresOperator(task_id="create_table", postgres_conn_id="postgres_default",
                          sql="sql/create_table.sql", autocommit=True)

    t1
