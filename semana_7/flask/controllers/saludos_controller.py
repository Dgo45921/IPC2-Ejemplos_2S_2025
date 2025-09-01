from flask import Blueprint


saludos_bp = Blueprint('saludo', __name__)

@saludos_bp.route('/saludo/<nombre>')
def saludo(nombre):
    return f"¡Hola, {nombre}!"

