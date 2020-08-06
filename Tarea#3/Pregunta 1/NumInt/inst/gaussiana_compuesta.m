function I = gaussiana_compuesta(f, a, b, M, N)
    %Funcion que obtiene un valor aproximado de la integral de la funcion f en 
    %un intervalo [a, b] utilizando el metodo de cuadraturas gaussianas compuestas; 
    %para ello se ayuda de la funcion polinomio de legendre el cual se encarga de 
    %calcular el polinomio de legendre de grado n necesario. "hepl polinomio_legendre"
    %Parametros iniciales: 
    % -f: funcion que se desea integrar.
    % -a: punto inicial de integracion de la funcion.
    % -b: punto final de integracion de la funcion.
    % -M: grado del polinomio de legendre.
    % -N: numero de puntos en el intervalo [a, b].  
    %           
    %Parametros de salida:                           
    % -I: Valor aproximado de la integral de la funcion f en los intervalos [a, b].
    % 
    warning('off')
    pkg load symbolic
    syms x;
    [polinomio, ceros] = polinomio_legendre(M);
    h = (b - a)/(N - 1);
    valores = [a];
    atemp = a + h;
    while (atemp) < b
        valores = [valores atemp];
        atemp = atemp + h;
    endwhile
    valores = [valores b];
    intera = 1;
    interb = 1;
    res = 0;
    j = 1;
    temp = 0;
    while(j <= (M - 1))
        i = 1;
        intera = valores(j);
        interb = valores(j + 1);
        t1 = (interb - intera)/2;
        t2 = (interb + intera)/2;
        expr = f;
        expr = subs(expr, x, (t1)*x + (t2));
        fx = matlabFunction(sym(expr));
        res = 0;
        while(i <= M)
            res += fx(ceros(i));
            i = i + 1;
        endwhile
        temp = temp + (res*t1);
        j = j + 1;
    endwhile
    I = temp;
endfunction