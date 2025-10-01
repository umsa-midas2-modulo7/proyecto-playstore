from datetime import date
from ..etl.ingest_exp import reviews_por_fecha_exp

data = reviews_por_fecha_exp(app_id="com.bancosol.altoke", fecha=date(2025, 9, 29))
print(len(data))

for r in data:
    print(
        f"Fecha: {r['at']} | Usuario: {r.get('userName')} | "
        f"Puntaje: {r.get('score')} | Reseña: {r.get('content')[:100]}..."
    )