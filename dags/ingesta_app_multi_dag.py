# dags/ingesta_app_multi_dag.py
from datetime import datetime, date
from airflow.decorators import dag, task

@dag(
    dag_id="ingesta_app_multi_dag",
    description="Prueba: obtiene reseñas de varias apps y las imprime (sin guardar archivos)",
    start_date=datetime(2024, 1, 1),
    schedule=None,      # solo manual
    catchup=False,
    tags=["playstore", "prueba", "multi"],
    params={
        # opcional: puedes pasar app_ids como string separado por comas para ignorar los DEFAULT_APP_IDS:
        # "app_ids_csv": "com.foo.app,com.bar.app",
        "fecha": "2025-09-29",
        "max_print": 20,
    },
)
def ingesta_app_multi_dag():
    @task
    def run_and_print(fecha_str: str | None, max_print: int | str = 20, app_ids_csv: str | None = None):
        from src.etl.ingesta import get_app_reviews  # import absoluto desde tu código

        # parseo de params
        max_print = int(max_print) if isinstance(max_print, str) else max_print
        fecha = date.fromisoformat(fecha_str) if fecha_str else None
        data = get_app_reviews(fecha=fecha)
        total = len(data)
        print(f"Total reseñas obtenidas: {total}")

        # imprime hasta max_print
        for r in data[:max_print]:
            at = r.get("at")
            user = r.get("userName")
            score = r.get("score")
            content = (r.get("content") or "")
            app = r.get("app_id")
            print(
                f"[{app}] Fecha: {at} | Usuario: {user} | "
                f"Puntaje: {score} | Reseña: {content[:100]}..."
            )
        if total > max_print:
            print(f"(Mostradas {max_print} de {total} reseñas)")

        # devolver metadatos por si quieres revisar en XCom
        return {"count": total, "fecha": fecha_str}

    run_and_print(
        fecha_str="{{ params.fecha }}",
        max_print="{{ params.max_print }}",
        # app_ids_csv="{{ params.app_ids_csv }}"  # descomenta si quieres pasar por UI
    )

ingesta_app_multi_dag()
