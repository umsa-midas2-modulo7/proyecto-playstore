"""
Descipcion: Módulo de ingesta de datos de Play Store Reviews
"""

import time
import random
from typing import List, Dict, Any, Tuple
from google_play_scraper import Sort, reviews
import pandas as pd

from common.constants import AppConstants



def reviews_por_fecha(app_id, date=None):
    
    all_app_reviews = []
    token = None
    # para la fecha de hoy 
    hoy = pd.to_datetime('today').normalize()

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
            comparison_date = date.normalize() if date else hoy

            if review_date >= comparison_date:
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


if __name__ == "__main__":
    df = main()