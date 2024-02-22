import os
from pathlib import Path
import logging


# Configuración del sistema de registro (logging) para la aplicación.
# Se establece el nivel de registro en INFO para registrar mensajes de nivel INFO o superior.
# El formato del registro incluye la marca de tiempo y el mensaje.
# El formato puede necesitar revisión para eliminar el carácter ':' al final.
logging.basicConfig(level = logging.INFO, format= '[%(asctime)s]: %(message)s:')


project_name = "mlProject"

# Defino la carpeta y archivos que se deben crear en el proceso
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]


# Proceso para crear la estructura del proyecto
for filepath in list_of_files:
    #Revisión de los archivos que se van a crear
    #print(filepath) 

    # Divide la ruta del archivo en el directorio y el nombre del archivo.
    # filedir contendrá el directorio del archivo y filename contendrá el nombre del archivo.
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file:  {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file : {filepath}")
    
    else:
        logging.info(f"Is already exists : {filename}")
