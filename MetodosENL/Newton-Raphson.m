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

function [xAprox, err] = newtonRaphson(func, x0, MAXIT, TOL)
    iter = 1;
    err = 1; 
    iterl = []; % Lista que almacena el numero de iteraciones para despues graficar
    errl = []; % Lista que almacena el % de error de cada iteracion para despues graficar
    xAprox = x0;
    syms f(x);
    f(x) = func;
    fd = diff(f);

    while(iter < MAXIT)
        xk = xAprox;
        xAprox = xk - (func(xk)) / (double(fd(xk)));
        err = (abs(xAprox - xk)) / (abs(xAprox));
        iterl(iter) = iter;
        errl(iter) = err;
        
        if(err < TOL)
          grafica(iterl, errl);
          return;
        else
            iter = iter + 1;
        endif
    endwhile
    grafica(iterl, errl);
    return;
endfunction

function grafica(listaValoresX, listValoresY)
    plot(listaValoresX, listValoresY, 'bx');
    title("Metodo de Newton-Raphson");
    xlabel("Iteraciones");
    ylabel("% Error");
endfunction

%Valor inicial
x0 = 1;
%Iteraciones maximas
MAXIT = 100;
%Tolerancia
TOL = 0.0001;
%Funcion 
func = @(x) e^x - 1/x;
%Llamado de la funcion
[xAprox, err] =  newtonRaphson(func, x0, MAXIT, TOL);
printf("############################################ \n");
printf("Metodo de Newton-Raphson \n");
printf('xAprox = %f\n%%Error = %i \n', xAprox, err);