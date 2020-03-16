#Metodo de la Secante
#Entradas:
    #func: es la funcion a analizar
    #xk_1: valor inicial en la iteracion 0
    #xk: valor inicial en la iteracion 1
    #tol: es la tolerancia del algoritmo
#Salidas:
    #xk: es la solucion, valor aproximado de x
    #_iter: es el numero de iteraciones

import math

def secant(func, xk_1, xk, tol):
    _iter = 1

    # Repetir hasta que x el error sea mas pequeno que la tolerancia
    while (abs(xk - xk_1) / abs(xk)) > tol:
        # Nuevo valor de x
        xTemp = xk - (xk - xk_1) / (func(xk) - func(xk_1)) * func(xk)
        # Actualizar el valor anterior y el valor actual
        xk_1 = xk
        xk = xTemp
        # Actualizar las iteraciones
        _iter += 1

    return xk, _iter

# Prueba
if __name__ == '__main__':
    # Valores iniciales
    x0 = 0
    x1 = 1
    # Tolerancia
    tol = 0.01
    # Funcion a la cual se le aplica el metodo
    func = lambda x: math.e**(-x**2) - x
    # Llamado de la funcion
    xk, _iter = secant(func, x0, x1, tol)
    print('xk = {}\nIteraciones = {}'.format(xk, _iter))
