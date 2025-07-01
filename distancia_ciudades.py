#!/usr/bin/env python3

"""
Script que mide la distancia entre una ciudad de Chile y una de Argentina.
Utiliza la API de Nominatim (OpenStreetMap) para obtener las coordenadas
y la fórmula de Haversine para calcular la distancia.
"""

import requests
import math

# Función para obtener las coordenadas (latitud, longitud) de una ciudad
def obtener_coordenadas(ciudad, pais):
    """
    Usa la API de Nominatim para convertir un nombre de ciudad en coordenadas.
    """
    # URL de la API de Nominatim. Se añade un User-Agent como buena práctica.
    url = f"https://nominatim.openstreetmap.org/search?q={ciudad},{pais}&format=json"
    headers = {
        'User-Agent': 'ExamenDRY7122/1.0 (https://github.com/NicolasEstayFernandez/Examen-Transversal-Programacion-y-Redes-Virtualizadas-DRY7122)'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Esto generará un error si la solicitud HTTP falla
        
        data = response.json()
        
        if data:
            # Si se encontraron resultados, devuelve la latitud y longitud del primero
            latitud = float(data[0]['lat'])
            longitud = float(data[0]['lon'])
            return latitud, longitud
        else:
            # Si no se encontró la ciudad
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None

# Función para calcular la distancia usando la fórmula de Haversine
def calcular_distancia(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia en kilómetros entre dos puntos geográficos.
    """
    R = 6371  # Radio de la Tierra en kilómetros

    # Convertir coordenadas de grados a radianes
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Diferencias de longitud y latitud
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    # Fórmula de Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = R * c

    return distancia

# --- Lógica Principal del Script ---
if __name__ == "__main__":
    print("--- Calculadora de Distancia entre Ciudades ---")
    
    # 1. Obtener los nombres de las ciudades del usuario
    ciudad_chile = input("Ingrese una ciudad de Chile: ")
    ciudad_argentina = input("Ingrese una ciudad de Argentina: ")
    
    print(f"\nBuscando coordenadas para {ciudad_chile}, Chile...")
    coordenadas_chile = obtener_coordenadas(ciudad_chile, "Chile")
    
    print(f"Buscando coordenadas para {ciudad_argentina}, Argentina...")
    coordenadas_argentina = obtener_coordenadas(ciudad_argentina, "Argentina")
    
    # 2. Verificar que ambas ciudades fueron encontradas
    if coordenadas_chile and coordenadas_argentina:
        # Si se encontraron ambas, calcular la distancia
        distancia_km = calcular_distancia(
            coordenadas_chile[0], coordenadas_chile[1],
            coordenadas_argentina[0], coordenadas_argentina[1]
        )
        
        # 3. Mostrar el resultado
        print("\n--- RESULTADO ---")
        print(f"La distancia entre {ciudad_chile} y {ciudad_argentina} es de aproximadamente {round(distancia_km)} km.")
        
    else:
        # Si una o ambas ciudades no se encontraron
        print("\nNo se pudo calcular la distancia. Asegúrese de que los nombres de las ciudades sean correctos.")