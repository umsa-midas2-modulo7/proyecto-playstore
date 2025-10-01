# ingest.py  (NO ejecutar nada al importar)
import time, random
from datetime import date
import pandas as pd
from google_play_scraper import Sort, reviews


'''
description: Metodo para obtener reseñas de una app por fecha   
inputs:
    result: lista de reseñas
    app_id: id de la app
    fecha: fecha de la reseña
outputs:
    resenas: lista de reseñas
    token: token de paginacion
'''
def get_reviews_exp(result, app_id, fecha):
    resenas = []
    hoy = date.today()
    token = True
    for r in result:
        review_date = pd.Timestamp(r['at']).normalize()
        comparison_date = fecha if fecha else hoy
        if review_date.date() >= comparison_date:
            r['app_id'] = app_id
            resenas.append(r)
        else:
            token = None
            break
    return resenas, token

'''
description: Metodo para obtener reseñas de una app por fecha
inputs:
    app_id: id de la app
    fecha: fecha de la reseña
outputs:
    all_app_reviews: lista de reseñas
'''
def reviews_por_fecha_exp(app_id, fecha: date = None):
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
            break
        resenas, token = get_reviews_exp(result, app_id, fecha)
        all_app_reviews.extend(resenas)
        if not token:
            break
        time.sleep(random.uniform(5, 10))
    return all_app_reviews
