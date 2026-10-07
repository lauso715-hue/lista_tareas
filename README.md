# Lista de Tareas - Proyecto Django

##  Descripción
Aplicación web CRUD (Create, Read, Update, Delete) desarrollada con Django para gestionar tareas. Permite crear, listar, editar y eliminar tareas con título, descripción, fecha de vencimiento y estado.

##  Tecnologías usadas
- Python
- Django
- SQLite (Base de datos)
- HTML

##  Funcionalidades
- Crear nuevas tareas.
- Ver la lista de todas las tareas.
- Editar tareas existentes.
- Eliminar tareas.
- Gestión de estados (Completada / Pendiente).

##  Cómo ejecutar el proyecto localmente
1. Clonar el repositorio:
   `git clone [PEGA_AQUÍ_LA_URL_DE_TU_REPOSITORIO]`
2. Crear un entorno virtual:
   `python -m venv env`
3. Activar el entorno virtual (Windows):
   `env\Scripts\activate`
4. Instalar las dependencias:
   `pip install -r requirements.txt`
5. Realizar las migraciones (crear la base de datos):
   `python manage.py migrate`
6. Iniciar el servidor:
   `python manage.py runserver`
7. Abrir en el navegador:
   `http://127.0.0.1:8000/`

##  Autor
[Nombre Completo] - [Tu Correo o Usuario de GitHub]
