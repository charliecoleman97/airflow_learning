from airflow.decorators import dag, task
from datetime import timedelta, datetime


default_args = {
    'owner': 'charlie',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(dag_id='dag_with_taskflow_api_v1',
    default_args=default_args, 
    start_date=datetime(2022, 11, 8), 
    schedule_interval='@daily')

def hello_world_etl():
    
    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Jerry',
            'last_name': 'Fridman',
        }

    @task()
    def get_age():
        return 20
    
    @task()
    def greet(first_name, last_name, age):
        print(f"Hello World! My name is {first_name} {last_name} and my age is {age}")

    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'], last_name=name_dict['last_name'], age=age)

greet_dag = hello_world_etl()