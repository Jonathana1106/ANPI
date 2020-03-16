clear;
close all;

%{
    Metodo del Punto Fijo
    Entradas
      @param gx: funcion despejada
      @param a:  valor inicial
      @param tolera:  tolerencia del algoritmo
      @param n: numero de iteraciones
    Salidas
      @return respuesta: punto fijo solucion
%}

function respuesta = PFijo(gx,a,tolera, n)
    n = 15;
    i = 1;
    b = gx(a);
    e = [];
    tramo = abs(b - a);
    % Calcula el valor mas aproximado
    while(tramo>=tolera & i<=n)
        a = b;
        b = gx(a);
        e=[e b];
        tramo = abs(b-a);
        i = i+1;
    endwhile
    % Valor final
    respuesta = b;
    plot(1:n,e);
endfunction

% Prueba
% funcion gx
gx = @(x) exp(-x);
% Valores iniciales 
a = 0 ; 
b = 1;
% Tolerancia del algoritmo
tolera = 10e-8;
tramos = 101;
% Llamadoa de la funcion
respuesta = PFijo(gx,a,tolera);
printf('Punto Fijo = %f\n', respuesta);