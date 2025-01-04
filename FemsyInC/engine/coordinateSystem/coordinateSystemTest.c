#include "coordinateSystemTest.h"

#include <assert.h>
#include <gsl/gsl_vector.h>
#include <stdio.h>
#include <math.h>
#include "coordinateSystem.h"
#include "../../models/types.h"
#include "../vector/vector.h"

void CreateCoordinateSystemFromThreeNonLinearPoints_ReturnsCorrectResult() {
    Point origin = {0.0, 0.0, 0.0};
    Point pointOnX = {1.0, 0.0, 0.0};
    Point pointOnXY = {1.0, 1.0, 0.0};
    CoordinateSystem *coordinateSystem = createCoordinateSystemFromThreeNonLinearPoints(origin, pointOnX, pointOnXY);

    // Debug prints
    printf("UnitVectorX: [%f, %f, %f]\n", gsl_vector_get(coordinateSystem->UnitVectorX, 0), gsl_vector_get(coordinateSystem->UnitVectorX, 1), gsl_vector_get(coordinateSystem->UnitVectorX, 2));
    printf("UnitVectorY: [%f, %f, %f]\n", gsl_vector_get(coordinateSystem->UnitVectorY, 0), gsl_vector_get(coordinateSystem->UnitVectorY, 1), gsl_vector_get(coordinateSystem->UnitVectorY, 2));
    printf("UnitVectorZ: [%f, %f, %f]\n", gsl_vector_get(coordinateSystem->UnitVectorZ, 0), gsl_vector_get(coordinateSystem->UnitVectorZ, 1), gsl_vector_get(coordinateSystem->UnitVectorZ, 2));

    assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorX, 0) - 1.0) < 1e-6);
    assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorX, 1) - 0.0) < 1e-6);
    assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorX, 2) - 0.0) < 1e-6);

    assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorY, 0) - 0.0) < 1e-6);
    assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorY, 1) - 1.0) < 1e-6);
    assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorY, 2) - 0.0) < 1e-6);

    assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorZ, 0) - 0.0) < 1e-6);
    assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorZ, 1) - 0.0) < 1e-6);
    assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorZ, 2) - 1.0) < 1e-6);

    freeCoordinateSystem(&coordinateSystem);
}


void test_freeCoordinateSystem() {
    // Allocate a CoordinateSystem
    CoordinateSystem *coordinateSystem = (CoordinateSystem *)malloc(sizeof(CoordinateSystem));
    if (coordinateSystem == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    coordinateSystem->UnitVectorX = gsl_vector_alloc(3);
    coordinateSystem->UnitVectorY = gsl_vector_alloc(3);
    coordinateSystem->UnitVectorZ = gsl_vector_alloc(3);

    // Free the CoordinateSystem
    freeCoordinateSystem(&coordinateSystem);

    // Check that the CoordinateSystem pointer is NULL after freeing
    assert(coordinateSystem == NULL);
}

void test_createTransformationMatrix() {
    Point origin = {0.0, 0.0, 0.0};
    Point pointOnX = {1.0, 0.0, 0.0};
    Point pointOnXY = {1.0, 1.0, 0.0};
    CoordinateSystem *coordinateSystem = createCoordinateSystemFromThreeNonLinearPoints(origin, pointOnX, pointOnXY);

    gsl_matrix *transformationMatrix = gsl_matrix_alloc(3, 3);
    createTransformationMatrix(coordinateSystem, transformationMatrix);

    assert(fabs(gsl_matrix_get(transformationMatrix, 0, 0) - 1.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix, 1, 0) - 0.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix, 2, 0) - 0.0) < 1e-6);

    assert(fabs(gsl_matrix_get(transformationMatrix, 0, 1) - 0.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix, 1, 1) - 1.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix, 2, 1) - 0.0) < 1e-6);

    assert(fabs(gsl_matrix_get(transformationMatrix, 0, 2) - 0.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix, 1, 2) - 0.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix, 2, 2) - 1.0) < 1e-6);

    gsl_matrix_free(transformationMatrix);
    freeCoordinateSystem(&coordinateSystem);
}


void coordinateSystemTest() {
    CreateCoordinateSystemFromThreeNonLinearPoints_ReturnsCorrectResult();
    test_createTransformationMatrix();
    test_freeCoordinateSystem();

    printf("All coordinateSystem Test passed.\n");
}
