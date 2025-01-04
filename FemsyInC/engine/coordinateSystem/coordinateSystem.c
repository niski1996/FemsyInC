#include "coordinateSystem.h"
#include "../../models/types.h"
#include "../vector/vector.h"
#include <gsl/gsl_vector.h>
#include <gsl/gsl_blas.h>
#include <stdio.h>
#include <stdlib.h>

// Normalize a given vector
static gsl_vector* normalize_vector(gsl_vector* vector) {
    double norm = gsl_blas_dnrm2(vector);
    if (norm == 0.0) {
        fprintf(stderr, "Error: Zero vector cannot be normalized\n");
        gsl_vector_free(vector);
        return NULL;
    }
    gsl_vector_scale(vector, 1.0 / norm);
    return vector;
}


// Create a coordinate system from three non-linear points
CoordinateSystem* createCoordinateSystemFromThreeNonLinearPoints(const Point origin, const Point pointOnX, const Point pointOnXY) {
    CoordinateSystem* coordinateSystemWritenInOldSystem = malloc(sizeof(CoordinateSystem));
    if (coordinateSystemWritenInOldSystem == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    gsl_vector* UnitVectorX = gsl_vector_alloc(3);
    gsl_vector* UnitVectorY = gsl_vector_alloc(3);
    gsl_vector* UnitVectorZ = gsl_vector_alloc(3);
    gsl_vector* VectorXY = gsl_vector_alloc(3);

    // Create and log the unit vector X
    createUnitVectorFromPoints(&origin, &pointOnX, UnitVectorX);
    coordinateSystemWritenInOldSystem->UnitVectorX = UnitVectorX;

    // Create and log the unit vector Z
    createUnitVectorFromPoints(&origin, &pointOnXY, VectorXY);
    coordinateSystemWritenInOldSystem->UnitVectorY = UnitVectorY;
    getUnitVectorOnDirectionOfCrossProduct(UnitVectorX, VectorXY, UnitVectorZ);
    coordinateSystemWritenInOldSystem->UnitVectorZ = UnitVectorZ;

    // Create and log the unit vector Y
    cross_product(UnitVectorZ, UnitVectorX, UnitVectorY);
    coordinateSystemWritenInOldSystem->UnitVectorZ = UnitVectorZ;
    gsl_vector_free(VectorXY);

    return coordinateSystemWritenInOldSystem;
}

// Free the memory allocated for the coordinate system
void freeCoordinateSystem(CoordinateSystem** coordinateSystem) {
    if (coordinateSystem != NULL && *coordinateSystem != NULL) {
        gsl_vector_free((*coordinateSystem)->UnitVectorX);
        gsl_vector_free((*coordinateSystem)->UnitVectorY);
        gsl_vector_free((*coordinateSystem)->UnitVectorZ);
        free(*coordinateSystem);
        *coordinateSystem = NULL;
    }
}

void createTransformationMatrix(const CoordinateSystem *newCoordinateSystemInnOldLayout,
    gsl_matrix *OldToNewTransformationMatrix) {

    // Set the first column of the transformation matrix to UnitVectorX
    gsl_matrix_set_col(OldToNewTransformationMatrix, 0, newCoordinateSystemInnOldLayout->UnitVectorX);

    // Set the second column of the transformation matrix to UnitVectorY
    gsl_matrix_set_col(OldToNewTransformationMatrix, 1, newCoordinateSystemInnOldLayout->UnitVectorY);

    // Set the third column of the transformation matrix to UnitVectorZ
    gsl_matrix_set_col(OldToNewTransformationMatrix, 2, newCoordinateSystemInnOldLayout->UnitVectorZ);
}
