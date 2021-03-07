# Metodo de la Falsa Posicion
# Entradas:
            # func: es la funcion a analizar
            # x0: primer valor inicial
            # x1: segundo valor inicial
            # MAXIT: es la cantidad de iteraciones máximas a realizar
            # TOL: es la tolerancia del algoritmo
# Salidas:
            # xAprox: es la solucion, valor aproximado de x
            # error: pocentaje de error del resultado obtenido

########################################################################################
import math
import matplotlib.pyplot as plt
########################################################################################

def falsaPosicion(func, x0, x1, MAXIT, TOL):
    a = x0
    b = x1

    if (func(a) * func(b) < 0):
        itera = 0
        err = 1
        iterl = []  # Lista que almacena el numero de iteraciones para despues graficar
        errl = []  # Lista que almacena el % de error de cada iteracion para despues graficar
        xAprox = 0

        x2 = x1 - ((x1 - x0) / (func(x1) - func(x0))) * func(x1)

        if (func(a) * func(x2) < 0):

            while (itera < MAXIT):
                xAprox = x2 - ((x2 - a) / (func(x2) - func(a))) * func(x2)
                err = (abs(xAprox - x2)) / (abs(xAprox))
                iterl.append(itera)
                errl.append(err)

                if (err < TOL):
                    grafica(iterl, errl)
                    return xAprox, err
                else:
                    itera = itera + 1
                    a = x2
                    x2 = xAprox

            grafica(iterl, errl)
            return xAprox, err

        elif (func(x2) * func(b) < 0):

            while (itera < MAXIT):
                xAprox = b - ((b - x2) / (func(b) - func(x2))) * func(b)
                err = (abs(xAprox - b)) / (abs(xAprox))
                iterl.append(itera)
                errl.append(err)

                if (err < TOL):
                    grafica(iterl, errl)
                    return xAprox, err
                else:
                    itera = itera + 1
                    x2 = b
                    b = xAprox

            grafica(iterl, errl)
            return xAprox, err
        else:
            raise ValueError("Las condiciones no garantizan el cero de la funcion")
    else:
        raise ValueError("Las condiciones no garantizan el cero de la funcion")

def grafica(listaValoresX, listaValoresY):
    plt.plot(listaValoresX, listaValoresY, 'bx')
    plt.title("Metodo de la Falsa Posicion")
    plt.xlabel("Iteraciones")
    plt.ylabel("% Error")
    plt.show()

if __name__ == '__main__':
    # Intervalos
    x0 = 1 / 2
    x1 = (math.pi) / 4
    # Tolerancia
    TOL = 0.00001
    # Maximo iteraciones
    MAXIT = 100
    # Funcion
    func = lambda x: math.cos(x) - x
    # Llamado de la funcion
    xAprox, err = falsaPosicion(func, x0, x1, MAXIT, TOL)
    print('xAprox = {}\n%Error = {}'.format(xAprox, err))