# dags/fecha_hora_dag.py
from datetime import datetime
from airflow.decorators import dag, task

@dag(
    dag_id="fecha_hora_dag",
    description="Obtiene la fecha/hora en la primera tarea y la imprime en la segunda",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,   # <-- SIN schedule, solo manual
    catchup=False,
)
def fecha_hora_dag():
    @task
    def obtener_fecha():
        ahora = datetime.now().isoformat()
        return ahora

    @task
    def imprimir_fecha(fecha):
        print(f"La fecha/hora recibida es: {fecha}")

    # Workflow: primero obtener -> luego imprimir
    imprimir_fecha(obtener_fecha())

fecha_hora_dag()
