"""Tarea 1: Crear una APP para la salida y puesta del sol

Crear una aplicación para acceder a la API de las horas de salida y puesta del sol de la siguiente URL:

https://api.sunrise-sunset.org/json?lat=48.8584&lng=2.2945 (Enlaces a un sitio externo.)Enlaces a un sitio externo.
En el ejemplo, se calcula para París, Francia.

Crear un archivo llamado: sunsetSunrise.py
Mostrar las horas para una latitud y longitud concretas (que no sea la del ejemplo; por ejemplo, donde vivís). Incluir un print con texto (lo que queráis), con los valores de latitud y longitud, y con las horas obtenidas.
Subir el archivo a vuestro repositorio en GitHub."""

import requests
print("Calculo de la salida y puesta del sol dependiendo de la localización")
geocode_location = input("Introduce el pueblo, ciudad o pais a calcular:")
geocode_url = "http://open.mapquestapi.com/geocoding/v1/address"

geocode_querystring = {"key":"iBL788R2Cz0miic5kAoMmNS8bC9eFwOt","location":geocode_location}
geocode_json_data = requests.request("GET", geocode_url,params=geocode_querystring).json()

url = "https://api.sunrise-sunset.org/json"

querystring = {"lat":geocode_json_data["results"][0]["locations"][0]["latLng"]["lat"],"lng":geocode_json_data["results"][0]["locations"][0]["latLng"]["lng"]}

json_data = requests.request("GET", url, params=querystring).json()
print("----------------------------------")
print("Para",geocode_location, "con latitud y longitud" ,list(querystring.values()), "se ha calculado que:","\nLa salida del sol será a las:",json_data['results']['sunrise'],"\nLa puesta de sol será a las:",json_data['results']['sunset'])
print("----------------------------------")

