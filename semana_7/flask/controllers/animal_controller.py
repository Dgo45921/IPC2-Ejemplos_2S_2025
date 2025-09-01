from flask import Blueprint, render_template, request, redirect, url_for
from models.lista_enlazada import ListaEnlazada
from models.animal import Animal

animal_bp = Blueprint('animal', __name__)
lista = ListaEnlazada()

@animal_bp.route('/')
def index():
    animales = lista
    return render_template('index.html', animales=animales)

@animal_bp.route('/animal/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        especie = request.form['especie']
        animal = Animal(nombre, especie)
        lista.agregar(animal)
        return redirect(url_for('animal.index'))
    return render_template('form.html', titulo='Agregar Animal', animal=None)

@animal_bp.route('/animal/editar/<nombre>', methods=['GET', 'POST'])
def editar(nombre):
    animales = lista
    animal = next((a for a in animales if a.nombre == nombre), None)
    if not animal:
        return redirect(url_for('animal.index'))
    if request.method == 'POST':
        nuevo_nombre = request.form['nombre']
        nueva_especie = request.form['especie']
        nuevo_animal = Animal(nuevo_nombre, nueva_especie)
        lista.actualizar(nombre, nuevo_animal)
        return redirect(url_for('animal.index'))
    return render_template('form.html', titulo='Editar Animal', animal=animal)

@animal_bp.route('/animal/eliminar/<nombre>')
def eliminar(nombre):
    lista.eliminar(nombre)
    return redirect(url_for('animal.index'))
