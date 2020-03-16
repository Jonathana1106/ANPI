#Metodo de la Biseccion
#Entradas:
            #func: es la funcion a analizar
            #a: es "a" valor inferior en el intervalo de la funcion [a, b]
            #b: es "b" valor superior en el intervalo de la funcion [a, b]
            #tol: es la tolerancia del algoritmo
#Salidas:
            #xAprox: es la solucion, valor aproximado de x
            #_iter: es el numero de iteraciones

import math
import matplotlib.pyplot

def bisection(func, a, b, tol):
    aprox = []
    it =[]
    # Validar la condicion para encontrar el cero
    if (func(a) * func(b) < 0):
        # Valor inicial de x
        xAprox = (a + b) / 2
        _iter = 0

        # Repetir hasta que el x se acerque al cero
        while (abs(func(xAprox)) > tol):
            # Verificar cual es el nuevo intervalo de la funcion
            if (func(a) * func(xAprox) < 0):
                b = xAprox
            else:
                a = xAprox

            # Actualizar el valor de x y de las iteraciones
            xAprox = (a + b) / 2
            aprox.append(xAprox)
            _iter += 1
            it.append(_iter)
    else:
        raise ValueError("Las condiciones no garantizan el cero de la función")
    matplotlib.pyplot.plot(xAprox, _iter)
    return xAprox, _iter

# Prueba
if __name__ == '__main__':
    # Limites
    a = 0
    b = 2
    # Tolerancia
    tol = 0.1
    # Funcion a la cual se le aplicara el metodo
    func = lambda x: math.e**x - x - 2
    # Llamado de la funcion
    xAprox, _iter = bisection(func, a, b, tol)
    print('xAprox = {}\nIteraciones = {}'.format(xAprox, _iter))
