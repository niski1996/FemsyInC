#include <assert.h>
#include <gsl/gsl_vector.h>
#include <stdio.h>
#include "vector.h"
#include <math.h>

void CrossProduct_ReturnsCorrectResult() {
    gsl_vector *u = gsl_vector_alloc(3);
    gsl_vector *v = gsl_vector_alloc(3);
    gsl_vector *product = gsl_vector_alloc(3);

    gsl_vector_set(u, 0, 1.0);
    gsl_vector_set(u, 1, 0.0);
    gsl_vector_set(u, 2, 0.0);

    gsl_vector_set(v, 0, 0.0);
    gsl_vector_set(v, 1, 1.0);
    gsl_vector_set(v, 2, 0.0);

    cross_product(u, v, product);

    assert(gsl_vector_get(product, 0) == 0.0);
    assert(gsl_vector_get(product, 1) == 0.0);
    assert(gsl_vector_get(product, 2) == 1.0);

    gsl_vector_free(u);
    gsl_vector_free(v);
    gsl_vector_free(product);
}

void CrossProduct_HandlesZeroVectors() {
    gsl_vector *u = gsl_vector_alloc(3);
    gsl_vector *v = gsl_vector_alloc(3);
    gsl_vector *product = gsl_vector_alloc(3);

    gsl_vector_set_zero(u);
    gsl_vector_set_zero(v);

    cross_product(u, v, product);

    assert(gsl_vector_get(product, 0) == 0.0);
    assert(gsl_vector_get(product, 1) == 0.0);
    assert(gsl_vector_get(product, 2) == 0.0);

    gsl_vector_free(u);
    gsl_vector_free(v);
    gsl_vector_free(product);
}

void CrossProduct_HandlesParallelVectors() {
    gsl_vector *u = gsl_vector_alloc(3);
    gsl_vector *v = gsl_vector_alloc(3);
    gsl_vector *product = gsl_vector_alloc(3);

    gsl_vector_set(u, 0, 1.0);
    gsl_vector_set(u, 1, 1.0);
    gsl_vector_set(u, 2, 1.0);

    gsl_vector_set(v, 0, 2.0);
    gsl_vector_set(v, 1, 2.0);
    gsl_vector_set(v, 2, 2.0);

    cross_product(u, v, product);

    assert(gsl_vector_get(product, 0) == 0.0);
    assert(gsl_vector_get(product, 1) == 0.0);
    assert(gsl_vector_get(product, 2) == 0.0);

    gsl_vector_free(u);
    gsl_vector_free(v);
    gsl_vector_free(product);
}

void test_createUnitVectorFromPoints_ReturnsCorrectResult() {
    Point start = {0.0, 0.0, 0.0};
    Point end = {1.0, 1.0, 1.0};
    gsl_vector *unitVector = gsl_vector_alloc(3);

    createUnitVectorFromPoints(&start, &end, unitVector);

    double expectedNorm = 1.0 / sqrt(3.0);
    assert(fabs(gsl_vector_get(unitVector, 0) - expectedNorm) < 1e-6);
    assert(fabs(gsl_vector_get(unitVector, 1) - expectedNorm) < 1e-6);
    assert(fabs(gsl_vector_get(unitVector, 2) - expectedNorm) < 1e-6);

    gsl_vector_free(unitVector);
}

void test_createUnitVectorFromPoints_HandlesZeroVector() {
    Point start = {0.0, 0.0, 0.0};
    Point end = {0.0, 0.0, 0.0};
    gsl_vector *unitVector = gsl_vector_alloc(3);

    createUnitVectorFromPoints(&start, &end, unitVector);

    // Since the function should print an error and return without modifying the vector,
    // we expect the unit vector to remain zero.
    assert(gsl_vector_get(unitVector, 0) == 0.0);
    assert(gsl_vector_get(unitVector, 1) == 0.0);
    assert(gsl_vector_get(unitVector, 2) == 0.0);

    gsl_vector_free(unitVector);
}

void vectorTest() {
    CrossProduct_ReturnsCorrectResult();
    CrossProduct_HandlesZeroVectors();
    CrossProduct_HandlesParallelVectors();
    test_createUnitVectorFromPoints_ReturnsCorrectResult();
    test_createUnitVectorFromPoints_HandlesZeroVector();

    printf("All vector tests passed.\n");

}