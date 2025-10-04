from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Funciones para las tareas
def extraer():
    print("📥 Extrayendo datos...")

def transformar():
    print("🔄 Transformando datos...")

def cargar():
    print("💾 Cargando datos a la base de datos...")

# Definir el DAG
with DAG(
    dag_id="tutorial_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",  # se ejecuta todos los días
    catchup=False,
    tags=["ejemplo", "pipeline"],
) as dag:

    t1 = PythonOperator(
        task_id="extraer_datos",
        python_callable=extraer,
    )

    t2 = PythonOperator(
        task_id="transformar_datos",
        python_callable=transformar,
    )

    t3 = PythonOperator(
        task_id="cargar_datos",
        python_callable=cargar,
    )

    # Definir el orden de las tareas
    t1 >> t2 >> t3
