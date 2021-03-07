%{
    Metodo del Punto Fijo
    Parametros de Entrada
    @param func: funcion a la cual se le aplicara el algoritmo
    @param xa: primer valor inicial
    @param xb: segundo valor inicial
    @param MAXIT:  iteraciones maximas
    @param TOL:  tolerencia del algoritmo
    
    Parametros de Salida
    @return xAprox: valor aproximado de x
    @return error: porcentaje de error del resultado obtenido
%}

clc;
clear;
pkg load symbolic;

function [xAprox, iter] = puntoFijo(func, xa, xb, MAXIT, TOL)
    iter = 0;
    iterl = [];
    err = 1;
    errl = [];

    x0 =  x0 + x1.rand(1,1)
    syms g(x);
    g(x) = func;
    gd = diff(f);

    

    %Existencia



