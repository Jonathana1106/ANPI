from sympy import sympify
import matplotlib.pyplot
import numpy as np

def edo2(p, q, f, h, a, b, y0, yn):
    """
    # Funcion que se encarga de resolver sistemas de ecuaciones lineales cuya
    # matriz de coeficientes es una matriz tridiagonal.
    #Entradas:
    # -p: funcion continua de variable real.
    # -q: funcion continua de variable real.
    # -f: funcion continua de variable real.
    # -h: tamano del paso.
    # -a: valor inicial del intervalo.
    # -b: valor final del intervalo.
    # -y0: valor de y evaluado en a.
    # -yn: valor de y evaluado en b.
    #Salidas:
    # -x: vectorSolucion que contiene los puntos del eje x.
    # -y: vectorSolucion que contiene los puntos del eje y.
    """
    N = int((b - a)/h)
    matriz = []
    vectorSolucion = []
    x = []
    pj = sympify(p)
    qj = sympify(q)
    fj = sympify(f)
    tj = a + (0*h)
    x += [tj]
    listaValoresX = [] 
    listaValoresY = []
    listaValoresX += [tj]
    
    for i in range(0, N):
        flag = []
        for j in range(0, N):
            flag += [0]
        matriz += [flag]

    matriz[0][0] = 2 + (pow(h, 2)*qj.subs({'x': tj}))
    matriz[0][1] = (h/2)*(pj.subs({'x':tj})) - 1
    e0 = ((h/2)*(pj.subs({'x':tj})) + 1) * y0
    vectorSolucion += [(-pow(h, 2)*fj.subs({'x':tj})) + e0]
    
    for i in range(1, N-1):
        tj = a + (i*h)
        x += [tj]
        listaValoresX += [tj]
        matriz[i][i-1] = (-h/2)*(pj.subs({'x':tj})) - 1
        matriz[i][i] = 2 + (pow(h,2)*qj.subs({'x': tj}))
        matriz[i][i+1] = (h/2)*(pj.subs({'x':tj})) - 1
        vectorSolucion += [(-pow(h, 2)*fj.subs({'x':tj}))]
        
    tj = a + ((N-1)*h)
    x += [tj]
    listaValoresX += [tj]
    matriz[N-1][N-2] = ((-h/2)*pj.subs({'x':tj})) - 1
    matriz[N-1][N-1] = 2 + (pow(h,2)*qj.subs({'x': tj}))

    en = (((-h/2)*pj.subs({'x':tj})) + 1)*yn
    vectorSolucion += [(-pow(h,2)*fj.subs({'x':tj})) + en]
    y = np.linalg.solve( np.array(matriz, dtype='float'), np.array(vectorSolucion, dtype='float')).copy()
    for i in range(0, len(y)):
        listaValoresY += [y[i]]
    return [listaValoresX, listaValoresY]

def ejemploDiferenciasFinitas():
    a = 1
    X = []
    Y = []
    funcion = "(sin(6-x))*((sin(5)*(x**(1/2)))**-1)"
    f = sympify(funcion)
    for i in range(0, 5*10**3):
        X += [a + (i*10**-3)]
        Y += [f.subs({'x':X[i]})]
    return[X, Y]


def animacionGrafica():
    p = "-1/x"
    q = "(1/(4*x**2))-1"
    f = "0"
    y0 = 1
    yn = 0
    a = 1
    b = 6
    h = 0
    leyendaGrafica = []
    matplotlib.pyplot.title("Resultado") 
    puntos = ejemploDiferenciasFinitas()
    matplotlib.pyplot.plot(puntos[0], puntos[1]) 
    leyendaGrafica.append('Funcion Inicial')
    matplotlib.pyplot.legend( leyendaGrafica, loc=1)
    matplotlib.pyplot.pause(2)
    for i in range(1,3):
        leyendaGrafica.append("Iteracion: #"+ str(i))
        h = 10**-i
        x = edo2(p, q, f, h, a, b, y0, yn)
        matplotlib.pyplot.plot(x[0], x[1])   
        matplotlib.pyplot.legend( leyendaGrafica, loc=1)
        matplotlib.pyplot.pause(2)
    matplotlib.pyplot.show()
    
animacionGrafica()
