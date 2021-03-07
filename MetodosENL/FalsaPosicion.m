%{
    Metodo de la Falsa Posicion
    Parametros de Entrada
        @param func: funcion a la cual se le aplicara el algoritmo
        @param x0: valor del primer intervalo
        @param x1: valor del segundo intervalo
        @param MAXIT:  iteraciones maximas
        @param TOL:  tolerencia del algoritmo
    
    Parametros de Salida
        @return xAprox: valor aproximado de x
        @return error: porcentaje de error del resultado obtenido
%}

clc;
clear;

function [xAprox, err] = falsaPosicion(func, x0, x1, MAXIT, TOL)
    a = x0;
    b = x1;

    if(func(a) * func(b) < 0)
        iter = 1;
        err = 1;
        iterl = []; % Lista que almacena el numero de iteraciones para despues graficar
        errl = []; % Lista que almacena el % de error de cada iteracion para despues graficar
        xAprox = 0;

        x2 = x1 - ((x1 - x0) / (func(x1) - func(x0))) * func(x1);

        if(func(a) * func(x2) < 0)

            while(iter < MAXIT)
                xAprox = x2 - ((x2 - a) / (func(x2) - func(a))) * func(x2);
                err = (abs(xAprox - x2)) / (abs(xAprox));
                iterl(iter) = iter;
                errl(iter) = err;
                
                if(err < TOL)
                  grafica(iterl, errl);
                  return;
                else
                    iter = iter + 1;
                    a = x2;
                    x2 =  xAprox;
                endif
            endwhile

            grafica(iterl, errl);
            return;

        elseif(func(x2) * func(b) < 0)
     
            while(iter < MAXIT)
                xAprox = b - ((b - x2) / (func(b) - func(x2))) * func(b);
                err = (abs(xAprox - b)) / (abs(xAprox));
                iterl(iter) = iter;
                errl(iter) = err;
                
                if(err < TOL)
                  grafica(iterl, errl);
                  return;
                else
                    iter = iter + 1;
                    x2 = b;
                    b =  xAprox;
                endif
            endwhile

            grafica(iterl, errl);
        else
            error("Condiciones en los parametros de entrada no garantizan el cero de la funcion.")
        endif
    else
        error("Condiciones en los parametros de entrada no garantizan el cero de la funcion.")
    endif
    return;
endfunction

function grafica(listaValoresX, listValoresY)
    plot(listaValoresX, listValoresY, 'bx');
    title("Metodo de la Falsa Posicion");
    xlabel("Iteraciones");
    ylabel("% Error");
endfunction

x0 = 1/2;
x1 = pi/4;
MAXIT = 100;
TOL = 0.00001;
func = @(x) cos(x) - x;
[xAprox, err] = falsaPosicion(func, x0, x1, MAXIT, TOL);
printf("############################################ \n");
printf("Metodo de la Falsa Posicion \n");
printf('xAprox = %f\n%%Error = %i \n', xAprox, err);