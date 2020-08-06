import numpy as np


def matriz(a, b, n):
    matrix = []
    if a != b and n >= 3:
        for i in range(n):
            fila = []
            for j in range(n):
                fila.append(min(a*(i+1) - b, a*(j+1) - b))
            matrix.append(fila)
        print (np.asmatrix(matrix))
        return (np.asmatrix(matrix))
    else:
        return "Error"



matriz(1, 0, 3)
    

