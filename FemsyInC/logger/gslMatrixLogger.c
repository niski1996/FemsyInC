//
// Created by kali on 1/10/25.
//

#include <gsl/gsl_matrix_double.h>
#include "logger.h"


void logMatrix(const gsl_matrix *matrix) {
    logDatetime();
    FILE *file = fopen(LogName, "wa");
    for (size_t i = 0; i < matrix->size1; ++i) {
        for (size_t j = 0; j < matrix->size2; ++j) {
            fprintf(file,"%f ", gsl_matrix_get(matrix, i, j));
        }
        printf("\n");
    }
}
