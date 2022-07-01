%{
    Metodo de Sustitucion Adelante
    -Resuelve un sistema del tipo Ax = b
    Parametros de Entrada
        @param matrizA: matriz triangular inferior NxN
        @param matrizB: matriz Nx1
    
    Parametros de Salida
        @return X: solucion de la matriz
%}

clc;
clear;
pkg load symbolic;
format long;
warning('off', 'all');

function X = sustitucionAdelante(matrizA, matrizB)
    n = length(matrizB);
    X = zeros(n, 1);
    X(1) = matrizB(1)/matrizA(1, 1);
    
    for(k = 2 : n)
        div = matrizA(k, k);
    if (div != 0)
        X(k) = (matrizB(k) - matrizA(k, 1 : k-1)*X(1: k-1))/matrizA(k, k);
    else
        disp("Error: se ha producido una division por cero");
    endif
  endfor
endfunction