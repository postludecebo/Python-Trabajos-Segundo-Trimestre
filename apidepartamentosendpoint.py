import requests
import json

url = "https://api-colombia.com/api/v1/Department"

try:
    respuesta = requests.get(url, timeout = 10)

    if respuesta.status_code == 200:
        datos = respuesta.json()

        for atraccion in datos:
            nombre = atraccion.get("name", "Nombre no disponible")
            print(f"Nombre: {nombre}")

    
    else:
        print(f"Error en la solicitud: Código {respuesta.status_code}")
    
except requests.exceptions.RequestException as e:
    print(f"Error de conexión: {e}")