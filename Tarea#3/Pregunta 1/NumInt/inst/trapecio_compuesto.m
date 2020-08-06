function I = trapecio_compuesto(f, a, b, N)
    %Funcion que obtiene un valor aproximado de la integral de la funcion f en 
    %un intervalo [a, b] utilizando el metodo de la regla del trapecio compuesto.
    %Parametros iniciales: 
    % -f: funcion que se desea integrar.
    % -a: punto inicial de integracion de la funcion.
    % -b: punto final de integracion de la funcion.
    % -N: numero de puntos en el intervalo [a, b].  
    %           
    %Parametros de salida:                           
    % -I: Valor aproximado de la integral de la funcion f en los intervalos [a, b].
    %
    warning('off')
    pkg load symbolic
    h = (b - a)/(N - 1);
    valores = [a];
    x_k = a + h;
    while (x_k) < b
        valores = [valores x_k];
        x_k = x_k + h;
    endwhile
    valores = [valores b];
    syms x;
    var = sym('x');
    f1 = matlabFunction(sym(f));
    pdf = matlabFunction(diff(sym(f1)));
    sdf = matlabFunction(diff(sym(pdf)));
    s = solve(sdf, x);
    i = length(s);
    j = 1;
    ev = [];
    sa = abs(double(sdf(a)));
    sb = abs(double(sdf(b)));
    ev = [ev sa sb];
    while (j < i)
        si = abs(double(sdf(s(j))));
        ev = [ev si];
        j = j + 1;
    endwhile
    sumatoria = 0;
    for i = (1:numel(valores))
        if(i == 1 || i == (numel(valores)))
            sumatoria += f1(valores(i));
        else
            sumatoria += f1(valores(i))*2;
        endif
    endfor
    I = (h/2)*sumatoria;
    cota = (((b-a)*(h^2))/12)*max(ev);
endfunction