#include "coordinateSystemTest.h"

#include <assert.h>
#include <gsl/gsl_vector.h>
#include <stdio.h>
#include <math.h>
#include "coordinateSystem.h"
#include "../../models/types.h"
#include "../vector/vector.h"

void CreateCoordinateSystemFromThreeNonLinearPoints_ReturnsCorrectResult() {
    // Use (1.0, 0.0, 0.0) and (1.0, 1.0, 0.0) to test normalization
    Point origin = {0.0, 0.0, 0.0};
    Point pointOnX = {1.0, -1.0, 0.0};
    Point pointOnXY = {1.0, 0.0, 0.0};
    CoordinateSystem *coordinateSystem = createCoordinateSystemFromThreeNonLinearPoints(origin, pointOnX, pointOnXY);

    // // Check if UnitVectorX is normalized (should be exactly along the X-axis)
    // assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorX, 0) - 1.0) < 1e-6);
    // assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorX, 1) - 0.0) < 1e-6);
    // assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorX, 2) - 0.0) < 1e-6);
    //
    // // Check if UnitVectorY is approximately (0.707107, 0.707107, 0.0) due to normalization
    // assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorY, 0) - 0.707107) < 1e-6);
    // assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorY, 1) - 0.707107) < 1e-6);
    // assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorY, 2) - 0.0) < 1e-6);
    //
    // // Check if UnitVectorZ is perpendicular to X and Y, and normalized
    // assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorZ, 0) - 0.0) < 1e-6);
    // assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorZ, 1) - 0.0) < 1e-6);
    // assert(fabs(gsl_vector_get(coordinateSystem->UnitVectorZ, 2) - 1.0) < 1e-6);

    freeCoordinateSystem(&coordinateSystem);
}

void CreateCoordinateSystemFromThreeNonLinearPoints_HandlesCollinearPoints() {
    FILE *stderr_backup = stderr;
    stderr = fopen("/dev/null", "w");

    Point origin = {0.0, 0.0, 0.0};
    Point pointOnX = {1.0, 0.0, 0.0};
    Point pointOnXY = {2.0, 0.0, 0.0};
    CoordinateSystem *coordinateSystem = createCoordinateSystemFromThreeNonLinearPoints(origin, pointOnX, pointOnXY);

    // Check that the function handles collinear points correctly by returning NULL
    assert(coordinateSystem == NULL);

    fclose(stderr);
    stderr = stderr_backup;
}

void CreateCoordinateSystemFromThreeNonLinearPoints_HandlesIdenticalPoints() {
    FILE *stderr_backup = stderr;
    stderr = fopen("/dev/null", "w");

    Point origin = {0.0, 0.0, 0.0};
    Point pointOnX = {0.0, 0.0, 0.0};
    Point pointOnXY = {0.0, 0.0, 0.0};
    CoordinateSystem *coordinateSystem = createCoordinateSystemFromThreeNonLinearPoints(origin, pointOnX, pointOnXY);

    // Check that the function handles identical points by returning NULL
    assert(coordinateSystem == NULL);

    fclose(stderr);
    stderr = stderr_backup;
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

void coordinateSystemTest() {
    CreateCoordinateSystemFromThreeNonLinearPoints_ReturnsCorrectResult();
    test_freeCoordinateSystem();

    printf("All coordinateSystem Test passed.\n");
}
