import math
import numpy as np
import matplotlib.pyplot as plt

def trazador_cubico(func, S):
    # Procedemos a evaluar los puntos 'x'
    # para encontrar su valor 'y'
    valoresY = []
    k = len(S)
    for i in range(0, k):
        valoresY.append(func(S[i]))
    # Procedemos a agrupar los valores 'xi'
    # y 'yi' en una lista de tuplas
    points = []
    n = len(S)
    for i in range(0, n):
        points.append([S[i], valoresY[i]])

    points = np.array([np.array(p) for p in points])
    print("Los puntos son:\n", points, "\n")
    # Calculando los delta_hk
    delta_hk = points[1:, 0] - points[:-1, 0]
    print("Los delta_hk son:\n", delta_hk, "\n")
    # Calculando los delta_yk
    delta_yk = points[1:, 1] - points[:-1, 1]
    print("Los delta_yk son:\n", delta_yk, "\n")
    # La matriz y el vector para resolver el sistema
    A, u = [], []
    print("A es:\n", A, "\n")
    print("u es:\n", u, "\n")
    # Cantidad de puntos -1 (n)
    k = delta_hk.shape[0]
    print("k es:\n", k, "\n")
    for i in range(1, k):
        # Primer caso Ms[1] = 0
        if i == 1:
            print("delta_hk[i] es:\n", delta_hk[i], "\n")
            print("(k - 3) * [0] es:\n", (k - 3) * [0], "\n")
            print("delta_hk[i] + [0] * (k - 3) es:\n", delta_hk[i] + [0] * (k - 3), "\n")
            A.append([2 * (delta_hk[i - 1] + delta_hk[i]), delta_hk[i]] + [0] * (k - 3))
        # Segundo caso Ms[n+1] = 0
        elif i == k - 1:
            print("delta_hk[i] es:\n", delta_hk[i], "\n")
            print("(k - 3) * [0] es:\n", (k - 3) * [0], "\n")
            print("delta_hk[i] + [0] * (k - 3) es:\n", delta_hk[i] + [0] * (k - 3), "\n")
            A.append([0] * (k - 3) + [delta_hk[i - 1], 2 * (delta_hk[i - 1] + delta_hk[i])])
        else:
            A.append([0] * (i - 2) + [delta_hk[i - 1], 2 * (delta_hk[i - 1] + delta_hk[i]), delta_hk[i]] + [0] * (k - 2 - i))
        # Creando el vector u
        u.append(6 * (delta_yk[i] / delta_hk[i] - delta_yk[i - 1] / delta_hk[i - 1]))
    # Convirtiendolo a numpy array
    A = np.array([np.array(a) for a in A])
    u = np.array(u)
    print("A es:\n", A, "\n")
    print("u es:\n", u, "\n")
    # Resolviendo el sistema mediante Thomas, LU o Jacobi
    x0 = np.zeros(u.shape)
    # Ms = gauss_seidel(A, u, u*0, 0.000001)
    # Ms = fact_lu(A, u)
    Ms = jacobi(A, u, u*0, 0.0000001)
    print("X0 es:\n", x0, "\n")
    print("Ms es:\n", Ms, "\n")
    # Append Ms[1] = 0 and Ms[n+1] = 0
    Ms = np.append(0, np.append(Ms, 0))
    print("Ms es:\n", Ms, "\n")
    # Coeficientes
    a, b, c, d = [[], [], [], []]
    # Puntos iniciales
    xk = points[:, 0]
    yk = points[:, 1]
    # Calculando los coeficientes
    for i in range(k):
        a.append((Ms[i + 1] - Ms[i]) / (6 * delta_hk[i]))
        b.append(Ms[i] / 2)
        c.append((yk[i + 1] - yk[i]) / delta_hk[i] - (2 * delta_hk[i] * Ms[i] + delta_hk[i] * Ms[i + 1]) / 6)
        d.append(yk[i])
    # Convirtiendo
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    d = np.array(d)

    Sx = []
    iteraciones = []
    for i in range(len(a)):
        iteraciones.append(i)
        Sx.append(a[i]*(math.pow(S[i+1] - S[i], 3)) + b[i]*(math.pow(S[i+1] - S[i], 2)) + c[i]*(S[i+1] - S[i]) + d[i])

    print("Sx es:\n", Sx, "\n")
    plt.title("Trazadores Cubicos")
    plt.xlabel("Iteraciones")
    plt.ylabel("Sx(i)")
    plt.stem(iteraciones, Sx)
    plt.show()
    return a, b, c, d, Sx

def jacobi(A, b, x0, tol):
    n = len(A)
    A = np.array(A)
    b = np.array(b)
    L = np.zeros((n, n))
    D = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i > j:
                L[i][j] = A[i][j]
            elif i < j:
                U[i][j] = A[i][j]
            else:
                D[i][j] = A[i][j]

    x = np.array(x0)
    error = np.linalg.norm(np.dot(A, x) - b)
    i = 0

    m_inv = np.linalg.inv(D)
    m_times_n = np.dot(m_inv, (-1 * (L + U)))
    m_times_b = np.dot(m_inv, b)

    while error >= tol:
        x = np.dot(m_times_n, x) + m_times_b
        error = np.linalg.norm(np.dot(A, x) - b)
        i += 1

    return x


def fact_lu(matrizD, matrizI):
    if(np.linalg.det(matrizD) == 0):
        print("La matriz no es singular")
        return
    else:
        pass
    n = len(matrizD)
    L = np.eye(n)
    U = matrizD

    for i in range(1, n):
        pivot = U[i - 1][i - 1]
        pivotRow = U[i - 1]
        M = np.zeros((1, n - i))
        m = M.size + 1

        for k in range(1, m):
            try:
                M[i - 1][k - 1] = (U[i + k - 1][i - 1]) / pivot
            except:
                M = (U[i + k - 1][i - 1]) / pivot

        for k in range(1, m):
            try:
                U[i + k - 1] = U[i + k - 1] - (np.multiply(pivotRow, M[i - 1][k - 1]))
                L[i + k - 1][i - 1] = M[i - 1][k - 1]
            except:
                U[i + k - 1] = U[i + k - 1] - (np.multiply(pivotRow, M))
                L[i + k - 1][i - 1] = M

    Y = ((np.linalg.inv(L)).dot(np.transpose(matrizI)))
    X = (np.linalg.inv(U)).dot(Y)
    return X

def gauss_seidel(A, b, x0, tol):
    n = len(A)
    A = np.array(A)
    b = np.array(b)
    L = np.zeros((n, n))
    D = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i > j:
                L[i][j] = A[i][j]
            elif i < j:
                U[i][j] = A[i][j]
            else:
                D[i][j] = A[i][j]

    x = np.array(x0)
    error = np.linalg.norm(np.dot(A, x) - b)
    i = 0

    m_inv = np.linalg.inv(D + U)
    m_times_n = np.dot(m_inv, (-1 * L))
    m_times_b = np.dot(m_inv, b)

    while error >= tol:
        x = np.dot(m_times_n, x) + m_times_b
        error = np.linalg.norm(np.dot(A, x) - b)
        i += 1

    return x

if __name__ == '__main__':
    # Intervalo
    intervalo = [1, 6]
    # Conjunto soporte
    # S = [1, 2, 3, 4, 5, 6]
    S = [1, 1.05, 1.07, 1.1]
    # Funcion
    # func = lambda x: x * (math.cos(x)) + math.pow(x, 2) - (1 / x)
    func = lambda x: 3*x*(math.pow(math.e, x)) - 2*(math.pow(math.e, x))
    # Llamado de la funcion
    a, b, c, d, Sx = trazador_cubico(func, S)
    print("######################################################")
    print("Metodo del Trazador Cubico \n")
    print('a = {}\nb = {}\nc = {}\nd = {}\nSx(i) = {}'.format(a, b, c, d, Sx))