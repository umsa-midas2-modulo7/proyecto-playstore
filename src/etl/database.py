# src/etl/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import os

class PostgreSQLConnection:
    def __init__(self):
        self.host = "10.0.2.236"
        self.port = "5432"
        self.database = "victor"
        self.username = "victor"
        self.password = "victor"
        self.schema = "apache_airflow_dl"
    
    def get_connection_string(self):
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
    
    def get_engine(self):
        connection_string = self.get_connection_string()
        engine = create_engine(
            connection_string,
            connect_args={'options': f'-c search_path={self.schema}'},
            pool_pre_ping=True,
            echo=False  # Cambia a True para debug
        )
        return engine

# Instancia global
postgres_conn = PostgreSQLConnection()

@contextmanager
def get_db_session():
    """Context manager para manejar sesiones de base de datos"""
    engine = postgres_conn.get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()