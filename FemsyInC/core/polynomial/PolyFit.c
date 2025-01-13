#include <stdio.h>
#include <stdlib.h>
#include "Poly.h"
#include "PolyHelper.h"
#include <gsl/gsl_linalg.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_permutation.h>
#include "../../models/types.h"

void PolyXYFit(TriangleElementGeometry *ElementInLocalCoordinates, float *functionValuesInPoint, PolyXY OutputPolynomialXY) {
    gsl_matrix *A = gsl_matrix_alloc(3, 3);
    gsl_vector *b = gsl_vector_alloc(3);
    gsl_vector *x = gsl_vector_alloc(3);
    gsl_permutation *p = gsl_permutation_alloc(3);
    int i;
    for (int i = 0; i < 3; i++) {
        gsl_matrix_set(A, i, 0, ElementInLocalCoordinates->nodes[i].x);
        gsl_matrix_set(A, i, 1, ElementInLocalCoordinates->nodes[i].y);
        gsl_matrix_set(A, i, 2, ElementInLocalCoordinates->nodes[i].x * ElementInLocalCoordinates->nodes[i].y);
        gsl_vector_set(b, i, functionValuesInPoint[i]);
    }
    gsl_linalg_LU_decomp(A, p, &i);
    gsl_linalg_LU_solve(A, p, b, x);
    OutputPolynomialXY.coefficients[0] = gsl_vector_get(x, 0);
    OutputPolynomialXY.coefficients[1] = gsl_vector_get(x, 1);
    OutputPolynomialXY.coefficients[2] = gsl_vector_get(x, 2);
    gsl_matrix_free(A);
    gsl_vector_free(b);
    gsl_vector_free(x);
    gsl_permutation_free(p);
}