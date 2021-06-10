########################################################################################
import math
import matplotlib.pyplot as plt
########################################################################################


def muller(func, x0, x1, x2, MAXIT, TOL):
    '''
    Metodo de Muller
    :param func: es la funcion a analizar
    :param x0: primer valor inicial
    :param x1: segundo valor inicial
    :param x2: tercer valor inicial
    :param MAXIT: es la cantidad de iteraciones máximas a realizar
    :param TOL: es la tolerancia del algoritmo
    :return: r: es la solucion, valor aproximado de x
    :return: error: pocentaje de error del resultado obtenido
    '''
    itera = 1
    err = 1
    iterl = []  # Lista que almacena el numero de iteraciones para despues graficar
    errl = []  # Lista que almacena el % de error de cada iteracion para despues graficar
    while(itera < MAXIT):
        divisor = ((x0 - x1) * (x0 - x2) * (x1 - x2))
        frac1a = (float(x1) - float(x2)) * (float(func(x0)) - float(func(x2)))
        frac2a = (float(x0) - float(x2)) * (float(func(x1)) - float(func(x2)))
        frac1b = ((float(x0) - float(x2))**2) * \
            (float(func(x1)) - float(func(x2)))
        frac2b = ((float(x1) - float(x2))**2) * \
            (float(func(x0)) - float(func(x2)))
        a = (frac1a - frac2a) / (divisor)
        b = (frac1b - frac2b) / (divisor)
        c = func(x2)
        discriminante = b**2 - 4 * a * c
        if(discriminante < 0):
            raise ValueError("La solucion no es real.")
        r = x2 - (2 * c) / (b + (math.sin(b)) * (math.sqrt(discriminante)))
        err = (abs(r - x2)) / (abs(r))
        errl.append(err)
        iterl.append(itera)
        itera = itera + 1
        if(err < TOL):
            grafica(iterl, errl)
            return r, err
        x0Dist = abs(r - x0)
        x1Dist = abs(r - x1)
        x2Dist = abs(r - x2)
        if (x0Dist > x2Dist and x0Dist > x1Dist):
            x0 = x2
        elif (x1Dist > x2Dist and x1Dist > x0Dist):
            x1 = x2
        x2 = r
    grafica(iterl, errl)
    return r, err


def grafica(listaValoresX, listaValoresY):
    '''
    Grafica
    :param listaValoresX: valores que se graficaran en el eje 'x'
    :param listaValoresY: valores que se graficaran en el eje 'y'
    :return: Grafico con los valores ingresados
    '''
    plt.plot(listaValoresX, listaValoresY, 'bx')
    plt.title("Metodo de Muller")
    plt.xlabel("Iteraciones")
    plt.ylabel("% Error")
    plt.show()


if __name__ == '__main__':
    # Valores iniciales
    x0 = 2
    x1 = 2.2
    x2 = 1.8
    # Tolerancia
    TOL = 0.0000001
    # Maximo iteraciones
    MAXIT = 100
    # Funcion
    def func(x): return math.sin(x) - x/2
    # Llamado de la funcion
    r, err = muller(func, x0, x1, x2, MAXIT, TOL)
    print("######################################################")
    print("Metodo de Muller \n")
    print('xAprox = {}\nIteraciones = {}'.format(r, err))
