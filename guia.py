class Guia():
    def __init__(self):
        pass

    def imprimirGuia(self):
        print(
            """
            ------ GUIA DE USO ------

Para utilizar el programa debe abrir el archivo "main.py" y ejecutarlo, al hacerlo se deplegara un
menu con el cual se puede interactuar. 

En la seccion de asignacion de variables debe ingresar con las variables con las que se va a trabajar
por ejemplo: (x, y, p, D, d)

Luego cuando ingrese la funcion debe hacerlo respetando las mismas variables que ingreso anteriormente.
Para el ingreso de la funcion se tiene en cuenta la siguiente notacion:
-------------------

* -> multiplicacion
** -> exponente
+ -> suma
- -> resta
/ -> division
cos() -> coseno
sin() -> seno

-------------------

ejemplo : 1/6*x*y**3

Al calcular las derivadas parciales se calculara la derivada respecto cada variable y sera mostrara

Cuando solicite ingresar el valor para las variables se ingresa que valor quiere que tome cada una

Por ultimo calcula el error absoluto

Si desea finalizar el programa puede hacerlo ingresando el N° 7

            ------------------------
"""
        )