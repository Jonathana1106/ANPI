clear;
close all;

%{
    Metodo de la Muller
    Entradas
      @param x0: Valor inicial
      @param x1: Valor inicial
      @param x2: Valor inicial
      @param tol: Tolerancia
      @param f: funcion a la cual se le aplicara el algoritmo
    Salidas
      @return x2: valor aproximado de r
      @return _iter: iteraciones necesarias para aproximar r
%}

function [x2, _iter] = muller(f, x0, x1, x2, tol)
  _iter = 0;
  % Repetir hasta que el % de error sea menor que la tolerancia
  while ((abs((x2 - x1) / (x2))) > tol)
    div = ((x0 - x2) * (x1 - x2) * (x0 -x1));
    % Condicion de no realizar division por cero
    if (div == 0)
      disp("Error: division por cero");
      return;
    else
      % Encontrar los valores de a , b y c segun las ecuaciones
      a = ((((x1 - x2)*(f(x0) - f(x2)) - (x0 - x2)*(f(x1) - f(x2))) / div));
      b = ((((x0 - x2)**2)*(f(x1) - f(x2)) - ((x1 - x2)**2)*(f(x0) - f(x2))) / (div));
      c = f(x2);
      disc = (b^2) - (4*a*c);
      % Un discriminante menor que cero generaria resultados complejos que no se abarcan en el codigo
      if (disc < 0)
        disp("El discriminante es menor que cero por lo que no hay solucion real");
        return;
      % Encontrar el valor de r
      else
        div2 = b + b*(sqrt(abs(disc)));
        r = x2 - ((2*c) / (div2));
        _iter = _iter + 1;
        % Actualizar los valores de x0, x1, x2
        x0 = x1;
        x1 = x2;
        x2 = r;
      endif
    endif
  endwhile
  return;
endfunction

% Main
% Valores iniciales
x0 = 2;
x1 = 2.2;
x2 = 1.8;
% Tolerancia
tol = 0.00000000000001
% Funcion a la cual se le aplicara el metodo
func = @(x) sin(x) - x/2;
% Llamado de la funcion
[x2, _iter] = muller (func, x0, x1, x2, tol);
printf('r = %f\nIteraciones = %i', x2, _iter);