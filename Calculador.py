from sympy import Symbol
from sympy import sympify
from repositorio import Repositorio

#variables = {0:'x', 1:'y', 2:'z', 3:'k'}
class Calculadora():

    def __init__(self):
        self.funcion = ''
        self.cantVar = 0
        self.count = 0
        self.error = 0
        self.suma = 0
        self.resFinal = 0

    def asignacionVariables(self):
        while (self.cantVar < 2 or self.cantVar > 5):
            self.cantVar = int(input("\nIngrese la cantidad de variables con la que va a trabajar (minimo 2 - maximo 5): "))
        print("\n----ASIGNANDO VARIABLES----")
        if self.cantVar > 0:
            for i in range (int(self.cantVar)):
                variable = input(str("Ingrese la variable: "))
                Repositorio.variables.append(str(Symbol(variable)))
                #Repositorio.variables.append(variable)
            print("\nLas variables ingresadas son: "+ str(Repositorio.variables))
        else:
            self.asignacionVariables()


    def asignacionFuncion(self):
        print("\n----ASIGNANDO FUNCION----")
        while (self.funcion == ''):
            try:
                self.funcion = input(str("\nIngrese la funcion con la que se va a trabajar\n\
                    por ejemplo x**2+3*y: "))
                self.funcion = sympify(self.funcion)
                Repositorio.funcion = self.funcion
            except:
                self.funcion = ''
                print("Ingrese una funcion valida")
        print("\nLa funcion ingresada es: "+str(self.funcion))
        print("\n----ASIGNANDO ERRORES----")
        while (self.error == 0):
            try:
                print("\nIngrese los errores de cada variable")
                self.count = len(Repositorio.variables)
                for i in range(self.count):
                    self.error = float(input("\nIngrese el error relativo de la variable "+str(Repositorio.variables[i]+": ")))
                    Repositorio.errores.append(self.error)
            except:
                print("Ingrese un error valido")
        print("\nLos errores ingresados son: "+str(Repositorio.errores))

    def calculoParciales(self):
        print("\n----CALCULANDO DERIVADAS PARCIALES----")
        self.count = len(Repositorio.variables)
        for i in range(self.count):
            var = Repositorio.variables[i]
            der = Repositorio.funcion.diff(var)
            Repositorio.derParciales.append(der)
            print("\nLa derivada parcial respecto a "+str(Repositorio.variables[i])+" es: "+str(der))

    def asignacionResVariables(self):
        print("\n----ASIGNANDO VALOR A VARIABLES----")
        self.count = len(Repositorio.variables)
        for i in range(self.count):
            valorVariable = float(input("\nIngrese el valor que le quiere dar a la variable "+str(Repositorio.variables[i])+": "))
            Repositorio.valorVariables.append(valorVariable)
        print("\nLos valores ingresados para cada variable son: "+str(Repositorio.valorVariables))
    
    def calculoErrorAbsoluto(self):
        print("\n----CALCULANDO ERROR ABSOLUTO----")
        suma = 0
        self.count = len(Repositorio.variables)
        if self.count == 2:
            for i in range(self.count):
                resultado = Repositorio.derParciales[i].subs([(Repositorio.variables[0], Repositorio.valorVariables[0]), (Repositorio.variables[1],Repositorio.valorVariables[1])])
                Repositorio.resultadoDerivadas.append(resultado)
                suma = suma + (resultado * Repositorio.errores[i])
                print("\nEl valor de la funcion respecto de " +str(Repositorio.variables[i])+ " es: " +str(resultado))
            
            print("\n" +str(Repositorio.resultadoDerivadas))

            print("\nLa suma de derivadas con sus respectivos errores es de: " +str(suma))

            valorFuncion = Repositorio.funcion.subs([(Repositorio.variables[0], Repositorio.valorVariables[0]), (Repositorio.variables[1],Repositorio.valorVariables[1])])
            print("\nEl valor de la funcion es de: " +str(valorFuncion))
            self.resFinal = suma / valorFuncion
            errorAbsProcentual = round(self.resFinal, 5) * 100
            print("\nEl valor del error absoluto es de: " +str(self.resFinal)+"   *100 ---> " +str(errorAbsProcentual)+"%")

        if self.count == 3:
            for i in range(self.count):
                resultado = Repositorio.derParciales[i].subs([(Repositorio.variables[0], Repositorio.valorVariables[0]), (Repositorio.variables[1],Repositorio.valorVariables[1]),
                (Repositorio.variables[2],Repositorio.valorVariables[2])])
                Repositorio.resultadoDerivadas.append(resultado)
                suma = suma + (resultado * Repositorio.errores[i])
                print("\nEl valor de la funcion respecto de " +str(Repositorio.variables[i])+ " es: " +str(resultado))

            print("\n" +str(Repositorio.resultadoDerivadas))

            print("\nLa suma de derivadas con sus respectivos errores es de: " +str(suma))

            valorFuncion = Repositorio.funcion.subs([(Repositorio.variables[0], Repositorio.valorVariables[0]), (Repositorio.variables[1],Repositorio.valorVariables[1]),
            (Repositorio.variables[2],Repositorio.valorVariables[2])])
            print("\nEl valor de la funcion es de: " +str(valorFuncion))
            self.resFinal = suma / valorFuncion
            errorAbsProcentual = round(self.resFinal, 5) * 100
            print("\nEl valor del error absoluto es de: " +str(self.resFinal)+"   *100 ---> " +str(errorAbsProcentual)+"%")

        if self.count == 4:
            for i in range(self.count):
                resultado = Repositorio.derParciales[i].subs([(Repositorio.variables[0], Repositorio.valorVariables[0]), (Repositorio.variables[1],Repositorio.valorVariables[1]),
                (Repositorio.variables[2],Repositorio.valorVariables[2]), (Repositorio.variables[3],Repositorio.valorVariables[3])])
                Repositorio.resultadoDerivadas.append(resultado)
                suma = suma + (resultado * Repositorio.errores[i])
                print("\nEl valor de la funcion respecto de " +str(Repositorio.variables[i])+ " es: " +str(resultado))

            print("\n" +str(Repositorio.resultadoDerivadas))

            print("\nLa suma de derivadas con sus respectivos errores es de: " +str(suma))

            valorFuncion = Repositorio.funcion.subs([(Repositorio.variables[0], Repositorio.valorVariables[0]), (Repositorio.variables[1],Repositorio.valorVariables[1]),
            (Repositorio.variables[2],Repositorio.valorVariables[2]), (Repositorio.variables[3],Repositorio.valorVariables[3])])
            print("\nEl valor de la funcion es de: " +str(valorFuncion))
            self.resFinal = suma / valorFuncion
            errorAbsProcentual = round(self.resFinal, 5) * 100
            print("\nEl valor del error absoluto es de: " +str(self.resFinal)+"   *100 ---> " +str(errorAbsProcentual)+"%")

        if self.count == 5:
            for i in range(self.count):
                resultado = Repositorio.derParciales[i].subs([(Repositorio.variables[0], Repositorio.valorVariables[0]), (Repositorio.variables[1],Repositorio.valorVariables[1]),
                (Repositorio.variables[2],Repositorio.valorVariables[2]), (Repositorio.variables[3],Repositorio.valorVariables[3]),
                (Repositorio.variables[4],Repositorio.valorVariables[4])])
                Repositorio.resultadoDerivadas.append(resultado)
                suma = suma + (resultado * Repositorio.errores[i])
                print("\nEl valor de la funcion respecto de " +str(Repositorio.variables[i])+ " es: " +str(resultado))

            print("\n" +str(Repositorio.resultadoDerivadas))

            print("\nLa suma de derivadas con sus respectivos errores es de: " +str(suma))

            valorFuncion = Repositorio.funcion.subs([(Repositorio.variables[0], Repositorio.valorVariables[0]), (Repositorio.variables[1],Repositorio.valorVariables[1]),
            (Repositorio.variables[2],Repositorio.valorVariables[2]), (Repositorio.variables[3],Repositorio.valorVariables[3]),
            (Repositorio.variables[4],Repositorio.valorVariables[4])])
            print("\nEl valor de la funcion es de: " +str(valorFuncion))
            self.resFinal = suma / valorFuncion
            errorAbsProcentual = round(self.resFinal, 5) * 100
            print("\nEl valor del error absoluto es de: " +str(self.resFinal)+"   *100 ---> " +str(errorAbsProcentual)+"%")

    
    
