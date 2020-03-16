clear;
close all;

%{
    Metodo de la Falsa Posicion
    Entradas
      @param a: limite inferior del intervalo
      @param b: limite superior del intervalo
      @param tol: tolerencia del algoritmo
      @param f: funcion a la cual se le aplicara el algoritmo
    Salidas
      @return xk: valor aproximado de x
      @return iter: iteraciones necesarias para aproximar x
%}


function [xk, iter] = falsePosition (a, b, tol, f)
  % Validar la condicion para encontrar el cero
  if (f(a) * f(b) < 0)
    % Valor inicial de x_k y x_{k-1}
    xk_1 = b;
    xk = b - (b - a) / (f(b) - f(a)) * f(b);
    iter = 2;
    % Repetir hasta que el x se acerque al cero
    while ((abs((xk - xk_1) / xk)) > tol)
      ck = 0;
      % Verificar cual es el nuevo intervalo de la funcion
      % y el valor de ck
      if (f(a) * f(xk) < 0)
        b = xk;
        ck = a;
      else
        a = xk;
        ck = b;
      endif
      % Calcular el nuevo valor con el metodo de la secante
      xAprox = xk - (xk - ck) / (f(xk) - f(ck)) * f(xk);
      xk_1 = xk;
      xk = xAprox;
      iter = iter + 1;
    endwhile
  else
    error("Condiciones no garantizan el cero de la funcion");
  endif
  return;
endfunction


% Main
% Limites
a = 0.5;
b = pi / 4;
% Tolerancia
tol = 0.00001;
% Funcion a la cual se le aplicara el metodo
func = @(x) cos(x)-x;
% Llamado de la funcion
[xk, iter] = falsePosition (a, b, tol, func);
printf('xk = %f\nIteraciones = %i', xk, iter);
