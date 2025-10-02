# dags/python_time_dag.py
from datetime import datetime, timezone
from airflow import DAG
from airflow.decorators import dag, task

@dag(
    dag_id="python_time_dag",
    description="Obtiene hora UTC y local desde Python",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@hourly",
    catchup=False,
    tags=["demo", "hora"],
)
def _python_time_dag():
    @task
    def get_times():
        now_utc = datetime.now(timezone.utc)
        now_local = datetime.now()
        print(f"[UTC]    {now_utc.isoformat()}")
        print(f"[Local]  {now_local.isoformat()}")
        # Si quieres verlo en XCom desde la UI:
        return {"utc": now_utc.isoformat(), "local": now_local.isoformat()}

    get_times()

_python_time_dag()
