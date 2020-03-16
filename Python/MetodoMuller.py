#Metodo de Muller
#Entradas:
    #f: es la funcion a analizar
    #x0: valor inicial
    #x1: valor inicial
    #x2: valor inicial
    #_iter: iteracion inicial
    #maxIter: numero de iteraciones maximas
#Salidas:
    #r: es la solucion, valor aproximado de x
    #_iter: es el numero de iteraciones


import math
import numpy as np

def muller(f, x0, x1, x2, _iter, maxIter):
    # Si aun no llega al numero maximo de iteraciones
    if (_iter < maxIter):
        div = ((x0 - x2) * (x1 - x2) * (x0 - x1))
        print("div: ", div)
        # Si para calcular a y b la divisiones no son cero
        if (div == 0):
            print("Error: Division por cero")
            return x2, _iter
        # Entonces porcede a calcular a, b y c
        else:
            a = ((((x1 - x2)*(f(x0) - f(x2)) - (x0 - x2)*(f(x1) - f(x2))) / div))
            print("a: ", a)
            b = ((((x0 - x2)**2)*(f(x1) - f(x2)) - ((x1 - x2)**2)*(f(x0) - f(x2))) / (div))
            print("b: ", b)
            c = f(x2)
            print("c: ", c)
            disc = ((pow(b,2)) - (4*a*c))
            print("disc: ", disc)

            # Si el discriminante es menor que cero
            if(disc < 0):
                print("Error: No hay solucion real")
                return x2, _iter
            # Si no entonces procede a calcular el valor de r
            else:
                div2 = b + b*(math.sqrt(abs(disc)))
                r = x2 - ((2*c) / (div2))
                print("r: ", r)
                _iter += 1
                return muller(f, x1, x2, r, _iter, maxIter)
    else:
        return x2, _iter

#Prueba

if __name__ == '__main__':
    # Valores iniciales
    x0 = 2
    x1 = 2.2
    x2 = 1.8
    # Iteraciones
    _iter = 0
    maxIter = 50
    #Funcion a la cual se le aplica el metodo
    func = lambda x: (np.sin(x)) - (x/2)
    # Llamado de la funcion
    r, _iter = muller(func, x0, x1, x2, _iter, maxIter)
    print('r = {}\nIteraciones = {}'.format(r, _iter))
