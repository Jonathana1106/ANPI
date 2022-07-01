%{
    Metodo de la Falsa Posicion Modificado
    Parametros de Entrada
        @param func: funcion a la cual se le aplicara el algoritmo
        @param a: valor del primer intervalo
        @param b: valor del segundo intervalo
        @param n:  iteraciones maximas
        @param tol:  tolerencia del algoritmo
    
    Parametros de Salida
        @return x: valor aproximado de x
        @return error: porcentaje de error del resultado obtenido
%}

clc;
clear;

function x = metodo_falsa_posicion_mod(func, a, b, n, tol)

    err = 1;
    x = 0;
    k = 0;
    
    while (k < n)
        h = (b-a)/n;
        ck = a + k*h;
        ck1 = a + (k+1)*h;

        if(((func(ck))*(func(ck1))) < 0)
        
            x = ck1 - ((ck1-ck)/((func(ck1))-(func(ck))))*(func(ck1));
            k = k + 1;
            err = (abs(func(x)));

            if(err < tol)
                return;
            end
        elseif(func(ck) * func(ck1) > 0)
            if(err < tol)
                return;
            else
                k = k + 1;
            end
        else
            error("Error.")
        end
    endwhile
    return;
endfunction

a = 0;
b = 2;
n = 10;
tol = 0.0000000001;
func = @(x) (sin(x)^2) + x^2 -1;
x = metodo_falsa_posicion_mod(func, a, b, n, tol);
printf("############################################ \n");
printf("Metodo de la Falsa Posicion \n");
printf('x = %f\n', x);