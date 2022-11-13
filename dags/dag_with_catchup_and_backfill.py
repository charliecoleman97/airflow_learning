from datetime import datetime, timedelta
from airflow import DAG 
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'charlie',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='dag_with_catchup_and_backfill_v1',
    default_args = default_args,
    description='This is the first dag',
    start_date=datetime(2022, 11, 7),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo this is a simple bash command"
    )