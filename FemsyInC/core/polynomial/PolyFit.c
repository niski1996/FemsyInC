#include <gsl/gsl_linalg.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_permutation.h>
#include <stdio.h>
#include "../../models/types.h"
#include "Poly.h"

void PolyXYFit(TriangleElementGeometry *ElementInLocalCoordinates, float *functionValuesInPoint, PolyXY *OutputPolynomialXY) {
    if (ElementInLocalCoordinates == NULL || functionValuesInPoint == NULL || OutputPolynomialXY->coefficients == NULL) {
        fprintf(stderr, "Invalid input to PolyXYFit\n");
        return;
    }

    gsl_matrix *A = gsl_matrix_alloc(3, 3);
    gsl_vector *b = gsl_vector_alloc(3);
    gsl_vector *x = gsl_vector_alloc(3);
    gsl_permutation *p = gsl_permutation_alloc(3);
    int s;

    // Fill matrix A and vector b based on the input points and function values
    for (int i = 0; i < 3; i++) {
        gsl_matrix_set(A, i, 0, 1.0);
        gsl_matrix_set(A, i, 1, ElementInLocalCoordinates->nodes[i].x);
        gsl_matrix_set(A, i, 2, ElementInLocalCoordinates->nodes[i].y);
        gsl_vector_set(b, i, functionValuesInPoint[i]);
    }

    // Perform LU decomposition
    if (gsl_linalg_LU_decomp(A, p, &s) != 0) {
        fprintf(stderr, "Matrix is singular\n");
        gsl_matrix_free(A);
        gsl_vector_free(b);
        gsl_vector_free(x);
        gsl_permutation_free(p);
        return;
    }

    // Solve the system
    gsl_linalg_LU_solve(A, p, b, x);

    // Copy the result to the output polynomial coefficients
    for (int i = 0; i < 3; i++) {
        OutputPolynomialXY->coefficients[i] = gsl_vector_get(x, i);
    }

    gsl_matrix_free(A);
    gsl_vector_free(b);
    gsl_vector_free(x);
    gsl_permutation_free(p);
}