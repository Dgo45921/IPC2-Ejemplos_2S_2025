from flask import Flask
from controllers.persona_controller import persona_bp
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.register_blueprint(persona_bp, url_prefix='/personas')

if __name__ == '__main__':
    app.run(debug=True)