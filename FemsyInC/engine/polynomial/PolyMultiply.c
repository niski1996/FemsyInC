#include <stdio.h>
#include <stdlib.h>
#include "Poly.h"
#include "PolyHelper.h"

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

static double* scaleCoeff(double* coeff, unsigned int numberOfCoeff, int scale) {
    if (coeff == NULL || numberOfCoeff == 0) {
        fprintf(stderr, "Invalid input to scaleCoeff\n");
        return NULL;
    }

    double *result_coefficients = calloc(numberOfCoeff, sizeof(double));
    if (result_coefficients == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    for (unsigned int i = 0; i < numberOfCoeff; i++) {
        result_coefficients[i] = coeff[i] * scale;
    }

    return result_coefficients;
}



Poly scalePoly(Poly poly, int scale) {
    double* coeff = scaleCoeff(poly.coefficients, poly.degree + 1, scale);
    Poly result = createPoly(poly.degree, coeff);
    free(coeff);
    return result;
}

// PolyXY scalePolyXY(PolyXY poly, int scale){
//
//     double* coeff = scaleCoeff(poly.coefficients, getPascalTriangleElementCount(poly.degree), scale);
//     PolyXY result = {poly.degree, scaleCoeff(poly.coefficients, coeff, scale)};
//     return result;
// }
