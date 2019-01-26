#Crear un script en el que guardéis en una variable un número
x = int(input("Introduce un número: "))

#Controlar el tamaño del número en 4 rangos (menor de 20, entre 20 y 39, entre 40 y 59, mayor de 60)
#En cada uno de los casos imprimir por pantalla el número que se haya introducido.
if x >= 60:
    print('el número introducido es igual o mayor que 60')
elif x > 39:
    print('el número introducido está entre 40 y 59')
elif x > 19:
    print('el número introducido está entre 20 y 39')
else:
    print('el número introducido es menor de 20')