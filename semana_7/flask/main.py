
from flask import Flask
from controllers.animal_controller import animal_bp
from controllers.saludos_controller import saludos_bp

app = Flask(__name__)
app.register_blueprint(animal_bp)
app.register_blueprint(saludos_bp)

if __name__ == '__main__':
	app.run(debug=True)