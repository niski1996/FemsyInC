//
// Created by kali on 1/4/25.
//
#include "vector.h"
void createUnitVectorFromPoints(const Point *start, const Point *end, gsl_vector *outputUnitVector) {
    // Calculate the vector from start to end
    gsl_vector_set(outputUnitVector, 0, end->x - start->x);
    gsl_vector_set(outputUnitVector, 1, end->y - start->y);
    gsl_vector_set(outputUnitVector, 2, end->z - start->z);

    // Calculate the norm of the vector
    double norm = gsl_blas_dnrm2(outputUnitVector);

    // Check for zero vector
    if (norm == 0.0) {
        fprintf(stderr, "Error: Zero vector cannot be normalized\n");
        return;
    }

    // Normalize the vector to get the unit vector
    gsl_vector_scale(outputUnitVector, 1.0 / norm);
}