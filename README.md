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
│
├── src/
│   ├── common/           # lógica común
│   ├── interfaces/       # interfaces de usuario
│   ├── ingest.py         # lógica de ingesta de reseñas
│   ├── clean.py          # reglas de limpieza
│   ├── validate.py       # validaciones de calidad de datos (great_expectations)
│   └── pipeline.py       # pipeline completo
│
├── models/               # almacenamiento de modelos ML
├── predictions/          # resultados de predicciones
├── dags/                 # DAGs de Airflow (orquestación)
├── docs/                 # reportes y documentación
│
├── README.md             # documentación del proyecto
├── INSTRUCTIONS.md       # instrucciones de instalación
└── requirements.txt      # librerías necesarias


