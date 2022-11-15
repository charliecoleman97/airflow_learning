from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta, datetime


default_args = {
    'owner': 'charlie',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}
def get_sklearn():
    import sklearn
    print(f"scikit learn with version: {sklearn.__version__}")

def get_matplotlib():
    import matplotlib
    print(f"matplotlib with version: {matplotlib.__version__}")

with DAG(
    default_args=default_args,
    dag_id='dag_with_python_dependencies_v2',
    start_date=datetime(2022, 11, 11),
    schedule_interval='@daily'
) as dag:

    get_sklearn = PythonOperator(
        task_id='get_sklearn',
        python_callable=get_sklearn
    )

    get_matplotlib = PythonOperator(
        task_id='get_matplotlib',
        python_callable=get_matplotlib
    )

    get_sklearn >> get_matplotlib


