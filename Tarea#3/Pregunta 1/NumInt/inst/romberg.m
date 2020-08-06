function I = romberg(f, a, b, n)
    %Funcion que obtiene un valor aproximado de la integral de la funcion f en 
    %un intervalo [a, b] utilizando el metodo de romberg.
    %Parametros iniciales: 
    % -f: funcion que se desea integrar. funcion en string
    % -a: punto inicial de integracion de la funcion.
    % -b: punto final de integracion de la funcion.
    % -n: numero de puntos en el intervalo [a, b].  
    %             
    %Parametros de salida:                           
    % -I: Valor aproximado de la integral de la funcion f en los intervalos [a, b].

  warning('off');
  R(1, 1) = (b - a) * (evaluate(f, a) + evaluate(f, b));

  for j = 2:n
    h = (b - a)/(2^(j - 1));
    h_km1 = (b - a)/(2^(j - 2)); 
    sumatoria = 0;
    for i = 1:2^(j - 2)
      sumatoria = sumatoria + evaluate(f, a + ((2*i) - 1)*h);
    endfor
    R(j, 1) = (1/2)*(R(j - 1, 1) + h_km1*sumatoria);
    for k = 2:j
      R(j, k) = R(j, k - 1) + ((R(j , k - 1) - R(j - 1,k - 1))/(4^(k - 1) - 1));
    endfor
  endfor
    I = R(n, n);
endfunction

function [g] = evaluate(f, x)
  g = eval(f);
endfunction

