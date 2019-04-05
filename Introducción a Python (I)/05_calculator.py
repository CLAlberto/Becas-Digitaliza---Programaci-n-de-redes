class Calculadora:
    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b

    def Suma(self):
        print("El resultado de sumar", self.firstnumber, "+", self.secondnumber, "es igual a:",
              (self.firstnumber + self.secondnumber),"\n",self.firstnumber,"+",self.secondnumber,"=",(self.firstnumber + self.secondnumber))

    def Resta(self):
        print("El resultado de restar", self.firstnumber, "-", self.secondnumber, "es igual a:",
              (self.firstnumber - self.secondnumber),"\n",self.firstnumber,"-",self.secondnumber,"=",(self.firstnumber - self.secondnumber))

    def Multiplicacion(self):
        print("El resultado de multiplicar", self.firstnumber, "*", self.secondnumber, "es igual a:",
              (self.firstnumber * self.secondnumber),"\n",self.firstnumber,"*",self.secondnumber,"=",(self.firstnumber * self.secondnumber))

    def Division(self):
        try:
            print("El resultado de dividir", self.firstnumber, "/", self.secondnumber, "es igual a:",
                  (self.firstnumber / self.secondnumber),"\n",self.firstnumber,"/",self.secondnumber,"=",(self.firstnumber/self.secondnumber))
        except Exception:
            print(("No se puede dividir entre cero!\n"))

    def Exponencial(self):
        print("El resultado de elevar", self.firstnumber, "^", self.secondnumber, "es igual a:",
              (self.firstnumber ** self.secondnumber),"\n",self.firstnumber,"^",self.secondnumber,"=",(self.firstnumber**self.secondnumber))


print("--------------------\nOperaciones a realizar\n--------------------\n1 - Sumar\n2 - Restar\n3 - Multiplicar\n4 - Dividir\n5 - Exponencial\n--------------------")
while True:
    try:
        opcion = int(input("Seleccione operacion: "))
        assert 0 < opcion < 6
    except ValueError:
        print("No es un número entero! Por favor introduce un número entero.")
    except AssertionError:
        print("Por favor, introduce un número entero entre el 1 y el 5 (incluidos)")
    else:
        break

while True:
    try:
        primero = float(input("Inserta un Numero: "))
    except ValueError:
        print("Parece que no ha introducido un número correcto! Por favor introduce un número correcto (entero o decimal)")
    else:
        break

while True:
    try:
        segundo = float(input("Inserta otro Numero: "))
    except ValueError:
        print("Parece que no ha introducido un número correcto! Por favor introduce un número correcto (entero o decimal)")
    else:
        break
Objeto = Calculadora(primero, segundo)

operaciones = {
    1: Objeto.Suma,
    2: Objeto.Resta,
    3: Objeto.Multiplicacion,
    4: Objeto.Division,
    5: Objeto.Exponencial
}

print("--------------------\n")
operaciones[opcion]()