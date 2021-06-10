###############################################################################
from numpy import double
from sympy import sympify, symbols, diff
###############################################################################


def trapecio(funcion, a, b):
    '''
    Metodo de la Regla del Trapecio
    :param funcion: funcion a la cual se le calculara el area
    :param a: intervalo inferior
    :param b: intervalo superior
    :return: xAprox: aproximacion del area
    :return: error: error de la solucion
    '''
    x = symbols('x')
    f = sympify(funcion)
    xAprox = double(((b - a)/2)*(f.subs(x, a) + f.subs(x, b)))
    fd = diff(f, x)
    fdd = diff(fd, x)
    lista = []
    lista.append(abs(double(fdd.subs(x, a))))
    lista.append(abs(double(fdd.subs(x, b))))
    vmax = max(lista)
    error = ((b - a)**3/(12))*(vmax)
    return xAprox, error


if __name__ == '__main__':
    # Intervalo inferior
    a = 2
    # a = 1
    # Intervalo superior
    b = 5
    # b = 2
    # Funcion
    funcion = "ln(x)"
    # funcion = "13/(5*x+4)"
    # Llamado de la funcion
    print("######################################################")
    print("Metodo de la Regla del Trapecio \n")
    xAprox, error = trapecio(funcion, a, b)
    print('xAprox = {}\n%Error = {}'.format(xAprox, error))
