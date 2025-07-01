#!/usr/bin/env python3

"""
Script que solicita al usuario un número de VLAN y determina si pertenece
al rango normal (1-1005) o al rango extendido (1006-4094).
"""

# Definimos los rangos para claridad y fácil mantenimiento.
RANGO_NORMAL_INICIO = 1
RANGO_NORMAL_FIN = 1005
RANGO_EXTENDIDO_INICIO = 1006
RANGO_EXTENDIDO_FIN = 4094

print("--- Verificador de Rango de VLAN ---")

# Usamos un bloque try-except para manejar errores si el usuario no ingresa un número.
try:
    # 1. Solicitar el número de VLAN al usuario.
    # La función input() siempre devuelve el dato como texto (string).
    vlan_input = input("Por favor, ingrese el número de VLAN: ")

    # 2. Convertir el texto ingresado a un número entero.
    # Si el usuario escribe algo que no es un número, esto provocará un error.
    vlan_id = int(vlan_input)

    # 3. Aplicar la lógica de verificación con condicionales (if/elif/else).
    if vlan_id >= RANGO_NORMAL_INICIO and vlan_id <= RANGO_NORMAL_FIN:
        # Si el número está en el rango normal
        print(f"\nLa VLAN {vlan_id} corresponde al RANGO NORMAL.")

    elif vlan_id >= RANGO_EXTENDIDO_INICIO and vlan_id <= RANGO_EXTENDIDO_FIN:
        # Si el número está en el rango extendido
        print(f"\nLa VLAN {vlan_id} corresponde al RANGO EXTENDIDO.")
        
    else:
        # Si el número está fuera de los rangos válidos (ej: 0, 5000, -10)
        print(f"\nError: El número {vlan_id} está fuera de los rangos de VLAN válidos (1-4094).")

except ValueError:
    # Este bloque se ejecuta si el int() falla, es decir, si el usuario
    # ingresó texto en lugar de un número (ej: "abc").
    print("\nError: Debe ingresar solo un número entero válido.")

print("------------------------------------")