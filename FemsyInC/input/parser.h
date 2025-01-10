//
// Created by kali on 1/10/25.
//

#ifndef PARSER_H
#define PARSER_H

#include <gsl/gsl_matrix_double.h>

int parse_3_columns_matrix(
    const char *filepath,
    gsl_matrix **OutputMatrix,
    int *OutputRowCount,
    const char *Format);
#endif //PARSER_H
