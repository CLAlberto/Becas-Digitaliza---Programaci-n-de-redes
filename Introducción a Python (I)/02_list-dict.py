
# Crear una lista que contenga varios strings.
lista_string = ["Freezer","Cell","Boo"]

# Crear una lista que contenga varios integers.
lista_int = [8,16,32]

#Crear una lista que contenga strings, integers y floats.
lista_mix = [3.14,42,"zzzzZ"]

#Crear las sentencias necesarias para imprimir, por pantalla, la información de las listas.
print(lista_string,lista_int,lista_mix)

#Crear 3 sentencias para asignar, en cada una, el último valor de una lista diferente a una variable (es decir, habrá 3 variables, cada una con el último valor de una de las listas).
var1 = lista_string[-1]
var2 = lista_int[-1]
var3 = lista_mix[-1]
#Crear una sentencia para imprimir, por pantalla, un texto, y concatenar la información de las variables.
print(var1,var2,var3)

#Crear un diccionario de vuestras películas/obras favoritas (clave: autor, valor:película)
diccionario = {'Christopher Nolan':'Memento','Michel Gondry':'Olvídate de mi','Jaco Van Dormael':'Mr. Nobody','Richard Schenkman':'The Man from Earth'}

#Crear sentencia para imprimir por pantalla todo el diccionario.
print(diccionario)

#Crear sentencia para imprimir por pantalla sólo las claves del diccionario
print(diccionario.keys())

#Crear sentencia para imprimir por pantalla sólo los valores del diccionario.
print(diccionario.values())

