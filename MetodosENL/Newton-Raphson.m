%{
    Metodo de la Biseccion
    Parametros de Entrada
    @param func: funcion a la cual se le aplicara el algoritmo
    @param x0: valor inicial
    @param MAXIT:  iteraciones maximas
    @param TOL:  tolerencia del algoritmo
    
    Parametros de Salida
    @return xAprox: valor aproximado de x
    @return error: porcentaje de error del resultado obtenido
%}

clc;
clear;
pkg load symbolic;

function [xAprox, iter] = newtonRaphson(func, x0, MAXIT, TOL)
    iter = 0;
    iterl = [];
    err = 1;
    errl = [];
    xAprox = x0;
    syms f(x);
    f(x) = func;
    fd = diff(f);

    while(err > TOL)
        xk = xAprox;
        xAprox = xk - (func(xk))/(double(fd(xk)));

        err = (abs(xAprox - xk))/(abs(xAprox));

        iterl(iter+1) = iter;
        errl(iter+1) = err;

        iter = iter + 1;

        plot(iterl, errl);
        title("Metodo de Newton-Raphson");
        xlabel("Iteraciones");
        ylabel("% Error");
    endwhile
    return;
endfunction

x0 = 3/4;
MAXIT = 100;
TOL = 0.0000000001;
func = @(x) cos(2 * x)^2 - x^2;
[xAprox, iter] =  newtonRaphson(func, x0, MAXIT, TOL);
printf('xAprox = %f\nIteraciones = %i \n', xAprox, iter);