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

PolyXY multiplyPolysXY(PolyXY poly1, PolyXY poly2) {
    int result_degree = poly1.degree + poly2.degree;
    unsigned int result_element_count = getPascalTriangleElementCount(result_degree + 1);
    double *result_coefficients = (double *)calloc(result_element_count, sizeof(double));
    if (result_coefficients == NULL) {
        fprintf(stderr, "Developer error: Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    unsigned int elementCount1 = getPascalTriangleElementCount(poly1.degree + 1);
    unsigned int elementCount2 = getPascalTriangleElementCount(poly2.degree + 1);

    for (unsigned int i = 0; i < elementCount1; i++) {
        for (unsigned int j = 0; j < elementCount2; j++) {
            int degree_x1 = getPascalTriangleLevelCount(i + 1) - 1;
            int degree_y1 = i - getPascalTriangleNLevelStartIndex(degree_x1 + 1);
            int degree_x2 = getPascalTriangleLevelCount(j + 1) - 1;
            int degree_y2 = j - getPascalTriangleNLevelStartIndex(degree_x2 + 1);

            int result_degree_x = degree_x1 + degree_x2;
            int result_degree_y = degree_y1 + degree_y2;
            int result_index = getPascalTriangleNLevelStartIndex(result_degree_x + result_degree_y + 1) + result_degree_y;

            result_coefficients[result_index] += poly1.coefficients[i] * poly2.coefficients[j];
        }
    }

    PolyXY result = {result_degree, result_coefficients};
    return result;
}



PolyXY scalePolysXY(PolyXY poly, int scale) {
    unsigned int elementCount = getPascalTriangleElementCount(poly.degree + 1);
    double* coeff = scaleCoeff(poly.coefficients, elementCount, scale);
    PolyXY result = createPolyXY(poly.degree, coeff);
    free(coeff);
    return result;
}
