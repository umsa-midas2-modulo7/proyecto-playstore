# dags/bash_date_dag.py
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="bash_date_dag",
    description="Imprime la hora del sistema con `date`",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@hourly",  # cada hora
    catchup=False,
    tags=["demo", "hora"],
) as dag:
    print_date = BashOperator(
        task_id="print_date",
        bash_command="echo 'Hora del contenedor:' && date -u && echo '(UTC)'",
    )
