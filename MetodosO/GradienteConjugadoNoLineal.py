# Metodo del Gradiente Conjugado No Lineal
# Entradas:
            #func: string con la funcion a evaluar
            #vars: lista con las variables de la ecuacion
            #xk: vector con los valores iniciales
            #MAXIT: es la cantidad de iteraciones maximas a realizar
            #TOL: es la tolerancia del algoritmo
            #regla_bk: metodo seleccionado para calcular el Bk
# Salidas:
            #xAprox: es la solucion, valor aproximado de x
            #error: pocentaje de error del resultado obtenido

###############################################################################
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative
from sympy import sympify, Symbol, diff
from numpy import linalg, array
###############################################################################

def gradienteConjugadoNoLineal(func, variables, xk, MAXIT, TOL, reglaBK):
    funcion = sympify(func) #Convertir el string a una expresion matematica
    itera = 0
    iterl = []
    errl = []

    if(len(variables) != len(xk)):
        return "La lista de varables debe ser del mismo tamano que el vector de valores iniciales."

    elif(reglaBK != 'FR' and reglaBK != 'DC' and reglaBK != 'DY'):
        return "El parametro regla_bk debe ser FR, DC o DY."

    listaSimb = []
    n = len(variables)
    for i in range(0, n):
        listaSimb += [Symbol(variables[i])] #Hacer que 'x' 'y' sea variables matematicas y no solo string

    gradiente = []
    for i in range(0, n):
        gradiente += [diff(funcion, variables[i])]

    gk = evaluarGradiente(gradiente, variables, xk)
    dk = [i * -1 for i in gk]

    while(itera < MAXIT):
        ak = calcularAlphaK(funcion, variables, xk, dk, gk)

        alphakdk = [i * ak for i in dk]

        vecx = [x1 + x2 for(x1, x2) in zip(xk, alphakdk)]

        gkx = evaluarGradiente(gradiente, variables, vecx)

        vecFinal = evaluarGradiente(gradiente, variables, vecx)

        norma = linalg.norm(array(vecFinal, dtype='float'), 2)
        iterl.append(itera)
        errl.append(norma)
        if(norma < TOL):
            break

        bk = calcularBetaK(gkx, gk, dk, reglaBK)

        betakdk = [i * bk for i in dk]
        mgk = [i * -1 for i in gkx]

        '''
        Para cada elemento en mgk y en betakdk realizar la suma de esos elementos
        siempre y cuando no se salgan del rango maximo de elementos de cada uno
        '''
        dk = [x1 + x2 for (x1, x2) in zip(mgk, betakdk)]

        xk = vecx.copy()
        gk = gkx.copy()
        itera += 1
    grafica(iterl, errl)
    return vecx, norma

# Evaluar Gradiente
# Entradas:
            #gradiente: gradiente a evaluar
            #vars: lista con las variables de la ecuacion
            #xk: vector con los valores iniciales
# Salidas:
            #gradResult: resultado de evaluar el vector en el gradiente
def evaluarGradiente(gradiente, variables, xk):
    n = len(variables)
    gradResult = []

    for i in range(0, n):
        funcion = gradiente[i]

        for j in range(0, n):
            funcion = funcion.subs(variables[j], xk[j])

        gradResult += [funcion.doit()] #Decrile que evalue lo que no se ha evaluado

    return gradResult

# Calcular alpha k
# Entradas:
            #gradiente: gradiente a evaluar
            #vars: lista con las variables de la ecuacion
            #xk: vector con los valores iniciales
# Salidas:
            #gradResult: resultado de evaluar el vector en el gradiente
def calcularAlphaK(func, variables, xk, dk, gk):
    a = 1
    while 1:
        adk = [i * a for i in dk]

        vecadk = [x1 + x2 for (x1, x2) in zip(xk, adk)]

        refvecadk = evaluarFuncion(func, variables, vecadk)
        refvec = evaluarFuncion(func, variables, xk)

        izquierdaDesigualdad = refvecadk - refvec
        multiplicargkdk = [x1 * x2 for(x1, x2) in zip(gk, dk)]
        sumagkdk = sum(multiplicargkdk)
        derechaDesigualdad =  0.5 * a * sumagkdk

        if(izquierdaDesigualdad < derechaDesigualdad):
            break;
        a /= 2
    return a

# Evaluar en la funcion
# Entradas:
            #func: string con la funcion a evaluar
            #vars: lista con las variables de la ecuacion
            #xk: vector con los valores iniciales
# Salidas:
            #func: resultado de evaluar en la funcion
def evaluarFuncion(func, variables, xk):
    n = len(variables)

    for i in range(0, n):
        func = func.subs(variables[i], xk[i])

    return func

# Calcular beta k
# Entradas:
            #gk: vector gk
            #prevGK: vector gk de la iteracion anterior
            #dk: vector dk
            #reglaBK: regla utilizada para calcular el BK
# Salidas:
            #b: valor del Bk canculado
def calcularBetaK(gk, prevGK, dk, reglaBK):

    normagk = linalg.norm(array(gk, dtype='float'), 2)

    if(reglaBK == 'FR'):
        normaprevGK = linalg.norm(array(prevGK, dtype='float'), 2)
        b = (pow(normagk, 2)) / (pow(normaprevGK, 2))
        return b
    elif(reglaBK == 'CD'):
        mdk = [i * -1 for i in dk]
        dkgk = [x1 * x2 for(x1, x2) in zip(prevGK, mdk)]
        suma = sum(dkgk)
        b = (pow(normagk, 2))/(suma)
        return b
    elif(reglaBK == 'DY'):
        yk = [x1 - x2 for(x1, x2) in zip(gk, prevGK)]
        dkyk = [x1 * x2 for (x1, x2) in zip(dk, yk)]
        suma = sum(dkyk)
        b = (pow(normagk, 2))/(suma)
        return b
    else:
        return "No se ha ingresado un metodo valido para Bk"

#Grafica
#Entradas:
            #listaValoresX: valores que se graficaran en el eje 'x'
            #listaValoresY: valores que se graficaran en el eje 'y'
#Salidas:
            #Grafico con lo valores ingresados
def grafica(listaValoresX, listaValoresY):
    plt.plot(listaValoresX, listaValoresY, 'bx')
    plt.title("Metodo del Gradiente Conjugado No Lineal")
    plt.xlabel("Iteraciones")
    plt.ylabel("% Error")
    plt.show()

if __name__ == '__main__':
    #Valores iniciales
    xk = [0, 3]
    # Variables de la ecuacion
    variables = ['x', 'y']
    #Tolerancia
    TOL = 0.00001
    #Maximo iteraciones
    MAXIT = 14
    #Funcion
    func = '(x-2)**4 + (x-2*y)**2'
    #Llamado de la funcion
    xAprox, err = gradienteConjugadoNoLineal(func, variables, xk, MAXIT, TOL, 'FR')
    print("######################################################")
    print("Metodo del Gradiente Conjugado No Lineal \n")
    #print(gradienteConjugadoNoLineal(func, variables, xk, MAXIT, TOL, 'FR'))
    print('xAprox = {}\n%Error = {}'.format(xAprox, err))