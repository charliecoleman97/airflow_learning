from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'charlie',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args, 
    dag_id="dag_with_cron_expression_v1",
    start_date=datetime(2022, 10, 1), 
    schedule_interval = '0 3 * * 2,5'
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo dag with cron expression"
    )