function I = trapecio(f, a, b)
    %Funcion que obtiene un valor aproximado de la integral de la funcion f en 
    %un intervalo [a, b] utilizando el metodo de la regla del trapecio.
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
    h = (b - a);
    s = solve(sdf, x);
    i = length(s);
    j = 1;
    ev = [];
    sa = abs(double(sdf(a)));
    sb = abs(double(sdf(b)));
    ev = [ev sa sb];
    while (j <= i)
        si = abs(double(sdf(s(j))));
        ev = [ev si];
        j = j + 1;
    endwhile
    I = ((h/2)*(f1(b) + f1(a)));
    cota =((h^3)/12)*max(ev);
endfunction