from src.ingest import get_app_reviews, app_ids
from datetime import date

print("holi")

print(app_ids)
la_fecha = date(2025, 9, 29)
df = get_app_reviews(la_fecha)
print(df)
