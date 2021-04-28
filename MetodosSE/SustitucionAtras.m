%{
    Metodo de Sustitucion Atras
    -Resuelve un sistema del tipo Ax = b
    Parametros de Entrada
        @param matrizA: matriz triangular superior NxN
        @param matrizB: matriz Nx1
    
    Parametros de Salida
        @return X: solucion de la matriz
%}

clc;
clear;
pkg load symbolic;
format long;
warning('off', 'all');

function X = sustitucionAtras(matrizA, matrizB)
    n = length(matrizB);
    X = zeros(n, 1);
    X(n) = matrizB(n)/matrizA(n, n);
    
    for(k = n-1 : -1 : 1)
        div = matrizA(k, k);
    if (div != 0)
        X(k) = (matrizB(k) - matrizA(k, k+1:n)*X(k+1:n))/matrizA(k, k);
    else
        disp("Error: se ha producido una division por cero");
    endif
  endfor
endfunction