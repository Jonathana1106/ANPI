###############################################################################
from numpy import absolute, double
from sympy import Symbol, sympify, lambdify, solve, symbols, diff
###############################################################################

def trapecio(funcion, a, b):
    '''
    Metodo de la Regla del Trapecio
    :param funcion: funcion a la cual se le calculara el area
    :param a: intervalo inferior
    :param b: intervalo superior
    :return: xAprox: aproximacion del area
    '''
    x = symbols('x')
    f = sympify(funcion)
    xAprox = double(((b-a)/2)*(f.subs(x, a) + f.subs(x, b)))
    fd = diff(f, x)
    fdd = diff(fd, x)
    lista = []
    lista.append(absolute(fdd.subs(x, a)))
    lista.append(absolute(fdd.subs(x, b)))
    vmax = max(lista)
    error = ((b-a)**3/(12))*(abs(vmax))
    return xAprox, error

if __name__ == '__main__':
    #Intervalo inferior
    a = 2
    #Intervalo superior
    b = 5
    #Funcion
    funcion = "log(x)"
    #Llamado de la funcion
    print("######################################################")
    print("Metodo de la Regla del Trapecio \n")
    xAprox, error = trapecio("ln(x)", 2, 5)
    print('xAprox = {}\n%Error = {}'.format(xAprox, error))