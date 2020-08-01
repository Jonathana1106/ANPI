function Newtons_method()
    Is = 5e-16;
    Vbe = 0.8;
    f = @(x, Vbe) x*(10*((0.026/x) + 200) + 200) - (2.5 - Vbe);
    dfdx = 2200;
    eps = 10e-100;
    beta =100;
    x0 = 0.001;
    [Ic, no_iterations, Vbe] = Newton(f, dfdx, x0, eps, Is, Vbe, beta);
end

function [Ic, no_iterations, Vbe] = Newton(f, dfdx, x0, eps, Is, Vbe, beta)
    x = x0;
    f_value = f(x, Vbe);
    iteration_counter = 1;
    X_values = [];
    while abs(f_value) > eps && iteration_counter < 10
        x = x - (f_value)/dfdx
        X_values = [X_values x];
        Vbe = 0.026 * log(x/Is);
        f_value = f(x, Vbe);
        iteration_counter = iteration_counter + 1;
    end
    Vbe
    Ic = x
    Ib = Ic/beta
    Ie = ((beta + 1)/beta)*Ic
    no_iterations = iteration_counter -1
    plot(1:no_iterations, X_values)

end

Newtons_method()