########################################################################################
import math
import matplotlib.pyplot as plt
########################################################################################

def biseccion(func, a, b, MAXIT, TOL):
    '''
    Metodo de la Biseccion
    :param func: es la funcion a analizar
    :param a: es "a" valor inferior en el intervalo de la funcion en el rango [a, b]
    :param b: es "b" valor superior en el intervalo de la funcion en el rango [a, b]
    :param MAXIT: es la cantidad de iteraciones máximas a realizar
    :param TOL: es la tolerancia del algoritmo
    :return: xAprox: es la solucion, valor aproximado de x
    :return: error: pocentaje de error del resultado obtenido
    '''
    if(func(a) * func(b) < 0):
        itera = 1
        err = 1
        iterl = [] #Lista que almacena el numero de iteraciones para despues graficar
        errl = [] #Lista que almacena el % de error de cada iteracion para despues graficar

        while(itera < MAXIT):
            xAprox = (a + b) / 2
            fx = func(xAprox)

            if(func(a) * fx  < 0):
                b = xAprox
            elif(func(b) * fx < 0):
                a = xAprox

            iterl.append(itera)
            errl.append(err)
            itera = itera + 1
            err = (b - a) / (2)**(itera-1)

            if(err < TOL):
                grafica(iterl, errl)
                return xAprox, err
        grafica(iterl, errl)
        return xAprox, err
    else:
        raise ValueError("Las condiciones  no garantizan el cero de la funcion.")

def grafica(listaValoresX, listaValoresY):
    '''
    Grafica
    :param listaValoresX: valores que se graficaran en el eje 'x'
    :param listaValoresY: valores que se graficaran en el eje 'y'
    :return: Grafico con los valores ingresados
    '''
    plt.plot(listaValoresX, listaValoresY, 'bx')
    plt.title("Metodo de la Biseccion")
    plt.xlabel("Iteraciones")
    plt.ylabel("% Error")
    plt.show()

if __name__ == '__main__':
    #Intervalos
    a = 0
    b = 2
    #Tolerancia
    TOL = 0.0001
    #Maximo iteraciones
    MAXIT = 100
    #Funcion
    func = lambda x: math.e**x - x - 2
    #Llamado de la funcion
    xAprox, err = biseccion(func, a, b, MAXIT, TOL)
    print("######################################################")
    print("Metodo de la Biseccion\n")
    print('xAprox = {}\n%Error = {}'.format(xAprox, err))