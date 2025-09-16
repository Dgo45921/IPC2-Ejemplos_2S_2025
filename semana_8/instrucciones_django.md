# Guía de Instalación y Uso Básico de Django

## Instalación de Django

1. **Instalar Python**
   - Verificar que Python esté instalado ejecutando `python --version` en la terminal.
   - Descargar Python desde [python.org](https://www.python.org/) si no está instalado.

2. **Instalar Django**
   - Se recomienda crear un entorno virtual:
     ```powershell
     python -m venv venv
     venv\Scripts\activate
     ```
   - Instalar Django usando pip:
     ```powershell
     pip install django
     ```
   - Verificar la instalación:
     ```powershell
     python -m django --version
     ```

## Comandos Básicos de Django

### Crear un Proyecto

Para crear un nuevo proyecto Django, se utiliza el siguiente comando:
```powershell
django-admin startproject nombre_proyecto
```
Esto generará una carpeta con la estructura básica del proyecto.

### Ejecutar el Servidor de Desarrollo

Dentro de la carpeta del proyecto, se puede iniciar el servidor de desarrollo con:
```powershell
python manage.py runserver
```
El servidor estará disponible en `http://127.0.0.1:8000/`.

### Crear una Aplicación (App)

Para crear una nueva aplicación dentro del proyecto:
```powershell
python manage.py startapp nombre_app
```
Esto generará la estructura de archivos necesaria para la aplicación.

## Comandos Importantes para la Administración y Migraciones

### Crear superusuario (acceso admin)
Para crear el superusuario que te permite acceder al panel de administración de Django, ejecuta:
```powershell
python manage.py createsuperuser
```
Sigue las instrucciones para ingresar usuario, correo y contraseña.

### Migraciones de la base de datos
- **Crear archivos de migración (cuando cambias modelos):**
  ```powershell
  python manage.py makemigrations
  ```
- **Aplicar migraciones a la base de datos:**
  ```powershell
  python manage.py migrate
  ```

### Acceso al panel de administración
- Inicia el servidor:
  ```powershell
  python manage.py runserver
  ```
- Ingresa a `http://localhost:8000/admin` y accede con el superusuario creado.

## Estructura Básica de un Proyecto Django

- `manage.py`: Herramienta de línea de comandos para tareas administrativas.
- Carpeta del proyecto (por ejemplo, `nombre_proyecto/`): Configuración principal.
- Carpeta de aplicaciones (por ejemplo, `nombre_app/`): Código de la aplicación.

## Recursos Adicionales

- Documentación oficial: [https://docs.djangoproject.com/es/](https://docs.djangoproject.com/es/)
- Tutorial oficial: [https://docs.djangoproject.com/es/4.2/intro/tutorial01/](https://docs.djangoproject.com/es/4.2/intro/tutorial01/)

