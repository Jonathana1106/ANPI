%{
    Metodo de Sustitucion Atras
    Parametros de Entrada
        @param f: funcion a la cual se le aplicara el algoritmo
        @param a: limite inferior del intervalo
    
    Parametros de Salida
        @return xAprox: valor aproximado de x
%}

clc;
clear;

function matrizResultado = sustitucionB(matrizTI, matrizC)
    [n, m] = size(matrizD);
    listaSimb = [];

    for i = 1 : n
        listaSimb = [listaSimb; sym(strcat('x', num2str(i)))];
    end

    for i = 1 : n
        subLista = matrizTI(n-i+1,:);
        ecuacion = strcat('-', num2str(matrizC(i)));

        for x = 1 : m
            ecuacion = strcat(ecuacion, ' + ', num2str(subLista(x)), ' * ', char(listaSimb(x)));
        end
        
        resultado = solve(sym(ecuacion));
        listaSimb(i) = resultado;
    end
    matrizResultado = listaSimb;
endfunction