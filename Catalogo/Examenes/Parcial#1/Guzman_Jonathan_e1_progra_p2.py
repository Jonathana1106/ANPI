import numpy as np
from sympy import Symbol, solve

def tridiag(T,x,y,z,k1=-1, k2=0, k3=1):
    a = [x]*(T-abs(k1)); b = [y]*(T-abs(k2)); c = [z]*(T-abs(k3))
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)

def triagonal(n,a,b):
    if n>=3 and a!=b:
        A=tridiag(n,1,4,1)
        A[0][0]=1+(a/(a-b))
        A[n-1][n-1]=1
        print(A)
    else:
        print('Error en matriz')

def mb():
    b = [2.5]
    n=1
    while n<250:
        b.append(3)
        n=n+1
    b.append(2.5)
    return b

from numpy import transpose, linalg, array

def sustitucion_adelante(matriz_a, matriz_b):
    """
    Funcion para realizar una sustitucion hacia adelante
    :param matriz_a: matriz triangular inferior
    :param matriz_b: matriz columna
    :return: matriz con el resultado de realizar la sustitucion
    """
    n = len(matriz_a)
    m = len(matriz_a[0])

    lista_simb = []
    # Se crea una lista con las variables simbolicas de la ecuacion
    for i in range(0, n):
        lista_simb.append([Symbol('x' + str(i))])

    # Se resuelve el sistema A x = B utilizando una sustitucion hacia adelante
    for i in range(0, n):
        sub_lista = matriz_a[i]
        ecuacion = '- ' + str(matriz_b[i][0])

        # Se forma la ecuacion
        for x in range(0, m):
            ecuacion += ' + ' + str(sub_lista[x]) + ' * ' + str(lista_simb[x][0])

        # Se resuelve la ecuacion
        resultado = solve(ecuacion)
        lista_simb[i] = resultado

    return lista_simb


def sustitucion_atras(matriz_a, matriz_b):
    """
    Funcion para realizar una sustitucion hacia adelante
    :param matriz_a: matriz triangular superior
    :param matriz_b: matriz columna
    :return: matriz con el resultado de realizar la sustitucion
    """
    n = len(matriz_a)
    m = len(matriz_a[0])

    lista_simb = []
    # Se crea una lista con las variables simbolicas de la ecuacion
    for i in range(0, n):
        lista_simb.append([Symbol('x' + str(i))])

    # Se realiza una sustitucion hacia atras
    for i in range(1, n + 1):
        sub_lista = matriz_a[-i]
        ecuacion = '- ' + str(matriz_b[-i][0])

        for x in range(0, m):
            ecuacion += ' + ' + str(sub_lista[x]) + ' * ' + str(lista_simb[x][0])

        resultado = solve(ecuacion)
        lista_simb[-i] = resultado

    return lista_simb

def factorizacion_cholesky(matriz_a, matriz_b):
    """
    Metodo Factorizacion de Cholesky para resolver un sistema A x = B
    :param matriz_a: matriz cuadrada de nxn
    :param matriz_b: matriz columna de nx1
    :return: matriz x que resuelve el sistema A x = b
    """
    # Se verifica que la matriz A tenga simetria
    ma_transpuesta = transpose(matriz_a)
    norma_a = linalg.norm(array(matriz_a, dtype='float'))
    norma_a_t = linalg.norm(array(ma_transpuesta, dtype='float'))
    if norma_a - norma_a_t != 0:
        return "Error: La matriz_a debe ser simetrica"

    # Se calcula la factorizacion de Cholesky para la matriz_a
    matriz_l = linalg.cholesky(matriz_a)
    matriz_l_t = transpose(matriz_l)

    # Se resuelve el sistema L y = b utilizando una sustitucion hacia adelante
    matriz_y = sustitucion_adelante(matriz_l, matriz_b)

    # Se resuelve el sistema Lt x = y utilizando una sustitucion hacia adelante
    matriz_x = sustitucion_atras(matriz_l_t, matriz_y)

    return matriz_x

a = triagonal(251, 4, 1)
d = mb()
print(factorizacion_cholesky(a, d))