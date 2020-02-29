clear;
close all;

%{
    Metodo de la Biseccion
    Entradas
      @param a: limite inferior del intervalo
      @param b:  limite superior del intervalo
      @param tol:  tolerencia del algoritmo
      @param f: funcion a la cual se le aplicara el algoritmo
    Salidas
      @return xAprox: valor aproximado de x
      @return iter: iteraciones necesarias para aproximar x
    %}

function [xAprox, iter] = bisection (a, b, tol, f)

    % Validar la condicion para encontrar el cero
    if (f(a) * f(b) < 0)
        % Valor inicial de x
        xAprox = (a + b) / 2;
        iter = 0;
        
        % Repetir hasta que el x se acerque al cero
        while (abs(f(xAprox)) > tol)
            % Verificar cual es el nuevo intervalo de la funcion
            if (f(a) * f(xAprox) < 0)
                b = xAprox;
            else
                a = xAprox;
            endif

            % Actualizar el valor de x y de las iteraciones
            xAprox = (a + b) / 2;
            iter = iter + 1;
        endwhile
    else
        error("Condiciones no garantizan el cero de la funcion");
    endif

    return;
endfunction


% Main
% Limites
a = 0;
b = 2;
% Tolerancia
tol = 0.1;
% Funcion a la cual se le aplicara el metodo
func = @(x) e^x-x-2;
% Llamado de la funcion
[xAprox, iter] = bisection (a, b, tol, func);
printf('xAprox = %f\nIteraciones = %i', xAprox, iter);
