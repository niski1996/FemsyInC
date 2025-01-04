//
// Created by kali on 1/4/25.
//
#include "matrix.h"
void printMatrix(const gsl_matrix *matrix) {
    for (size_t i = 0; i < matrix->size1; ++i) {
        for (size_t j = 0; j < matrix->size2; ++j) {
            printf("%f ", gsl_matrix_get(matrix, i, j));
        }
        printf("\n");
    }
}
