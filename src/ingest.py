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

# Función para obtener reseñas desde una fecha específica o la fecha de hoy por defecto, sin captura de errores


def get_reviews(result, app_id, fecha):
    resenas = []
    hoy = date.today()  # para la fecha de hoy
    token = True  # Inicializar como True para indicar que seguimos

    for r in result:
        review_date = pd.Timestamp(r['at']).normalize()
        comparison_date = fecha if fecha else hoy

        if review_date.date() >= comparison_date:
            r['app_id'] = app_id
            resenas.append(r)
        else:
            token = None  # Detener la paginación si la reseña es más antigua
            break

    return resenas, token


def reviews_por_fecha(app_id, fecha: date = None):

    all_app_reviews = []
    token = None

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

        resenas, token = get_reviews(result, app_id, fecha)
        all_app_reviews.extend(resenas)

        if not token:
            break

        time.sleep(random.uniform(5, 10))

    return all_app_reviews


def get_app_reviews(fecha: date = None):
    all_reviews = []
    for app in app_ids:
        print(f"recolectando {app} ...")
    # para las reseñas de hoy solo 'reviews_por_fecha(app)' sin fecha
        app_reviews = reviews_por_fecha(app, fecha)
        all_reviews.extend(app_reviews)
        print(f"...finalizado de {app}")
    df = pd.DataFrame(all_reviews)

    print(f"Total de reseñas descargadas: {len(df)}\nen fecha: {fecha}")
    return df


def save_to_csv(df):
    df.to_csv(f"../data/restore/{df['at'].dt.date.max()}_comentarios_app.csv",
              index=False, encoding="utf-8-sig")
    print("Total de reseñas guardadas:", len(df))
