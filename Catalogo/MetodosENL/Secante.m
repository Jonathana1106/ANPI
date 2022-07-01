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

function [xAprox, err] = secante(func, x0, x1, MAXIT, TOL)
    iter = 2;
    err = 1;
    iterl = []; % Lista que almacena el numero de iteraciones para despues graficar
    errl = []; % Lista que almacena el % de error de cada iteracion para despues graficar

    while(iter < MAXIT)

        xAprox = x1 - ((x1 - x0) / (func(x1) - func(x0))) * func(x1);
        err = (abs(xAprox - x1)) / (abs(xAprox));
        iterl(iter-1) = iter;
        errl(iter-1) = err;
        
        if(err < TOL)
          grafica(iterl, errl);
          return;
        else
          iter = iter + 1;
          x0 = x1;
          x1 =  xAprox;
        endif
    endwhile
    grafica(iterl, errl);
    return;
endfunction

%{
    Parametros de Entrada
        @param listaValoresX: valores del eje 'x'
        @param listaValoresY: valores del eje 'y'
    
    Parametros de Salida
        @return: Grafico de los datos ingresados
%}
function grafica(listaValoresX, listaValoresY)
    plot(listaValoresX, listaValoresY, 'bx');
    title("Metodo de la Secante");
    xlabel("Iteraciones");
    ylabel("% Error");
endfunction

%Valores iniciales
x0 = 0;
x1 = 1;
%Iteraciones maximas
MAXIT = 100;
%Tolerancia
TOL = 0.01;
%Funcion 
func = @(x) e^-(x^2) - x;
%Llamado de la funcion
[xAprox, err] = secante(func, x0, x1, MAXIT, TOL);
printf("############################################ \n");
printf("Metodo de la Secante \n");
printf('xAprox = %f\n%%Error = %i \n', xAprox, err);