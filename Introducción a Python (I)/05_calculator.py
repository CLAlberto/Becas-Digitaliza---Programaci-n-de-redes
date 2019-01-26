#Crear las sentencias necesarias para recoger dos números a través del terminal


#Integrar funcionalidades de suma, multiplicación, división, y exponencial
salir=False
while salir!=True:
    print("------------\n1) SUMAR\n2) MULTIPLICAR\n3) DIVIDIR\n4) POTENCIA\n5) SALIR\n------------\n")
    opcion = int(input("Ingrese el número de su opcion:"))
    if opcion > 0 and opcion < 6:
        if opcion < 5:
            a = int(input("Introduce el primer número para la operación a calcular: "))
            b = int(input("Introduce el segundo número para la operación a calcular: "))
            if opcion == 1:
                sumar = a + b
                print("El resultado de sumar",a,"+",b,"es igual a: ",sumar)
            elif opcion == 2:
                multiplicar = a * b
                print("El resultado de multiplicar", a, "*", b, "es igual a: ", multiplicar)
            elif opcion == 3:
                dividir = a / b
                print("El resultado de dividir", a, "/", b, "es igual a: ", dividir)
            elif opcion == 4:
                potencia = a ** b
                print("El resultado de elevar", a, "^", b, "es igual a: ", potencia)

        else:
            print("------------\nGracias por usar la calculadora.\nHasta luego!\n------------\n")
            salir=True
#Permitir escoger el modo de operación de forma manual (el usuario ha de introducir un número para que sepa qué operación realizar)


#Realizar las operaciones e imprimir el valor por pantalla.