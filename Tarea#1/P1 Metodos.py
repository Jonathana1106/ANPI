from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import math

def isBolsano(a, b, func): #Funcion que verifica si cumple con el teorema de Bolzano o no

    f = lambda x: eval(func, {'x': x, 'pi': np.pi, 'e': np.e,
                              'exp': exp, 'sqrt': sqrt,
                              'arccos': acos, 'sin': sin, 'tan': tan, 
                              'ln': np.log,
                              'log10': np.log10})  
    
    fa = f(a)
    fb = f(b)

    return (fa * fb <= 0)

def biseccion(f, a, b, tol):
    
    #Inicializacion de la variable i que cuenta las iteraciones y x que es la aproximacion 
    
    i = 0
    x = 0
    
    if (isBolsano(a, b, f)):
        
        #Si cumple con el teorema el metodo continúa ejecutandose
        itArray = []
        errArray = []
        tempA = a
        tempB = b
        e = (b - a) / 2
        while (e >= tol):
            
            #Mientras no haya alcanzado el margen de error sigue dividiendo los intervalos que cumplan  con el teorema
            
            x = (tempA + tempB) / 2
            if(isBolsano(x, tempB, f)):
                tempA = x
            elif(isBolsano(tempA, x, f)):
                tempB = x
            i = i + 1
            e = (b - a) / (2**i)
            itArray.append(i)
            errArray.append(e)


    plt.plot(itArray,errArray)
    plt.ylabel('Errores')
    plt.xlabel('Iteraciones')

    plt.show()
        
    return i, x, e


#biseccion("((log10(7/x)/((1/10)*ln(10)))+(x*(6-x)/(((2*10**2*arccos(x/20)-x*sqrt(10**2-(x**2/4)))**2/(2*(40/ln(10))**2))*((1/(20**2*arccos(x/20)-x*sqrt(10**2-(x**2/4))))+(1/pi*10**2)))))", 1, 19, 10**(-10))


def secante(function, x0, x1, tol):

    f = lambda x: eval(function,  {'x': x, 'pi': np.pi, 'e': np.e,
                                                      'exp': exp, 'sqrt': sqrt,
                                      'arccos': acos, 'sin': sin, 'tan': tan, 
                                              'ln': np.log, 'log10': math.log10})

    #Número de iteraciones y arreglos de iteraciones inician en cero y vacios
    iterations = 0
    itArray = []
    errArray = []

    while(abs(f(x1)) >= tol):

        #Calcula la aproximacion y reacsigna los nuevos valores a x0 y x1
        x = x1 - f(x1)*((x1 - x0) / (f(x1) - f(x0)))
        x0 = x1
        x1 = x

        #Incrementa el número de iteraciones
        iterations += 1
        itArray.append(iterations)
        errArray.append(abs(f(x1)))

    #Grafica
    plt.plot(itArray,errArray)
    plt.ylabel('Errores')
    plt.xlabel('Iteraciones')

    plt.show()
    return [x1, iterations, abs(f(x1))]
    


#secante("((log10(7/x)/((1/10)*ln(10)))+(x*(6-x)/(((2*10**2*arccos(x/20)-x*sqrt(10**2-(x**2/4)))**2/(2*(40/ln(10))**2))*((1/(20**2*arccos(x/20)-x*sqrt(10**2-(x**2/4))))+(1/pi*10**2)))))", 5, 10, 10**(-10))

def falsaPosicion(function, x0, x1, tol):

    f = lambda x: eval(function,  {'x': x, 'pi': np.pi, 'e': np.e,
                                                      'exp': exp, 'sqrt': sqrt,
                                      'arccos': acos, 'sin': sin, 'tan': tan, 
                                              'ln': np.log, 'log10': math.log10})
    itArray = []
    errArray = []
    
    #Revisa si cumple el teorema de Bolzano
    if(f(x0)*f(x1) <= 0):

        iterations = 0
        xn = x1

        while(abs(f(xn)) >= tol):

            #Calcula la siguiente aproximacion
            xn = x1 - f(x1)*((x1 - x0) / (f(x1) - f(x0)))
            
            #Escoge el nuevo subintervalo para la siguiente aproximación
            if(f(x0)*f(xn)):
                x1 = xn
            else:
                x0 = xn

            #Incrementa el numero de iteraciones
            iterations += 1
            itArray.append(iterations)
            errArray.append(abs(f(xn)))

    #Grafica
    plt.plot(itArray,errArray)
    plt.ylabel('Errores')
    plt.xlabel('Iteraciones')

    plt.show()

    return [xn, iterations, abs(f(xn))]


#falsaPosicion("((log10(7/x)/((1/10)*ln(10)))+(x*(6-x)/(((2*10**2*arccos(x/20)-x*sqrt(10**2-(x**2/4)))**2/(2*(40/ln(10))**2))*((1/(20**2*arccos(x/20)-x*sqrt(10**2-(x**2/4))))+(1/pi*10**2)))))", 0.1, 19, 10**(-10))

def ssm(func,xo,tol):

    
    f = lambda x: eval(func, {'x': x, 'pi': np.pi, 'e': np.e,
                                  'exp': exp, 'sqrt': sqrt,
                                  'arccos': acos, 'sin': sin, 'tan': tan, 
                                  'ln': np.log, 'log10': math.log10})

     #Las iteraciones inician en cero y los arreglos de iteraciones en vacio   
    xC = xo
    itera = 0
    error = [ ]
    iteracion = [ ]
    tempTol = 1

    #Condicion de parada
    while(tempTol >= tol):

        itera += 1

        fx = f(xC)
        z = f(xC +fx)
            
        y = xC - ((fx**2)/(z-fx))
        fy = f(y)

        #Calculo de la nueva aproximacion
        xAprox = xC - (fx**3)/((z-fx)*(fx-fy))
        tempTol = abs(xAprox-xC)
        xC = xAprox

        #Concatenacion de iteraciones
        error.append(tempTol)
        iteracion.append(itera)

    #Grafica
    plt.plot(iteracion,error)
    plt.ylabel('Errores')
    plt.xlabel('Iteraciones')
    plt.show()

    return xAprox, itera, tempTol

 #ssm("((log10(7/x)/((1/10)*ln(10)))+(x*(6-x)/(((2*10**2*arccos(x/20)-x*sqrt(10**2-(x**2/4)))**2/(2*(40/ln(10))**2))*((1/(20**2*arccos(x/20)-x*sqrt(10**2-(x**2/4))))+(1/pi*10**2)))))",1,10**(-10))
