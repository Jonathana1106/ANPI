import numpy as np
def creamatriz(n):
    l = [0] * n
    m = [l] * n
    print(m)


def tridiagonal(a, b, n):
    l = [0] * n
    m = [l] * n
    x = -1
    y = 2
    z = 1
    #print(m)
    if a != b and n >= 3:
        m[0][0] = 1 + (a/(a-b))
        #m[n-1][n-1] = z
        print(np.asmatrix(m))
    else:
        print('Error')
        
        
        
        
        
    
