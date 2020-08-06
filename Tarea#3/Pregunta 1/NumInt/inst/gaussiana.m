function I = gaussiana(f, a, b, M)
    %Funcion que obtiene un valor aproximado de la integral de la funcion f en 
    %un intervalo [a, b] utilizando el metodo de cuadraturas gaussianas; para
    %ello se ayuda de la funcion polinomio de legendre el cual se encarga de 
    %calcular el polinomio de legendre de grado M necesario. "hepl polinomio_legendre"
    %Parametros iniciales: 
    % -f: funcion que se desea integrar.
    % -a: punto inicial de integracion de la funcion.
    % -b: punto final de integracion de la funcion.
    % -M: grado del polinomio de legendre.  
    %           
    %Parametros de salida:                           
    % -I: Valor aproximado de la integral de la funcion f en los intervalos [a, b].
    %
    warning('off')
    pkg load symbolic
    syms x;
    [polinomio,ceros] = polinomio_legendre(M);
    expr = f;
    expr = subs(expr, x,((b-a)/2)*x +((b + a)/2));
    fx = matlabFunction(sym(expr));
    i = 1;
    res = 0;
    while(i <= M)
        res += fx(ceros(i));
        i += 1;
    endwhile
    I = res*((b-a)/2);
endfunction