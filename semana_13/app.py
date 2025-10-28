from flask import Flask, request, jsonify
import jwt
import datetime
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)

# Endpoint público para generar token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Simulación de validación de usuario
    if username == "admin" and password == "admin":
        payload = {
            "user": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token})
    
    elif username == "user" and password == "user":
        payload = {
            "user": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token})
    
    return jsonify({"message": "Credenciales incorrectas"}), 401

# Decorador para proteger rutas
def token_required(f):
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            parts = auth_header.split()
            if len(parts) == 2 and parts[0] == "Bearer":
                token = parts[1]
        if not token:
            return jsonify({"message": "Token es requerido"}), 401

        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            print(f"Usuario que hizo la request: {decoded['user']}")
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token inválido"}), 401

        return f(*args, **kwargs)
    decorator.__name__ = f.__name__ 
    return decorator

# Ruta protegida
@app.route('/protegido', methods=['GET'])
@token_required
def protegido():
    return jsonify({"message": "Acceso permitido a la ruta protegida"})

if __name__ == "__main__":
    app.run(debug=True)
