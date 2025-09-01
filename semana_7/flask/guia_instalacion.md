# Guía de Instalación de Flask en Windows

Esta guía será de utilidad para instalar Flask en Windows utilizando un entorno virtual (`venv`). El uso de entornos virtuales es una práctica recomendada, ya que permite aislar las dependencias de cada proyecto, evita conflictos entre paquetes y mantiene el sistema limpio.

## 1. Instalar Python

Se debe contar con Python instalado en el sistema. El instalador se encuentra disponible en [python.org](https://www.python.org/downloads/windows/). Es importante marcar la opción **Add Python to PATH** durante la instalación.

## 2. Crear un entorno virtual (venv)

En PowerShell o CMD, se debe navegar a la carpeta del proyecto:

```powershell
cd ruta\a\tu\proyecto
```

Para crear el entorno virtual:

```powershell
python -m venv venv
```

Esto generará una carpeta llamada `venv` con una instalación aislada de Python.

## 3. Activar el entorno virtual

En PowerShell:

```powershell
.\venv\Scripts\Activate
```

En CMD:

```cmd
venv\Scripts\activate.bat
```

El prompt cambiará, indicando que el entorno está activo.

## 4. Instalar Flask

Con el entorno virtual activo, se puede instalar Flask ejecutando:

```powershell
pip install flask
```

## 5. Crear un archivo de requerimientos

Para guardar las dependencias del proyecto, se debe ejecutar:

```powershell
pip freeze > requirements.txt
```

Esto generará un archivo `requirements.txt` con los paquetes instalados.

## 6. Instalar dependencias desde requirements.txt

Si el proyecto se comparte, otros usuarios pueden instalar las mismas dependencias ejecutando:

```powershell
pip install -r requirements.txt
```

## 7. Crear y ejecutar una app Flask básica

Se puede crear un archivo `main.py` con el siguiente contenido:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
	return "¡Hola, mundo!"

if __name__ == '__main__':
	app.run(debug=True)
```

Para ejecutar la aplicación:

```powershell
python main.py
```

## 8. Desactivar el entorno virtual

Al finalizar, el entorno virtual puede desactivarse con:

```powershell
deactivate
```


