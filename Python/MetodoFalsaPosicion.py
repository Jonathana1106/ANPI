#Metodo de la Falsa Posicion
#Entradas
    #a: limite inferior del intervalo
    #b: limite superior del intervalo
    #tol: tolerencia del algoritmo
    #f: funcion a la cual se le aplicara el algoritmo
#Salidas
    #xk: valor aproximado de x
    #_iter: iteraciones necesarias para aproximar x

import math

def falsePosition(a, b, tol, f):
    
    # Validar la condicion para encontrar el cero
    if (f(a) * f(b) < 0):
        # Valor inicial de x_k y x_{k-1}
        xk_1 = b
        xk = b - (b - a) / (f(b) - f(a)) * f(b)
        _iter = 2

        # Repetir hasta que el x se acerque al cero
        while (abs((xk - xk_1) / xk)) > tol:
            # Verificar cual es el nuevo intervalo de la funcion
            # y el valor de ck
            if (f(a) * f(xk) < 0):
                b = xk
                ck = a
            else:
                a = xk
                ck = b

            # Calcular el nuevo valor con el metodo de la secante
            xAprox = xk - (xk - ck) / (f(xk) - f(ck)) * f(xk)
            xk_1 = xk
            xk = xAprox
            _iter += 1;
    else:
        raise ValueError("Condiciones no garantizan el cero de la función")

    return xk, _iter

#Prueba
if __name__ == '__main__':
    # Limites
    a = 0.5
    b = math.pi / 4
    # Tolerancia
    tol = 0.00001
    # Funcion a la cual se le aplicara el metodo
    func = lambda x: math.cos(x) - x
    # Llamado de la funcion
    xk, _iter = falsePosition(a, b, tol, func)
    print('xk = {}\nIteraciones = {}'.format(xk, _iter))
