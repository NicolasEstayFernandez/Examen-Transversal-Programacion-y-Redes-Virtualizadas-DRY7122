#!/usr/bin/env python3

"""
Script que mide la distancia entre una ciudad de origen y una de destino.
Utiliza la API de Nominatim (OpenStreetMap) para obtener las coordenadas
y la fórmula de Haversine para calcular la distancia.
"""

import requests
import math

# La función ahora es más genérica. Solo necesita un lugar para buscar.
def obtener_coordenadas(lugar):
    """
    Usa la API de Nominatim para convertir el nombre de un lugar en coordenadas.
    """
    # URL de la API. La consulta 'q' ahora es simplemente el lugar.
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
            # Devolvemos también el nombre completo encontrado por la API para más claridad.
            nombre_encontrado = data[0]['display_name']
            print(f"Coordenadas encontradas para '{lugar}': {nombre_encontrado}")
            return latitud, longitud
        else:
            print(f"Error: No se pudieron encontrar coordenadas para '{lugar}'.")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None

# La función para calcular la distancia no necesita cambios.
def calcular_distancia(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia en kilómetros entre dos puntos geográficos.
    """
    R = 6371  # Radio de la Tierra en kilómetros
    lat1_rad, lon1_rad = math.radians(lat1), math.radians(lon1)
    lat2_rad, lon2_rad = math.radians(lat2), math.radians(lon2)
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = R * c
    return distancia

# --- Lógica Principal del Script ---
if __name__ == "__main__":
    print("--- Calculadora de Distancia entre Ciudades ---")
    
    # 1. Solicitar "Ciudad de Origen" y "Ciudad de Destino".
    # Se recomienda al usuario poner "Ciudad, País" para mejores resultados.
    ciudad_origen = input("Ingrese la Ciudad de Origen (ej: Santiago, Chile): ")
    ciudad_destino = input("Ingrese la Ciudad de Destino (ej: Mendoza, Argentina): ")
    
    print("-" * 20) # Separador visual
    
    coordenadas_origen = obtener_coordenadas(ciudad_origen)
    coordenadas_destino = obtener_coordenadas(ciudad_destino)
    
    # 2. Verificar que ambas ciudades fueron encontradas
    if coordenadas_origen and coordenadas_destino:
        distancia_km = calcular_distancia(
            coordenadas_origen[0], coordenadas_origen[1],
            coordenadas_destino[0], coordenadas_destino[1]
        )
        
        # 3. Mostrar el resultado
        print("\n--- RESULTADO ---")
        print(f"La distancia entre '{ciudad_origen}' y '{ciudad_destino}' es de aproximadamente {round(distancia_km)} km.")
        
    else:
        print("\nNo se pudo calcular la distancia. Una o ambas ciudades no fueron encontradas.")