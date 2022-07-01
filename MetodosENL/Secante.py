########################################################################################
import math
import matplotlib.pyplot as plt
########################################################################################


def secante(func, x0, x1, MAXIT, TOL):
    '''
    Metodo de la Secante
    :param func: es la funcion a analizar
    :param x0: valor inicial
    :param x1: valor inicial
    :param MAXIT: es la cantidad de iteraciones máximas a realizar
    :param TOL: es la tolerancia del algoritmo
    :return: xAprox: es la solucion, valor aproximado de x
    :return: error: pocentaje de error del resultado obtenido
    '''
    itera = 2
    err = 1
    iterl = []  # Lista que almacena el numero de iteraciones para despues graficar
    errl = []  # Lista que almacena el % de error de cada iteracion para despues graficar
    xAprox = x0

    while(itera < MAXIT):
        xAprox = x1 - ((x1 - x0)/(func(x1) - func(x0))) * func(x1)
        err = abs(xAprox - x1)/abs(xAprox)
        iterl.append(itera)
        errl.append(err)
        if(err < TOL):
            grafica(iterl, errl)
            return xAprox, err
        else:
            itera = itera + 1
            x0 = x1
            x1 = xAprox
    grafica(iterl, errl)
    return xAprox, err


def grafica(listaValoresX, listaValoresY):
    '''
    Grafica
    :param listaValoresX: valores que se graficaran en el eje 'x'
    :param listaValoresY: valores que se graficaran en el eje 'y'
    :return: Grafico con los valores ingresados
    '''
    plt.plot(listaValoresX, listaValoresY, 'bx')
    plt.title("Metodo de la Secante")
    plt.xlabel("Iteraciones")
    plt.ylabel("% Error")
    plt.show()


if __name__ == '__main__':
    # Valores iniciales
    x0 = 0
    x1 = 1
    # Tolerancia
    TOL = 0.01
    # Maximo iteraciones
    MAXIT = 100
    # Funcion
    def func(x): return (math.e)**(-(x**2)) - x
    # Llamado de la funcion
    xAprox, err = secante(func, x0, x1, MAXIT, TOL)
    print("######################################################")
    print("Metodo de la Secante \n")
    print('xAprox = {}\n%Error = {}'.format(xAprox, err))
