#include <stdio.h>
#include <stdlib.h>
#include "Poly.h"
#include "PolyHepler.h"

Poly multiplyPolys(Poly poly1, Poly poly2) {
    int result_degree = poly1.degree + poly2.degree;
    double *result_coefficients = calloc(result_degree + 1, sizeof(double));
    if (result_coefficients == NULL) {
        fprintf(stderr, "Developer error: Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i <= poly1.degree; i++) {
        for (int j = 0; j <= poly2.degree; j++) {
            result_coefficients[i + j] += poly1.coefficients[i] * poly2.coefficients[j];
        }
    }

    Poly result = {result_degree, result_coefficients};
    return result;
}

static double* scaleCoeff(double* coeff, unsigned int numberOfCoeff1, int scale){
    double *result_coefficients = calloc(numberOfCoeff1, sizeof(double));
    if (result_coefficients == NULL) {
        fprintf(stderr, "Developer error: Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i <= numberOfCoeff1; i++) {
        result_coefficients[i] += coeff[i] * scale;
    }

    return result_coefficients;
}


Poly scalePoly(Poly poly, int scale){

    Poly result = {poly.degree, scaleCoeff(poly.coefficients, poly.degree+1, scale)};
    return result;
}

PolyXY scalePoly(PolyXY poly, int scale){

    PolyXY result = {poly.degree, scaleCoeff(poly.coefficients, getPascalTriangleElementCount(poly.degree), scale)};
    return result;
}
