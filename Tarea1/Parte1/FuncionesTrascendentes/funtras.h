#ifndef FUNCIONESTRASCENDENTES_FUNTRAS_H
#define FUNCIONESTRASCENDENTES_FUNTRAS_H

#include <iostream>
using namespace std;

const double TOL = 0.00000001;

/**
 * Metodo que se encarga de calcular el calculo de la operacion
 * factorial de un numero
 * @param num: numero al que se le desea encontrar su factorial
 * @return numfact: factorial del numero ingresado
 */
double factorial(int num) {
    double numfact = 1;
    if (num < 0) {
        cout << "Error, en numero ingresado debe ser mayor o igual a cero";
    } else if (num == 0) {
        return numfact;
    }
    else {
        for(int i = num; i > 0; i--) {
            numfact = numfact * i;
        }
    }
    cout << numfact;
    return numfact;
}

#endif //FUNCIONESTRASCENDENTES_FUNTRAS_H