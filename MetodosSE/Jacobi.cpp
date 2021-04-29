#include <iostream>
#include <armadillo>

using namespace std;
using namespace arma;

/**
 * @param matrizD: matriz de coeficientes
 * @param vectorTI: vector de terminos independientes
 * @param xInicial: vector de valores iniciales
 * @param MAXIT: cantidad de iteraciones maximas
 * @param TOL: tolerancia de la respuesta
 * @return tuple<vec, double>: vector solucion, error de la solucion 
 */
tuple<vec, double> jacobi(mat matrizD, vec vectorTI, vec xInicial, int MAXIT, double TOL) {

    mat D (size(matrizD), fill::zeros);
    mat U (size(matrizD), fill::zeros);
    mat L (size(matrizD), fill::zeros);

    for(int i = 0; i < matrizD.n_rows; i++) {
        for(int j = 0; j < matrizD.n_cols; j++) {
            if(j < i) {
                L(i, j) = matrizD(i, j);
            }
            else if(j > i) {
                U(i, j) = matrizD(i, j);
            }
            else if(i == j) {
                D(i, j) = matrizD(i, j);
            }
            else {
                cout << "Error" << endl;
            }
        }
    }

    vec xk = xInicial;
    vec xk1;
    int iter = 0;
    double err = TOL + 1;

    while(iter < MAXIT) {
        xk1 = ((-D.i())*(L + U)*(xk)) + ((D.i())*(vectorTI));
        xk = xk1;
        err = norm(matrizD*xk-vectorTI);

        if(err < TOL) {
            break;
        }
        else {
            iter = iter + 1;
        }
    }
    return make_tuple(xk, err);
}

/**
 * Ejemplo numerico
 */
int main() {
    tuple<vec, double> testJ = jacobi("5 1 1; 1 5 1; 1 1 5", "7 7 7", "0 0 0", 100, 0.000001);
    cout << "Aproximacion: \n" << get<0>(testJ) << endl;
    cout << "Error: " << get<1>(testJ) << endl;
    return 0;
}