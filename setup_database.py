import sqlite3
import hashlib

DB_NAME = "usuarios.db"

# Nombres de los integrantes y sus contraseñas elegidas
usuarios_para_insertar = {
    "Nicolas Estay": "clave_nicolas",
    "Sebastian Lopez": "clave_sebastian",
    "Vicente Gonzalez": "clave_vicente"
}

with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()

    # Crear la tabla 'usuarios' con 'nombre' y 'contrasena'
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            nombre TEXT PRIMARY KEY,
            contrasena TEXT NOT NULL
        )
    """)
    print("Tabla 'usuarios' creada o ya existente.")

    # Insertar cada usuario con su contraseña hasheada
    for nombre, contrasena in usuarios_para_insertar.items():
        # Hashear la contraseña con SHA256
        hash_contrasena = hashlib.sha256(contrasena.encode()).hexdigest()

        # Usar INSERT OR IGNORE para no fallar si el usuario ya existe
        cursor.execute(
            "INSERT OR IGNORE INTO usuarios (nombre, contrasena) VALUES (?, ?)",
            (nombre, hash_contrasena)
        )

    print("Usuarios insertados/actualizados en la base de datos.")

print("Base de datos preparada exitosamente.")
