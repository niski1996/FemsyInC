//
// Created by kali on 1/10/25.
//

#include "parser.h"

int parse_3_columns_matrix(const char *filepath, gsl_matrix **OutputMatrix, int *OutputRowCount, const char *Format) {
    FILE *file;
    const size_t column_count = 3;
    union {
        int i;
        float f;
    } temp[3];

    if ((file = fopen(filepath, "rt")) == NULL) {
        fprintf(stderr, "Error: Unable to open file %s\n", filepath);
        return -1;
    }

    *OutputRowCount = 0;

    while (fscanf(file, Format, &temp[0].f, &temp[1].f, &temp[2].f) == 3 || fscanf(file, Format, &temp[0].i, &temp[1].i, &temp[2].i) == 3) {
        (*OutputRowCount)++;
    }

    rewind(file);

    *OutputMatrix = gsl_matrix_alloc(*OutputRowCount, column_count);
    if (*OutputMatrix == NULL) {
        fclose(file);
        fprintf(stderr, "Error: Unable to allocate matrix\n");
        return -1;
    }

    size_t row = 0;
    while (fscanf(file, Format, &temp[0].f, &temp[1].f, &temp[2].f) == 3 || fscanf(file, Format, &temp[0].i, &temp[1].i, &temp[2].i) == 3) {
        gsl_matrix_set(*OutputMatrix, row, 0, (float)temp[0].f);
        gsl_matrix_set(*OutputMatrix, row, 1, (float)temp[1].f);
        gsl_matrix_set(*OutputMatrix, row, 2, (float)temp[2].f);
        row++;
    }

    fclose(file);
    return 0;
}
