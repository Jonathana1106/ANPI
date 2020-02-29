clear;
close all;

%{
    Metodo de Newton Raphson
    @param func: funcion a la cual se le aplicara el algoritmo
    @param x0: valor inicial
    @param tol: tolerencia del algoritmo

    @return xAprox: valor aproximado de x
    @return iter: iteraciones necesarias para aproximar x
    %}

function [xAprox, iter] = newtonRaphson (func, x0, tol)

    % Valor incial de x
    xAprox(1) = x0;
    iter = 0;

    % Convertir la funcion a programacion simbolica
    syms f(x);
    f(x) = func;
    
    % Repetir hasta que x se haya acercado al cero de la funcion
    while (abs(func(xAprox(end))) > tol)
        % Obtener el valor de xk
        xk = xAprox(end);
        % Derivar la funcion
        df = diff(f);
        % Actualizar el valor de x y las iteraciones
        xAprox(end + 1) = xk - func(xk) / double(df(xk));
        iter = iter + 1;
    endwhile

    return;
endfunction


% Prueba
% Valor inicial
x0 = 3 / 4;
% Tolerancia
tol = 0.0000000001;
% Funcion a la cual se le aplica el metodo
func = @(x) cos(2 * x).^2 - x.^2;
% Llamado de la funcion
[xAprox, iter] = newtonRaphson (func, x0, tol);
printf('xAprox = [');
printf(' %f ', xAprox);
printf(']\nIteraciones = %i', iter);
