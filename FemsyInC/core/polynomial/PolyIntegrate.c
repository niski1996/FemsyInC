//
// Created by kali on 1/2/25.
//
#include "Poly.h"
#include <stdlib.h>
#include <stdio.h>

Poly integratePoly(Poly poly) {
    int new_degree = poly.degree + 1;
    double *new_coefficients = (double *) calloc(new_degree + 1, sizeof(double));
    if (new_coefficients == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    new_coefficients[0] = 0.0; // The constant of integration can be set to 0
    for (int i = 0; i <= poly.degree; i++) {
        new_coefficients[i + 1] = poly.coefficients[i] / (i + 1);
    }

    Poly result = {new_degree, new_coefficients};
    return result;
}
