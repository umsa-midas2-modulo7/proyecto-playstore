# 1. Instala Python y pip (si no los tienes)

sudo apt update
sudo apt install python3 python3-pip python3-venv -y

# 2. Crea un entorno virtual

python3 -m venv venv

# 3. Activa el entorno

source venv/bin/activate

# 4. Actualizar PIP

python -m pip install --upgrade pip
python.exe -m pip install --upgrade pip

# 5. Instala librerias

pip install -r requirements.txt

# 6. Levantar el proyecto

jupyter notebook

