from Calculador import Calculadora
from guia import Guia


class Menu():
    def __init__(self):
        pass

    def menuCalculadora(self):
        print("\n  Menu calculadora")
        print("\n--> 1 - Guia de uso")
        print("--> 2 - Asignacion de variables")
        print("--> 3 - Ingresar funcion")
        print("--> 4 - Calcular derivadas parciales")
        print("--> 5 - Asignar valor a las variables")
        print("--> 6 - Calcular error absoluto")
        print("--> 7 - Finalizar")
        return int(input("\n Ingrese un numero para seleccionar una opcion: "))

if __name__ == '__main__':
    menu = Menu()
    bucle = True
    while bucle == True:
        opcion = menu.menuCalculadora()
        if opcion == 1:
            serviceCalculadora = Guia()
            serviceCalculadora.imprimirGuia()
            servicePersona = None
        if opcion == 2:
            serviceCalculadora = Calculadora()
            serviceCalculadora.asignacionVariables()
            servicePersona = None
        if opcion == 3:
            serviceCalculadora = Calculadora()
            serviceCalculadora.asignacionFuncion()
            servicePersona = None
        if opcion == 4:
            serviceCalculadora = Calculadora()
            serviceCalculadora.calculoParciales()
            servicePersona = None
        if opcion == 5:
            serviceCalculadora = Calculadora()
            serviceCalculadora.asignacionResVariables()
            servicePersona = None
        if opcion == 6:
            serviceCalculadora = Calculadora()
            serviceCalculadora.calculoErrorAbsoluto()
            servicePersona = None
        if opcion == 7:
            bucle = False
