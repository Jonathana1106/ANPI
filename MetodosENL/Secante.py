# Metodo de la Secante
# Entradas:
            # func: es la funcion a analizar
            # x0: valor iniciar
            # MAXIT: es la cantidad de iteraciones máximas a realizar
            # TOL: es la tolerancia del algoritmo
# Salidas:
            # xAprox: es la solucion, valor aproximado de x
            # error: pocentaje de error del resultado obtenido

########################################################################################
import math
import matplotlib.pyplot as plt
########################################################################################

def secante(func, x0, x1, MAXIT, TOL):
    itera = 2
    err = 1
    iterl = []  # Lista que almacena el numero de iteraciones para despues graficar
    errl = []  # Lista que almacena el % de error de cada iteracion para despues graficar
    xAprox = x0

    while(itera < MAXIT):

        xAprox = x1 - ((x1 - x0)/(func(x1) - func(x0)))  * func(x1)
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

#Grafica
#Entradas:
            #listaValoresX: valores que se graficaran en el eje 'x'
            #listaValoresY: valores que se graficaran en el eje 'y'
#Salidas:
            #Grafico con lo valores ingresados
def grafica(listaValoresX, listaValoresY):
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
    func = lambda x: (math.e)**(-(x**2)) - x
    # Llamado de la funcion
    xAprox, err = secante(func, x0, x1, MAXIT, TOL)
    print('xAprox = {}\n%Error = {}'.format(xAprox, err))