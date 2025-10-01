# Proyecto: PlayStore

Este repositorio implementa un pipeline de adquisición, limpieza y almacenamiento de datos de reseñas de Google Play, siguiendo los objetivos de la tarea.

### Modulo 7
### Proyecto PlayStore

# Integrantes

- Noemi
- Marco
- Victor

## 📂 Estructura del proyecto

```bash
proyecto-playstore/
├── data/
│   ├── raw/              # datos crudos desde Google Play y CSV externos
│   ├── clean/            # datos después de limpieza
│   ├── processed/        # datos transformados/listos para análisis
│   └── external/         # segunda fuente de datos (CSV, etc.)
│
├── notebooks/
│   ├── 01_ingesta.ipynb          # ingesta de datos
│   ├── 02_limpieza.ipynb         # limpieza de datos
│   ├── 03_validacion.ipynb       # validaciones de calidad de datos (great_expectations)
│   ├── 04_almacenamiento.ipynb   # almacenamiento de datos
│   ├── 05_pipeline.ipynb         # pipeline de datos
│   └── experiments/              # notebooks auxiliares de pruebas
│── dags/                 # DAGs de Airflow (orquestación)
│   ├── __init__.py
│   ├── ingest_dag.py
│   ├── clean_dag.py
│   ├── pipeline_dag.py
│   └── validate_dag.py
│
├── src/
│   ├── common/           # lógica común
│   ├── interfaces/       # interfaces de usuario
│   └── etl/              # <--- nuevo directorio (o "ingest", como prefieras)
│       ├── __init__.py
│       ├── ingest.py  
│       ├── clean.py
│       ├── pipeline.py
│       └── validate.py
├── models/               # almacenamiento de modelos ML
├── predictions/          # resultados de predicciones
├── docs/                 # reportes y documentación
│
├── README.md             # documentación del proyecto
├── INSTRUCTIONS.md       # instrucciones de instalación
└── requirements.txt      # librerías necesarias


