"""
Descipcion: Módulo de ingesta de datos de Play Store Reviews
"""

import time
import random
from typing import List, Dict, Any, Tuple
from google_play_scraper import Sort, reviews
import pandas as pd
from datetime import date, datetime

from common.constants import AppConstants

app_ids = AppConstants.APP_IDS


def reviews_por_fecha(app_id, fecha:date = None):

    all_app_reviews = []
    token = None
    # para la fecha de hoy
    hoy = date.today()

    while True:
        result, token = reviews(
            app_id,
            lang='es',
            country='bo',
            sort=Sort.NEWEST,
            count=200,
            continuation_token=token
        )

        if not result:
            break  # No hay más reseñas

        for r in result:
            # Normalizar la fecha de la reseña para comparar solo la parte de la fecha
            review_date = pd.Timestamp(r['at']).normalize()
            # Usar la fecha de hoy si no se proporciona una fecha, de lo contrario usar la fecha proporcionada
            comparison_date = fecha if fecha else hoy

            if review_date.date() >= comparison_date:
                r['app_id'] = app_id
                all_app_reviews.append(r)
            else:
                # Dado que las reseñas están ordenadas por las más recientes, podemos detenernos cuando lleguemos a reseñas más antiguas que la fecha especificada
                token = None  # Detener la paginación
                break

        if not token:
            break

        time.sleep(random.uniform(5, 10))

    return all_app_reviews

def get_app_reviews(fecha:date = None):
    all_reviews = []
    for app in app_ids:
        print(f"recolectando {app} ...")    
    # para las reseñas de hoy solo 'reviews_por_fecha(app)' sin fecha 
        app_reviews = reviews_por_fecha(app, fecha)
        all_reviews.extend(app_reviews)
        print(f"...finalizado de {app}")
    df = pd.DataFrame(all_reviews)
    '''
    df.to_csv(f"../data/restore/{df2['at'].dt.date.max()}_comentarios_app.csv",   index=False, encoding="utf-8-sig")
    print("Total de reseñas guardadas:", len(df))
    '''
    print(f"Total de reseñas descargadas: {len(df)}\nen fecha: {fecha}")
    print(df)

print(app_ids)
la_fecha = date(2025, 9, 29)
get_app_reviews(la_fecha)


if __name__ == "__main__":
    print()
