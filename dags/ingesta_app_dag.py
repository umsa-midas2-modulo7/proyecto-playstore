# dags/ingesta_app_dag.py
from datetime import datetime, date
from airflow.decorators import dag, task

@dag(
    dag_id="ingesta_app_dag",
    description="Prueba: consume reviews_por_fecha_exp e imprime en logs",
    start_date=datetime(2024, 1, 1),
    schedule=None,          # <-- solo se ejecuta cuando tú lo disparas
    catchup=False,
    tags=["playstore", "prueba", "ingesta"],
    default_args={"owner": "airflow"},
    params={
        # valores por defecto; puedes cambiarlos en Trigger DAG -> Configure
        "app_id": "com.bancosol.altoke",
        "fecha": "2025-09-29",  # formato YYYY-MM-DD; o déjalo "" para None
        "max_print": 20,        # para no inundar logs, imprime primeras N reseñas
    },
)
def ingesta_app_dag():
    @task
    def run_and_print(app_id: str, fecha_str: str | None, max_print: int | str = 20):
        from src.etl.ingesta import reviews_por_fecha_exp
        from datetime import date
        max_print = int(max_print) if isinstance(max_print, str) else max_print # convierte a int
        fecha = date.fromisoformat(fecha_str) if fecha_str else None            # obtiene fecha
        data = reviews_por_fecha_exp(app_id=app_id, fecha=fecha)                # consulta elt
        total = len(data)
        print(f"Total reseñas obtenidas: {total}")
        print(f"app_id: {app_id} | fecha: {fecha_str}")

        to_show = data[: max_print] if max_print else data
        for r in to_show:
            at = r.get("at")
            user = r.get("userName")
            score = r.get("score")
            content = (r.get("content") or "")
            print(
                f"Fecha: {at} | Usuario: {user} | "
                f"Puntaje: {score} | Reseña: {content[:100]}..."
            )

        if total > len(to_show):
            print(f"(Mostradas {len(to_show)} de {total} reseñas)")

        # Devuelve metadatos por si quieres verlos en XCom
        return {"count": total, "app_id": app_id, "fecha": fecha_str}

    # Lee parámetros desde la UI / CLI al disparar
    run_and_print(
        app_id="{{ params.app_id }}",
        fecha_str="{{ params.fecha }}",
        max_print="{{ params.max_print }}",
    )

ingesta_app_dag()
