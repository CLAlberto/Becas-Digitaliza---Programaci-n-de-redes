#Crear una lista con nombres de persona e incluir, como mínimo, 5 nombres (como mínimo, uno ha de tener la vocal "a")
candidates = ["Alberto","Eulogio","Deivid","Ezequiel","Vergincetorix","Legolas"]

#Crear una lista llamada "selected"
selected = []

#Recorrer, mediante un for, la lista de los nombres e imprimir un texto con el nombre recorrido en dicha iterración. Asimismo, si el nombre de esa iteración contine una "a", añadirlo a la lista llamada "selected"
for e in candidates:
    if "a" in e or "A" in e:
        selected.append(e)


#Finalmente, imprimir por pantalla la lista "selected"
print("Los miembros de la lista selected son:",selected)