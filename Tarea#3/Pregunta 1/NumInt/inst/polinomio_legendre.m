function [polinomio, ceros] = polinomio_legendre(n)
    %Funcion que se encarga de obtener el polinomio de legendre de grado n.
    %Parametros iniciales: 
    % -n: grado del polinomio.           
    %            
    %Parametros de salida:                           
    % -pol: polinomio de grado n.
    % -ceros: ceros del polinomio.
    %
    
    pkg load symbolic
    syms x;
    var = sym('x');
    fracpol = 1/((factorial(n))*(2^n));
    polexp = ((x^2)-1)^n;
    df = diff(polexp, x, n);
    polinomio = (simplify(fracpol*df));
    ceros = double(solve(polinomio,x));
endfunction