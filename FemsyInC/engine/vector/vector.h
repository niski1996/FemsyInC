//
// Created by kali on 1/3/25.
//

#ifndef VECTOR_H
#define VECTOR_H
#include <gsl/gsl_vector.h>
#include <gsl/gsl_blas.h>
#include "../../models/types.h"

void cross_product(const gsl_vector *u, const gsl_vector *v, gsl_vector *product);
void createUnitVectorFromPoints(const Point *start, const Point *end, gsl_vector *outputUnitVector);
#endif //VECTOR_H
