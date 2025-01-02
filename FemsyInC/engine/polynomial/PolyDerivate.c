//
// Created by kali on 1/2/25.
//
#include "Poly.h"
#include <stdlib.h>
#include <stdio.h>

Poly derivatePoly(Poly poly) {
    if (poly.degree == 0) {
        double *new_coefficients = (double *)calloc(1, sizeof(double));
        if (new_coefficients == NULL) {
            fprintf(stderr, "Memory allocation failed\n");
            exit(EXIT_FAILURE);
        }
        new_coefficients[0] = 0.0;
        Poly result = {0, new_coefficients};
        return result;
    }

    int new_degree = poly.degree - 1;
    double *new_coefficients = (double *)calloc(new_degree + 1, sizeof(double));
    if (new_coefficients == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 1; i <= poly.degree; i++) {
        new_coefficients[i - 1] = poly.coefficients[i] * i;
    }

    Poly result = {new_degree, new_coefficients};
    return result;
}