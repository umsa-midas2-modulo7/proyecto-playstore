# from datetime import datetime
# from airflow.decorators import dag, task

# @dag(
#     dag_id="smoke_test_dag",
#     description="DAG de prueba rápida: imprime 'Hola desde Airflow' cada minuto",
#     start_date=datetime(2024, 1, 1),
#     schedule_interval="* * * * *",  # cada minuto
#     catchup=False,
#     tags=["smoke", "test"],
# )
# def smoke_test_dag():
#     @task
#     def hola_airflow():
#         ahora = datetime.now().isoformat()
#         print(f"Hola desde Airflow 🚀 | Fecha/hora: {ahora}")

#     hola_airflow()

# smoke_test_dag()

