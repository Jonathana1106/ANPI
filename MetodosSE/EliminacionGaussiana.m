%{
    Metodo de Eliminacion Gaussiana
    Parametros de Entrada
        @param f: funcion a la cual se le aplicara el algoritmo
        @param a: limite inferior del intervalo
    
    Parametros de Salida
        @return xAprox: valor aproximado de x
%}

clc;
clear;
pkg load symbolic;

function matrizResultado = eliminacionGaussiana(matrizD, matrizI)
    [n, m] = size(matrizD);
    listaSimb = [];

    if(n ~= m)
        error("La matriz dependiente debe ser cuadrada")
    endif

    matrizA = [];
    for i = i : n
        matrizA = [matrizA; matrizD(i,:), matrizI(i,:)];
        listaSimb = [listaSimb sym(strcat('x', num2str(i)))];
    end

    [L, U] = lu(matrizA);

    for i = 1 : n
        subLista = U(n-i+1,:)
        ecuacion = strcat('-', num2str(subLista(m+1)));

        for x = 1 : m
            ecuacion = strcat(ecuacion, ' + ', num2str(subLista(x)), ' * ', char(listaSimb(x)));
        end

        resultado = solve(sym(ecuacion));
        listaSimb(n-i+1) = resultado;
    end
    matrizResultado = listaSimb;
endfunction

%Matriz de coeficientes
a = [2, -6, 12, 16; 1, -2, 6, 6; -1, 3, -3, -7; 0, 4, 3, 6];
%Vector de terminos independientes
b = [70; 26; -30; -26]; 
%Llamado de la funcion
matrizResultado =  eliminacionGaussiana(a, b)
printf("############################################ \n");
printf("Metodo de Eliminacion Gaussiana \n");
printf('Matriz Resultado = %f\n', matrizResultado);