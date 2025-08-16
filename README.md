# Proyecto Django - Sistema de Login

Este proyecto es una aplicación web desarrollada con **Django** que implementa un sistema de autenticación completo.

## Funcionalidades
- Registro de usuarios (signup)
- Inicio de sesión con opción "Recordarme"
- Cierre de sesión seguro (requiere POST)
- Cambio de contraseña
- Recuperación de contraseña por email (consola)
- Vista protegida que requiere login

## Requisitos
- Python 3.10+
- Django 5.x

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/django_login.git
   cd django_login

2. Crear y activar un entorno virtual:
    python3 -m venv .venv
    source .venv/bin/activate  # En Windows: .venv\Scripts\activate

3. Instalar dependencias:
    pip install -r requirements.txt

4. Aplicar migraciones:
    python manage.py migrate

## Uso
1. Iniciar el servidor:
    python manage.py runserver

2. Abir en el navegador:
    http://127.0.0.1:8000/
    
## Uso
* Usuario: admin
* Contraseña: admin1234
    (Si no existe, crear con `python manage.py createsuperuser`)

## Autor

Luis Dolfi - GitHub
