"""Creacion de los vectores que a, b, c que son la tridiagonal de la matriz A."""
a = [1]*100
b = [5]*100
c = [1]*100
"""Creacion del vector d solucion."""
d = [0]*100
i = 0
n = 99
while i <= n:
    if i == 0 or i == 99:
        d[i] = -12
        i = i + 1
    else:
        d[i] = -14
        i = i + 1

        
import numpy as np

""" Solución de un sistema lineal de ecuaciones algebraicas con unamatriz
    de coeficientes de tres diagonales usando el algoritmo de Thomas.

    Entradas:
        a (matriz): una matriz que contiene una diagonal inferior (no se utiliza a [0]).
        b (matriz): una matriz que contiene la diagonal principal.
        c (matriz): una matriz que contiene una diagonal inferior (no se utiliza c [-1]).
        d (matriz): lado derecho del sistema de ecuacion matricial.
    Salida:
        x (matriz): matriz que contiene la solución del sistema.    
"""

def MTAT(a, b, c, d):
    n = len(b)
    x = np.zeros(n, dtype=int, order='F')
    
    #Primer paso:
    
    for i in range(1,n):
        q = a[i]/b[i-1]
        b[i] = b[i] - c[i-1]*q
        d[i] = d[i] - d[i-1]*q
    
    #Solucion del sistema:
    
    q = d[n-1]/b[n-1]
    x[n-1] = q
    
    for i in range(n-2,-1,-1):
        q = (d[i]-c[i]*q)/b[i]
        x[i] = q
    
    return x
