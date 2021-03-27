#include <iostream>
#include "funtras.h"

int main() {
    std::cout << "Hello, World!" << std::endl;

    double fac, expe, expoNUNO, seno, coseno, tangente, logan, logb, powert;

    fac = factorial(7);
    cout << "El factorial de 7 es: " << fac;
    cout << "\n";
    expe = exp_t(2);
    cout << "El resultado de e^2 es: " << expe;
    cout << "\n";
    expoNUNO = varM1(2);
    cout << "El calculo de 2^-1 es: "<< expoNUNO;
    cout << "\n";
    seno = sin_t(1);
    cout << "El seno de 1 es: "<< seno;
    cout << "\n";
    coseno = cos_t(1);
    cout << "El coseno de 1 es: "<< coseno;
    cout << "\n";
    tangente = tan_t(7);
    cout << "La tangente de 7 es: "<< tangente;
    cout << "\n";
    logan = ln_t(2);
    cout << "El logaritmo natural de 2 es: "<< logan;
    cout << "\n";
    logb = log_t(2, 5);
    cout << "El logaritmo en base 5 de 2 es: "<< logb;
    cout << "\n";
    powert = power_t(2, 2);
    cout << "El resultado de 2^2 es: "<< powert;

    return 0;
}
