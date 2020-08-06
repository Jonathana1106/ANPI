function I = simpson_compuesto(f, a, b, N)
    %Funcion que obtiene un valor aproximado de la integral de la funcion f en 
    %un intervalo [a, b] utilizando el metodo de la regla del simpson compuesto.
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
    format long;
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
    dfp = matlabFunction(diff(sym(f1)));
    dfs = matlabFunction(diff(sym(dfp)));
    dft = matlabFunction(diff(sym(dfs)));
    dfc = matlabFunction(diff(sym(dft)));
    s = solve(dfc, x);
    i = length(s);
    j = 1;
    ev = [];
    sa = abs(double(dfc(a)));
    sb = abs(double(dfc(b)));
    ev = [ev sa sb];
    while (j < i)
        si = abs(double(dfc(s(j))));
        ev = [ev si];
        j = j + 1;
    endwhile
    respargrande = 0;
    sumatoriapar = 0;
    sumatoriaimpar = 0;
    for i = (1:numel(valores))
        if(i == 1 || i == (numel(valores)))
            respargrande += f1(valores(i));
        elseif(mod(i, 2) == 0)
            sumatoriaimpar += f1(valores(i));
        else
            sumatoriapar += f1(valores(i));
        endif
    endfor
    respargrande = respargrande + (2*sumatoriapar) + (4*sumatoriaimpar);
    I = (h/3)*respargrande;
    cota =(((b-a)*(h^4))/180)*max(ev);
endfunction