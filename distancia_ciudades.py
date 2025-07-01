#!/usr/bin/env python3

"""
Script interactivo que mide la distancia entre ciudades.
Permite al usuario elegir un medio de transporte y calcula la duración del viaje.
El programa se ejecuta en un bucle y se puede salir ingresando 's'.
"""

import requests
import math

# --- CONSTANTES ---
CONVERSION_KM_A_MILLAS = 0.621371
TRANSPORTES = {
    "1": ("Auto", 80),
    "2": ("Avión", 850),
    "3": ("Bicicleta", 18),
    "4": ("A pie", 5)
}

# --- FUNCIONES ---
def obtener_coordenadas(lugar):
    """
    Usa la API de Nominatim para convertir el nombre de un lugar en coordenadas.
    """
    url = f"https://nominatim.openstreetmap.org/search?q={lugar}&format=json"
    headers = {
        'User-Agent': 'ExamenDRY7122/1.0 (https://github.com/NicolasEstayFernandez/Examen-Transversal-Programacion-y-Redes-Virtualizadas-DRY7122)'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        if data:
            latitud = float(data[0]['lat'])
            longitud = float(data[0]['lon'])
            nombre_encontrado = data[0]['display_name']
            print(f"Coordenadas encontradas para '{lugar}': {nombre_encontrado}")
            return latitud, longitud
        else:
            print(f"Error: No se pudieron encontrar coordenadas para '{lugar}'.")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None

def calcular_distancia(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia en kilómetros entre dos puntos geográficos.
    """
    R = 6371
    lat1_rad, lon1_rad = math.radians(lat1), math.radians(lon1)
    lat2_rad, lon2_rad = math.radians(lat2), math.radians(lon2)
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = R * c
    return distancia

def generar_narrativa(origen, destino, km, millas, horas, minutos, transporte, velocidad):
    """
    Crea un texto descriptivo (narrativa) del viaje, incluyendo el transporte.
    """
    narrativa = (
        f"¡Prepara todo para tu próxima aventura! El viaje comenzará en {origen} y te llevará hasta tu destino: {destino}.\n\n"
        f"Cubrirás una distancia total de {round(km)} kilómetros (aproximadamente {round(millas)} millas).\n"
        f"Viajando en {transporte.lower()} a una velocidad promedio estimada de {velocidad} km/h, "
        f"el tiempo de viaje será de alrededor de {horas} horas y {minutos} minutos.\n\n"
        f"¡Que tengas un excelente y seguro viaje!"
    )
    return narrativa

# --- LÓGICA PRINCIPAL DEL SCRIPT ---
if __name__ == "__main__":
    
    # Bucle principal para que el programa se ejecute continuamente
    while True:
        print("\n" + "="*50)
        print("--- Calculadora de Distancia y Duración de Viaje ---")
        print("(Ingrese 's' en cualquier momento para salir del programa)")
        print("="*50)
        
        ciudad_origen = input("Ingrese la Ciudad de Origen: ")
        
        # Condición de salida: si el usuario ingresa 's' o 'S'
        if ciudad_origen.lower() == 's':
            print("\nSaliendo del programa. ¡Hasta luego!")
            break  # Rompe el bucle while y termina el script
        
        ciudad_destino = input("Ingrese la Ciudad de Destino: ")

        if ciudad_destino.lower() == 's':
            print("\nSaliendo del programa. ¡Hasta luego!")
            break

        print("-" * 20)
        
        coordenadas_origen = obtener_coordenadas(ciudad_origen)
        coordenadas_destino = obtener_coordenadas(ciudad_destino)
        
        if coordenadas_origen and coordenadas_destino:
            # Menú para elegir el medio de transporte
            print("\nSeleccione el medio de transporte:")
            for key, value in TRANSPORTES.items():
                print(f"{key}. {value[0]}")
            
            opcion_transporte = ""
            while opcion_transporte not in TRANSPORTES:
                opcion_transporte = input("Ingrese el número de su opción (1-4): ")
                if opcion_transporte.lower() == 's':
                    break # Permite salir también en este punto
                if opcion_transporte not in TRANSPORTES:
                    print("Opción no válida. Por favor, elija un número del 1 al 4.")
            
            if opcion_transporte.lower() == 's':
                print("\nSaliendo del programa. ¡Hasta luego!")
                break
            
            nombre_transporte, velocidad_elegida = TRANSPORTES[opcion_transporte]

            # --- CÁLCULOS ---
            distancia_km = calcular_distancia(
                coordenadas_origen[0], coordenadas_origen[1],
                coordenadas_destino[0], coordenadas_destino[1]
            )
            distancia_millas = distancia_km * CONVERSION_KM_A_MILLAS
            duracion_horas_decimal = distancia_km / velocidad_elegida
            horas = int(duracion_horas_decimal)
            minutos = int((duracion_horas_decimal - horas) * 60)
            
            # --- GENERAR Y MOSTRAR NARRATIVA ---
            narrativa_del_viaje = generar_narrativa(
                ciudad_origen, ciudad_destino, 
                distancia_km, distancia_millas, 
                horas, minutos,
                nombre_transporte, velocidad_elegida
            )
            
            print("\n" + "="*25)
            print("   NARRATIVA DEL VIAJE")
            print("="*25 + "\n")
            print(narrativa_del_viaje)
            
        else:
            print("\nNo se pudo generar la narrativa. Una o ambas ciudades no fueron encontradas.")