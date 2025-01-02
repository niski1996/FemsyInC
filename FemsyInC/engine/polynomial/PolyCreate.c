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

PolyXY createPolyXY(int degree, double *coefficients) {
    PolyXY poly;
    poly.degree = degree;
    unsigned int elementCount = getPascalTriangleElementCount(degree + 1);
    poly.coefficients = (double *)calloc(elementCount, sizeof(double));
    if (poly.coefficients == NULL) {
        fprintf(stderr, "Developer error: Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < elementCount; i++) {
        poly.coefficients[i] = coefficients[i];
    }
    return poly;
}