#!/usr/bin/env python3

"""
Script que mide la distancia entre una ciudad de origen y una de destino.
Muestra la distancia en kilómetros, millas y una duración estimada del viaje en auto.
Utiliza la API de Nominatim (OpenStreetMap) para obtener las coordenadas
y la fórmula de Haversine para calcular la distancia.
"""

import requests
import math

# --- CONSTANTES ---
# Es una buena práctica definir valores que no cambian como constantes.
CONVERSION_KM_A_MILLAS = 0.621371
# Asumimos una velocidad promedio para un viaje largo en auto. Esto es una ESTIMACIÓN.
VELOCIDAD_PROMEDIO_KMH = 80 

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

# --- LÓGICA PRINCIPAL DEL SCRIPT ---
if __name__ == "__main__":
    print("--- Calculadora de Distancia y Duración de Viaje ---")
    
    ciudad_origen = input("Ingrese la Ciudad de Origen (ej: Santiago, Chile): ")
    ciudad_destino = input("Ingrese la Ciudad de Destino (ej: Mendoza, Argentina): ")
    
    print("-" * 20)
    
    coordenadas_origen = obtener_coordenadas(ciudad_origen)
    coordenadas_destino = obtener_coordenadas(ciudad_destino)
    
    if coordenadas_origen and coordenadas_destino:
        # --- CÁLCULOS ---
        # 1. Calcular distancia en kilómetros (como antes)
        distancia_km = calcular_distancia(
            coordenadas_origen[0], coordenadas_origen[1],
            coordenadas_destino[0], coordenadas_destino[1]
        )
        
        # 2. Convertir kilómetros a millas
        distancia_millas = distancia_km * CONVERSION_KM_A_MILLAS
        
        # 3. Calcular duración del viaje en horas
        duracion_horas_decimal = distancia_km / VELOCIDAD_PROMEDIO_KMH
        # Convertir las horas decimales a formato horas y minutos
        horas = int(duracion_horas_decimal)
        minutos = int((duracion_horas_decimal - horas) * 60)
        
        # --- MOSTRAR RESULTADOS ---
        print("\n--- RESULTADO DEL VIAJE ---")
        print(f"Desde: {ciudad_origen}")
        print(f"Hasta: {ciudad_destino}")
        print("-" * 25)
        print(f"Distancia en Kilómetros: {round(distancia_km)} km")
        print(f"Distancia en Millas:      {round(distancia_millas)} mi")
        print(f"Duración estimada del viaje en auto: {horas} horas y {minutos} minutos")
        print(f"(Estimación basada en una velocidad promedio de {VELOCIDAD_PROMEDIO_KMH} km/h)")
        
    else:
        print("\nNo se pudo calcular la distancia. Una o ambas ciudades no fueron encontradas.")