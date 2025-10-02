## Paso 1: poner todos los contenedores en la misma red

$ docker network create data-net

$ sudo docker network connect data-net postgres-11-db-1
$ sudo docker network connect data-net mongo-6-mongo-1

# LEVANTAR DOCKER COMPOSE

### Inicializa tablas en victor.apache_airflow
```
sudo docker compose up airflow-init
```

### Levanta servicios
```
sudo docker compose up -d webserver scheduler triggerer
```

### Verifica estado
```
sudo docker compose ps
```

### Verifica si hay usuarios
```
sudo docker compose exec webserver airflow users list
```

### Registrar nuevo usuario
```
sudo docker compose exec webserver airflow users create \
  --username admin \
  --firstname Victor \
  --lastname Quino \
  --role Admin \
  --email admin@example.com \
  --password admin
```

### Para detener el conenedor, debe estar donde esta el yaml y ejecutar:
```
sudo docker compose down (para borrar)
sudo docker compose stop (para parar)
```

### Ver logs de un contenedor
```
sudo docker compose logs -f --tail=100 scheduler
sudo docker compose exec webserver airflow dags list-import-errors
```

# ERRORES


### Error con SCHEDULER

En la base de datos se debe varificar que ya exisite un registro minimamente en la tabla apache_airflow.log_template, si no hay un registro ejecutar en base de datos:
```
INSERT INTO apache_airflow.log_template (id, filename, elasticsearch_id, created_at)
VALUES (
  1,
  '{{ ti.dag_id }}/{{ ti.task_id }}/{{ ts }}/{{ try_number }}.log',
  '{{ ti.dag_id }}-{{ ti.task_id }}-{{ ts }}-{{ try_number }}',
  now()
)
ON CONFLICT (id) DO NOTHING;
```

En la terminal verificar que ya esta corriendo corectamente SCHEDULER:
```
sudo docker compose restart scheduler
sudo docker compose logs -f --tail=100 scheduler
```

## INSTALACION DE LIBRERIAS

```
sudo docker compose exec webserver  bash -lc "python -m pip install --no-cache-dir -r /opt/airflow/requirements.txt"
sudo docker compose exec scheduler  bash -lc "python -m pip install --no-cache-dir -r /opt/airflow/requirements.txt"
sudo docker compose exec triggerer  bash -lc "python -m pip install --no-cache-dir -r /opt/airflow/requirements.txt"
```

## DAGS

Lista de DAGS
```
sudo docker compose exec webserver airflow dags list 
```
Error al CARGAR un nuevo DAG
```
sudo docker compose exec webserver airflow dags list-import-errors
```
Monitorear logs SCHEDULER en tiempo real
```
sudo docker compose logs -f --tail=100 scheduler
```
Ejecutar un DAG
```
sudo docker compose exec webserver airflow tasks test ingesta_prueba_dag run_and_print 2025-10-01T19:15:00+00:00

sudo docker compose exec webserver airflow tasks test ingesta_prueba_multi_dag run_and_print 2025-10-01T19:15:00+00:00
```