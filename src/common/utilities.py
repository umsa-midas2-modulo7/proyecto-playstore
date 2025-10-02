# src/common/utilities.py
from datetime import datetime

def hola_airflow():
    ahora = datetime.now().isoformat()
    print(f"Hola desde Airflow 🚀 | Fecha/hora: {ahora}")