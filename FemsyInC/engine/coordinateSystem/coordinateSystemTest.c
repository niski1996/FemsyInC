#include "coordinateSystemTest.h"

#include <assert.h>
#include <gsl/gsl_vector.h>
#include <stdio.h>
#include <math.h>
#include "coordinateSystem.h"
#include "../../models/types.h"
#include "../matrix/matrix.h"

void CreateCoordinateSystemFromThreeNonLinearPoints_ReturnsCorrectResult() {
    Point origin = {0.0, 0.0, 0.0};
    Point pointOnX = {1.0, 1.0, 0.0};
    Point pointOnXY = {-1.0, 1.0, 0.0};
    CoordinateSystem *newCoordinateSystem = createCoordinateSystemFromThreeNonLinearPoints(origin, pointOnX, pointOnXY);

    // Debug prints
    // printf("UnitVectorX: [%f, %f, %f]\n", gsl_vector_get(newCoordinateSystem->UnitVectorX, 0), gsl_vector_get(newCoordinateSystem->UnitVectorX, 1), gsl_vector_get(newCoordinateSystem->UnitVectorX, 2));
    // printf("UnitVectorY: [%f, %f, %f]\n", gsl_vector_get(newCoordinateSystem->UnitVectorY, 0), gsl_vector_get(newCoordinateSystem->UnitVectorY, 1), gsl_vector_get(newCoordinateSystem->UnitVectorY, 2));
    // printf("UnitVectorZ: [%f, %f, %f]\n", gsl_vector_get(newCoordinateSystem->UnitVectorZ, 0), gsl_vector_get(newCoordinateSystem->UnitVectorZ, 1), gsl_vector_get(newCoordinateSystem->UnitVectorZ, 2));

    assert(fabs(gsl_vector_get(newCoordinateSystem->UnitVectorX, 0) - 0.707107) < 1e-4);
    assert(fabs(gsl_vector_get(newCoordinateSystem->UnitVectorX, 1) - 0.707107) < 1e-4);
    assert(fabs(gsl_vector_get(newCoordinateSystem->UnitVectorX, 2) - 0.0) < 1e-4);

    assert(fabs(gsl_vector_get(newCoordinateSystem->UnitVectorY, 0) + 0.707107) < 1e-4);
    assert(fabs(gsl_vector_get(newCoordinateSystem->UnitVectorY, 1) - 0.707107) < 1e-4);
    assert(fabs(gsl_vector_get(newCoordinateSystem->UnitVectorY, 2) - 0.0) < 1e-4);

    assert(fabs(gsl_vector_get(newCoordinateSystem->UnitVectorZ, 0) - 0.0) < 1e-4);
    assert(fabs(gsl_vector_get(newCoordinateSystem->UnitVectorZ, 1) - 0.0) < 1e-4);
    assert(fabs(gsl_vector_get(newCoordinateSystem->UnitVectorZ, 2) - 1.0) < 1e-4);

    freeCoordinateSystem(&newCoordinateSystem);
}


void test_freeCoordinateSystem() {
    // Allocate a CoordinateSystem
    CoordinateSystem *coordinateSystem = malloc(sizeof(CoordinateSystem));
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

void CreateTransformationMatrix_ReturnsCorrectMatrix() {
    Point origin = {0.0, 0.0, 0.0};
    Point pointOnX = {1.0, 1.0, 0.0};
    Point pointOnXY = {-1.0, 1.0, 0.0};
    CoordinateSystem *coordinateSystem = createCoordinateSystemFromThreeNonLinearPoints(origin, pointOnX, pointOnXY);

    gsl_matrix *transformationMatrix = gsl_matrix_alloc(3, 3);
    createTransformationMatrix(coordinateSystem, transformationMatrix);

    assert(fabs(gsl_matrix_get(transformationMatrix, 0, 0) - 0.707107) < 1e-4);
    assert(fabs(gsl_matrix_get(transformationMatrix, 1, 0) - 0.707107) < 1e-4);
    assert(fabs(gsl_matrix_get(transformationMatrix, 2, 0) - 0.0) < 1e-4);

    assert(fabs(gsl_matrix_get(transformationMatrix, 0, 1) + 0.707107) < 1e-4);
    assert(fabs(gsl_matrix_get(transformationMatrix, 1, 1) - 0.707107) < 1e-4);
    assert(fabs(gsl_matrix_get(transformationMatrix, 2, 1) - 0.0) < 1e-4);

    assert(fabs(gsl_matrix_get(transformationMatrix, 0, 2) - 0.0) < 1e-4);
    assert(fabs(gsl_matrix_get(transformationMatrix, 1, 2) - 0.0) < 1e-4);
    assert(fabs(gsl_matrix_get(transformationMatrix, 2, 2) - 1.0) < 1e-4);

    printMatrix(transformationMatrix);
    gsl_matrix_free(transformationMatrix);
    freeCoordinateSystem(&coordinateSystem);
}


void coordinateSystemTest() {
    CreateCoordinateSystemFromThreeNonLinearPoints_ReturnsCorrectResult();
    test_createTransformationMatrix();
    CreateTransformationMatrix_ReturnsCorrectMatrix();
    // test_freeCoordinateSystem();

    printf("All coordinateSystem Test passed.\n");
}
