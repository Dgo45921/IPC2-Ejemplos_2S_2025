from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "clave_segura_para_flash"

# Carpeta donde se guardarán las imágenes
UPLOAD_FOLDER = os.path.join('static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Verifica si la extensión del archivo es válida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    # Verifica si el formulario contiene archivos
    if 'file' not in request.files:
        flash('No se envió ningún archivo.')
        return redirect(request.url)

    file = request.files['file']

    # Si el usuario no seleccionó ningún archivo
    if file.filename == '':
        flash('No se seleccionó ninguna imagen.')
        return redirect(request.url)

    # Si el archivo es válido
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Imagen subida correctamente.')
        return redirect(url_for('uploaded_file', filename=filename))
    else:
        flash('Tipo de archivo no permitido. Solo se aceptan imágenes.')
        return redirect(request.url)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    file_url = url_for('static', filename='uploads/' + filename)
    return f'''
        <h3>Imagen subida correctamente:</h3>
        <img src="{file_url}" alt="Imagen subida" width="400">
        <br><br>
        <a href="/">Subir otra imagen</a>
    '''


if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
