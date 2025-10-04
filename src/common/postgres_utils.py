# src/utils/postgres_utils.py
from sqlalchemy import text
from src.etl.database import get_db_session
import json
from datetime import datetime

def save_reviews_to_postgres(reviews_data, batch_size=100):
    """
    Guarda reseñas en la tabla data_lake de PostgreSQL
    
    Args:
        reviews_data: Lista de diccionarios con las reseñas
        batch_size: Tamaño del lote para inserción (evita timeouts)
    
    Returns:
        int: Número de registros insertados
    """
    if not reviews_data:
        print("No hay datos para guardar")
        return 0
    
    total_inserted = 0
    
    try:
        with get_db_session() as session:
            # Procesar en lotes para mejor performance
            for i in range(0, len(reviews_data), batch_size):
                batch = reviews_data[i:i + batch_size]
                
                for review in batch:
                    # Preparar el registro para insertar
                    insert_query = text("""
                        INSERT INTO data_lake (datos) 
                        VALUES (:datos)
                    """)
                    
                    # Convertir a JSON serializable
                    review_json = json.loads(json.dumps(review, default=str))
                    
                    session.execute(
                        insert_query,
                        {"datos": json.dumps(review_json)}
                    )
                
                total_inserted += len(batch)
                print(f"Lote guardado: {len(batch)} registros. Total: {total_inserted}")
            
            print(f"✅ Guardado exitoso: {total_inserted} reseñas en PostgreSQL")
            return total_inserted
            
    except Exception as e:
        print(f"❌ Error guardando en PostgreSQL: {str(e)}")
        raise

def test_connection():
    """Test simple de conexión a la base de datos"""
    try:
        with get_db_session() as session:
            result = session.execute(text("SELECT 1"))
            print("✅ Conexión a PostgreSQL exitosa")
            return True
    except Exception as e:
        print(f"❌ Error de conexión: {str(e)}")
        return False

def get_review_count():
    """Obtiene el número total de reseñas en la base de datos"""
    try:
        with get_db_session() as session:
            result = session.execute(
                text("SELECT COUNT(*) FROM data_lake")
            )
            count = result.scalar()
            print(f"📊 Total de reseñas en BD: {count}")
            return count
    except Exception as e:
        print(f"Error contando reseñas: {str(e)}")
        return 0