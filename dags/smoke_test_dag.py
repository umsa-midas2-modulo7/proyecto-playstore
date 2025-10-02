from datetime import datetime
from airflow.decorators import dag, task
from src.common.utilities import hola_airflow

@dag(
    dag_id="smoke_test_dag",
    description="DAG de prueba rápida: imprime 'Hola desde Airflow' cada minuto",
    start_date=datetime(2024, 1, 1),
    schedule_interval="* * * * *",  # cada minuto
    catchup=False,
    tags=["smoke", "test"],
)
def smoke_test_dag():
    @task
    def tarea():
        hola_airflow()
    tarea()

smoke_test_dag()
