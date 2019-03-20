"""Tarea 2: Crear una APP para el ISS (International Space Station)

Crear un archivo llamado: numberPeopleSpace.py
Crear una app para saber el número de personas que hay en el espacio. Podéis buscar la información en la siguiente URL:
http://open-notify.org/Open-Notify-API/ (Links to an external site.)Links to an external site.
Subir el archivo a vuestro repositorio en GitHub."""
import requests
pregunta = (input("¿Quieres saber el número de personas que hay actualmente en el espacio?"))
pregunta = pregunta.lower()
if "s" in pregunta:
    url = "http://api.open-notify.org/astros.json"
    json_data = requests.request("GET", url).json()
    print("El número de personas que actualmente hay en el espacio son:",json_data["number"])
else:
    print("ok, de acuerdo, hasta luego!")



