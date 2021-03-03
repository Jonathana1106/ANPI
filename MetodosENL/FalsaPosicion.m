%{
    Metodo de la Falsa Posicion
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


function [xAprox, iter] = falsaPosicion(func, x0, x1, MAXIT, TOL)
    a = x0;
    b = x1;

    if(func(a) * func(b) < 0)
        iter = 0;
        iterl = [];
        err = 1;
        errl = [];
        x2 = 0;
        xAprox = 0;

        x2 = x1 - ((x1 - x0)/(func(x1) - func(x0))) * func(x1);

        if(func(a) * func(x2) < 0)
            iter = 2;

            while(err > TOL)
                xAprox = x2 - ((x2 - a)/(func(x2) - func(a))) * func(x2);

                err = (abs(xAprox - x2))/(abs(xAprox));
                iterl(iter-1) = iter;
                errl(iter-1) = err;
                iter = iter + 1;
        
                a = x2;
                x2 =  xAprox;

                plot(iterl, errl);
                title("Metodo de la Falsa Posicion");
                xlabel("Iteraciones");
                ylabel("% Error");

            endwhile

        elseif(func(x2) * func(b) < 0)
            iter = 2;
            while(err > TOL)
                xAprox = b - ((b - x2)/(func(b) - func(x2))) * func(b);

                err = (abs(xAprox - b))/(abs(xAprox));
                iterl(iter-1) = iter;
                errl(iter-1) = err;
                iter = iter + 1;
        
                x2 = b;
                b =  xAprox;

                plot(iterl, errl);
                title("Metodo de la Falsa Posicion");
                xlabel("Iteraciones");
                ylabel("% Error");

            endwhile
        else
            error("Condiciones en los parametros de entrada no garantizan el cero de la funcion.")
        endif

    else
        error("Condiciones en los parametros de entrada no garantizan el cero de la funcion.")
    endif
    return;
endfunction

x0 = 1/2;
x1 = pi/4;
MAXIT = 100;
TOL = 0.00001;
func = @(x) cos(x) - x;
[xAprox, iter] = falsaPosicion(func, x0, x1, MAXIT, TOL);
printf('xAprox = %f\nIteraciones = %i \n', xAprox, iter);