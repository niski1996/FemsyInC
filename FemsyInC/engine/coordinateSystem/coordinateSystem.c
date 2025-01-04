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

// Create a unit vector from two points
static gsl_vector* create_unit_vector(const Point* start, const Point* end) {
    gsl_vector* unitVector = gsl_vector_alloc(3);
    createUnitVectorFromPoints(start, end, unitVector);

    return unitVector;
}

// Calculate the normalized cross product of two vectors
static gsl_vector* calculate_normalized_cross_product(const gsl_vector* u, const gsl_vector* v) {
    gsl_vector* product = gsl_vector_alloc(3);
    cross_product(u, v, product);

    return normalize_vector(product);
}

// Create a coordinate system from three non-linear points
CoordinateSystem* createCoordinateSystemFromThreeNonLinearPoints(Point origin, Point pointOnX, Point pointOnXY) {
    CoordinateSystem* coordinateSystem = (CoordinateSystem*)malloc(sizeof(CoordinateSystem));
    if (coordinateSystem == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    // Create and log the unit vector X
    gsl_vector* UnitVectorX = create_unit_vector(&origin, &pointOnX);
    coordinateSystem->UnitVectorX = UnitVectorX;

    // Create and log the unit vector Y
    gsl_vector* UnitVectorY = create_unit_vector(&origin, &pointOnXY);
    coordinateSystem->UnitVectorY = UnitVectorY;

    // Create and log the unit vector Z (cross product of X and Y)
    gsl_vector* product = gsl_vector_alloc(3);
    cross_product(UnitVectorX, UnitVectorY, product);
    coordinateSystem->UnitVectorZ = product;

    return coordinateSystem;
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