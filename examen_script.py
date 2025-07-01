#!/usr/bin/env python3

"""
Script que define una lista con los integrantes, el número del grupo,
y luego imprime toda la información en la consola.
"""

# --- INICIO DEL CÓDIGO ---

# 1. Definir las variables del grupo.
numero_grupo = 7
integrantes = [
    "Nicolas Estay",
    "Sebastian Lopez",
    "Vicente Gonzalez"
]

# 2. Imprimir la información del grupo.
print("--- Datos del Grupo ---")
print(f"Grupo Número: {numero_grupo}")
print("-----------------------")
print("Integrantes:")

# 3. Recorrer la lista e imprimir cada integrante.
for integrante in integrantes:
    print(f"- {integrante}")

# Imprimir un pie de página para marcar el fin del script.
print("-----------------------")

# --- FIN DEL CÓDIGO ---