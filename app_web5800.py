from flask import Flask, request, render_template_string
import sqlite3
import hashlib

app = Flask(__name__)
DB_NAME = "usuarios.db"

HTML_FORM = """
<!DOCTYPE html><html><head><title>Login</title></head><body>
<h1>Login de Usuarios DRY7122</h1>
<form action="/login" method="post">
    <label>Nombre:</label><br><input type="text" name="nombre"><br><br>
    <label>Contraseña:</label><br><input type="password" name="contrasena"><br><br>
    <input type="submit" value="Ingresar">
</form></body></html>
"""

@app.route('/')
def home():
    return HTML_FORM

@app.route('/login', methods=['POST'])
def login():
    nombre = request.form['nombre']
    contrasena = request.form['contrasena']
    hash_pass = hashlib.sha256(contrasena.encode()).hexdigest()

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND contrasena = ?", (nombre, hash_pass))
        resultado = cursor.fetchone()

    if resultado:
        return "<h1>Acceso permitido</h1>"
    else:
        return "<h1>Usuario o contraseña incorrecta</h1>"

if __name__ == '__main__':
    try:
        __import__('flask')
    except ImportError:
        print("Flask no está instalado. Instalando...")
        __import__('os').system('pip install Flask')

    print("Iniciando servidor web en http://127.0.0.1:5800")
    app.run(host='0.0.0.0', port=5800)