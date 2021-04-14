%{
    Metodo de Factorizacion LU
    Parametros de Entrada
        @param f: funcion a la cual se le aplicara el algoritmo
        @param a: limite inferior del intervalo
    
    Parametros de Salida
        @return xAprox: valor aproximado de x
%}

clc;
clear;
pkg load symbolic

function matrizResultado = factorizacionLU(matrizD, matrizI)