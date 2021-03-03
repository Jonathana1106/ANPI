%{
    Metodo de la Secante
    Parametros de Entrada
    @param func: funcion a la cual se le aplicara el algoritmo
    @param x0: primer valor inicial
    @param x1: segundo valor inicial
    @param MAXIT:  iteraciones maximas
    @param TOL:  tolerencia del algoritmo
    
    Parametros de Salida
    @return xAprox: valor aproximado de x
    @return error: porcentaje de error del resultado obtenido
%}

clc;
clear;

function [xAprox, iter] = secante(func, x0, x1, MAXIT, TOL)
    iter = 0;
    iterl = [];
    err = 1;
    errl = [];

    while(err > TOL)

        xAprox = x1 - ((x1 - x0)/(func(x1) - func(x0))) * func(x1);

        err = (abs(xAprox - x1))/(abs(xAprox));
        iterl(iter+1) = iter;
        errl(iter+1) = err;
        iter = iter + 1;
        
        x0 = x1;
        x1 =  xAprox;

        plot(iterl, errl);
        title("Metodo de la Secante");
        xlabel("Iteraciones");
        ylabel("% Error");

    endwhile
    return;
endfunction

x0 = 0;
x1 = 1;
MAXIT = 100;
TOL = 0.0001;
func = @(x) e^-(x^2) - x;
[xAprox, iter] = secante(func, x0, x1, MAXIT, TOL);
printf('xAprox = %f\nIteraciones = %i \n', xAprox, iter);