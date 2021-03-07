#Metodo de la Biseccion
#Entradas:
            #func: es la funcion a analizar
            #a: es "a" valor inferior en el intervalo de la funcion en el rango [a, b]
            #b: es "b" valor superior en el intervalo de la funcion en el rango [a, b]
            #MAXIT: es la cantidad de iteraciones máximas a realizar
            #TOL: es la tolerancia del algoritmo
#Salidas:
            #xAprox: es la solucion, valor aproximado de x
            #error: pocentaje de error del resultado obtenido

########################################################################################
import math
import matplotlib.pyplot as plt
########################################################################################

def biseccion(func, a, b, MAXIT, TOL):

    if(func(a) * func(b) < 0):
        itera = 1
        err = 1
        iterl = [] # Lista que almacena el numero de iteraciones para despues graficar
        errl = [] # Lista que almacena el % de error de cada iteracion para despues graficar

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

#Grafica
#Entradas:
            #listaValoresX: valores que se graficaran en el eje 'x'
            #listaValoresY: valores que se graficaran en el eje 'y'
#Salidas:
            #Grafico con lo valores ingresados
def grafica(listaValoresX, listaValoresY):
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
    #print(xAprox)
    print('xAprox = {}\n%Error = {}'.format(xAprox, err))