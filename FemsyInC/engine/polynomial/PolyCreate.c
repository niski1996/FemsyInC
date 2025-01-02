#include <stdio.h>
#include <stdlib.h>
#include "Poly.h"
#include "PolyHelper.h"

Poly createPoly(int degree, double *coefficients) {
    Poly poly;
    poly.degree = degree;
    poly.coefficients = (double *)calloc((degree + 1), sizeof(double));
    if (poly.coefficients == NULL) {
        fprintf(stderr, "Developer error:  Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i <= degree; i++) {
        poly.coefficients[i] = coefficients[i];
    }
    return poly;
}
PolyXY createPolXY(int degree, double *coefficients) {
    PolyXY poly;
    poly.degree = degree;
    poly.coefficients = (double *)calloc(getPascalTriangleLevelCount(degree), sizeof(double));
    if (poly.coefficients == NULL) {
        fprintf(stderr, "Developer error: Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i <= degree; i++) {
        poly.coefficients[i] = coefficients[i];
    }
    return poly;
}