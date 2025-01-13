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

PolyXY createPolyXY(const int degree, const double *coefficients) {
    const PolyXY poly = createPolyXYWithZeros(degree);
    const unsigned int elementCount = getPascalTriangleElementCount(degree + 1);
    for (int i = 0; i < elementCount; i++) {
        poly.coefficients[i] = coefficients[i];
    }
    return poly;
}

// create XY polynomial with coefficient fitting to degree with values 0.0. tbh handle only allocation an degree
PolyXY createPolyXYWithZeros(const int degree) {
    PolyXY poly;
    poly.degree = degree;
    const unsigned int elementCount = getPascalTriangleElementCount(degree + 1);
    poly.coefficients = (double *)calloc(elementCount, sizeof(double));
    if (poly.coefficients == NULL) {
        fprintf(stderr, "Developer error: Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    return poly;
}