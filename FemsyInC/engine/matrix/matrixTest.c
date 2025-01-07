//
// Created by kali on 1/7/25.
//

#include "matrixTest.h"
#include <assert.h>
#include <gsl/gsl_matrix.h>
#include <stdio.h>
#include "matrix.h"

void PrintMatrix_PrintsCorrectly() {
    gsl_matrix *matrix = gsl_matrix_alloc(2, 2);
    gsl_matrix_set(matrix, 0, 0, 1.0);
    gsl_matrix_set(matrix, 0, 1, 2.0);
    gsl_matrix_set(matrix, 1, 0, 3.0);
    gsl_matrix_set(matrix, 1, 1, 4.0);

    printf("Expected output:\n1.000000 2.000000 \n3.000000 4.000000 \n");
    printf("Actual output:\n");
    printMatrix(matrix);

    gsl_matrix_free(matrix);
}

void PrintMatrix_EmptyMatrix() {
    gsl_matrix *matrix = gsl_matrix_alloc(0, 0);

    printf("Expected output:\n");
    printf("Actual output:\n");
    printMatrix(matrix);

    gsl_matrix_free(matrix);
}

void PrintMatrix_SingleElementMatrix() {
    gsl_matrix *matrix = gsl_matrix_alloc(1, 1);
    gsl_matrix_set(matrix, 0, 0, 5.0);

    printf("Expected output:\n5.000000 \n");
    printf("Actual output:\n");
    printMatrix(matrix);

    gsl_matrix_free(matrix);
}

void matrixTest() {
    PrintMatrix_PrintsCorrectly();
    PrintMatrix_EmptyMatrix();
    PrintMatrix_SingleElementMatrix();

    printf("All matrixHelper tests passed.\n");
}