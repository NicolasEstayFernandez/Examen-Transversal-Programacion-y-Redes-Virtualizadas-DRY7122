import sqlite3
import hashlib
from nombres_integrantes import USUARIOS_EXAMEN

DB_NAME = "usuarios.db"
print(f"Iniciando la creación de la base de datos '{DB_NAME}'...")

with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            nombre TEXT PRIMARY KEY,
            contrasena TEXT NOT NULL
        )
    """)
    print("-> Tabla 'usuarios' creada o verificada.")

    for nombre, contrasena in USUARIOS_EXAMEN.items():
        hash_contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
        cursor.execute(
            "INSERT OR IGNORE INTO usuarios (nombre, contrasena) VALUES (?, ?)",
            (nombre, hash_contrasena)
        )
    print("-> Usuarios del examen insertados en la base de datos.")

print("Proceso completado. La base de datos está lista.")
