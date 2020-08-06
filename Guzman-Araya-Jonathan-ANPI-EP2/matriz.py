def matriz(a, b, n):
    matrix = []
    if a != b and n >= 3:
        for i in range(n):
            fila = []
            for j in range(n):
                fila.append(min(a*i - b, a*j - b))
            matrix.append(fila)
        return matrix
    else:
        return "Error"
