function I = simpson(f, a, b)
    %Funcion que obtiene un valor aproximado de la integral de la funcion f en 
    %un intervalo [a, b] utilizando el metodo de la regla de Simpson.
    %Parametros iniciales: 
    % -f: funcion que se desea integrar.
    % -a: punto inicial de integracion de la funcion.
    % -b: punto final de integracion de la funcion.            
    %           
    %Parametros de salida:                           
    % -I: Valor aproximado de la integral de la funcion f en los intervalos [a, b].
    %
    warning('off')
    pkg load symbolic
    syms x;
    var = sym('x');
    f1 = matlabFunction(sym(f));
    pdf = matlabFunction(diff(sym(f1)));
    sdf = matlabFunction(diff(sym(pdf)));
    tdf = matlabFunction(diff(sym(sdf)));
    cdf = matlabFunction(diff(sym(tdf)));
    h = (b - a)/2;
    c = (a + b)/2;
    s = solve(cdf, x);
    i = length(s);
    j = 1;
    ev = [];
    sa = abs(double(cdf(a)));
    sb = abs(double(cdf(b)));
    ev = [ev sa sb];
    while (j<=i)
        si = abs(double(cdf(s(i))));
        ev = [ev si];
        j = j + 1;
    endwhile
    I = (h/3)*(f1(a) + 4*f1(c) + f1(b));
    cota =(((h^5)/90)*max(ev));
endfunction
