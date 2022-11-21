from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3_key import S3KeySensor

default_args = {
    'owner': 'charlie',
    'retries': 5,
    'retry_delay': timedelta(minutes=10)
}

with DAG(
    default_args=default_args,
    dag_id='dag_with_minio_s3_v4',
    start_date=datetime(2022, 11, 20),
    schedule_interval='@daily'
) as dag:
    task1 = S3KeySensor(
        task_id='sensor_minio_s3',
        bucket_name='airflow',
        bucket_key='data.csv',
        aws_conn_id='mino_conn',
        mode='poke',
        poke_interval=5,
        timeout=300

    )