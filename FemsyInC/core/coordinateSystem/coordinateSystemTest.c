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

void ForCollectionOfCoordinateSystemsCreateTransformationMatrices_CreatesCorrectMatrices() {
    Point origin1 = {0.0, 0.0, 0.0};
    Point pointOnX1 = {1.0, 0.0, 0.0};
    Point pointOnXY1 = {0.0, 1.0, 0.0};
    CoordinateSystem *coordinateSystem1 = createCoordinateSystemFromThreeNonLinearPoints(origin1, pointOnX1, pointOnXY1);

    Point origin2 = {1.0, 1.0, 1.0};
    Point pointOnX2 = {2.0, 1.0, 1.0};
    Point pointOnXY2 = {1.0, 2.0, 1.0};
    CoordinateSystem *coordinateSystem2 = createCoordinateSystemFromThreeNonLinearPoints(origin2, pointOnX2, pointOnXY2);

    const CoordinateSystem* coordinateSystems[] = {coordinateSystem1, coordinateSystem2};
    unsigned int count = 2;

    gsl_matrix *transformationMatrix1 = gsl_matrix_alloc(3, 3);
    gsl_matrix *transformationMatrix2 = gsl_matrix_alloc(3, 3);
    gsl_matrix *OutputTransformationMatrices[] = {transformationMatrix1, transformationMatrix2};

    createTransformationMatrixCollectionFromGlobalToLocalCoordinateSystem(coordinateSystems, count, OutputTransformationMatrices);

    // Validate the first transformation matrix
    assert(fabs(gsl_matrix_get(transformationMatrix1, 0, 0) - 1.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix1, 1, 0) - 0.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix1, 2, 0) - 0.0) < 1e-6);

    assert(fabs(gsl_matrix_get(transformationMatrix1, 0, 1) - 0.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix1, 1, 1) - 1.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix1, 2, 1) - 0.0) < 1e-6);

    assert(fabs(gsl_matrix_get(transformationMatrix1, 0, 2) - 0.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix1, 1, 2) - 0.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix1, 2, 2) - 1.0) < 1e-6);

    // Validate the second transformation matrix
    assert(fabs(gsl_matrix_get(transformationMatrix2, 0, 0) - 1.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix2, 1, 0) - 0.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix2, 2, 0) - 0.0) < 1e-6);

    assert(fabs(gsl_matrix_get(transformationMatrix2, 0, 1) - 0.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix2, 1, 1) - 1.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix2, 2, 1) - 0.0) < 1e-6);

    assert(fabs(gsl_matrix_get(transformationMatrix2, 0, 2) - 0.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix2, 1, 2) - 0.0) < 1e-6);
    assert(fabs(gsl_matrix_get(transformationMatrix2, 2, 2) - 1.0) < 1e-6);

    gsl_matrix_free(transformationMatrix1);
    gsl_matrix_free(transformationMatrix2);
    freeCoordinateSystem(&coordinateSystem1);
    freeCoordinateSystem(&coordinateSystem2);
}


void coordinateSystemTest() {
    CreateCoordinateSystemFromThreeNonLinearPoints_ReturnsCorrectResult();
    test_createTransformationMatrix();
    CreateTransformationMatrix_ReturnsCorrectMatrix();
    ForCollectionOfCoordinateSystemsCreateTransformationMatrices_CreatesCorrectMatrices();
    // test_freeCoordinateSystem();

    printf("All coordinateSystem Test passed.\n");
}
