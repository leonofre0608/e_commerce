E-Commerce - Catálogo de Productos con Django y JavaScript

Este proyecto es un mini e-commerce desarrollado para la gestión de un catálogo de productos. Permite visualizar, agregar y eliminar productos (incluyendo la carga de imágenes) utilizando Django en el backend con PostgreSQL y HTML con Vanilla JavaScript en el frontend.

---

Requisitos Previos

Asegúrate de tener instalado lo siguiente en tu sistema:
* Python 3.10 o superior
* PostgreSQL
* Git



## Guía de Instalación y Configuración

### Clonar el repositorio
Abre tu terminal y clona este proyecto:
```bash
# 1. Clonar el repositorio
git clone <URL_DE_TU_REPOSITORIO>

# 2. Entrar a la carpeta generada por Git
cd <nombre-de-la-carpeta-clonada>

## CREA Y ACTIVA EL ENTORNO VIRTUAL

python -m venv djangoenv #CREAR
.\djangoenv\Scripts\activate # ACTIVAR


##INSTALAR DEPENDENCIAS 
pip install -r requeriments.txt

##VARIABLE DE ENTORNO Y BASE DE DATOS
SECRET_KEY=tu_clave_secreta_aqui
DEBUG=True

DB_NAME=nombre_de_tu_bd
DB_USER=postgres
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432

##APLICAR MIGACIONES
python manage.py makemigrations
python manage.py migrate

## CREAR UN SUPER USUARIO
python manage.py createsuperuser


##EJECUCION DEL PROJECTO
python manage.py runserver