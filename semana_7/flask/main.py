
from flask import Flask, render_template, request, redirect, url_for
from controllers.animal_controller import crear_animal, eliminar_animal, actualizar_animal, obtener_animales

app = Flask(__name__)

@app.route('/')
def index():
	animales = obtener_animales()
	return render_template('index.html', animales=animales)

@app.route('/crear', methods=['GET', 'POST'])
def crear():
	if request.method == 'POST':
		nombre = request.form['nombre']
		especie = request.form['especie']
		crear_animal(nombre, especie)
		return redirect(url_for('index'))
	return render_template('form.html', titulo='Agregar Animal', animal=None)

@app.route('/editar/<nombre>', methods=['GET', 'POST'])
def editar(nombre):
	animales = obtener_animales()
	animal = next((a for a in animales if a.nombre == nombre), None)
	if not animal:
		return redirect(url_for('index'))
	if request.method == 'POST':
		nuevo_nombre = request.form['nombre']
		nueva_especie = request.form['especie']
		actualizar_animal(nombre, nuevo_nombre, nueva_especie)
		return redirect(url_for('index'))
	return render_template('form.html', titulo='Editar Animal', animal=animal)

@app.route('/eliminar/<nombre>')
def eliminar(nombre):
	eliminar_animal(nombre)
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)