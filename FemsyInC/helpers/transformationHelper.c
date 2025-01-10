//
// Created by kali on 1/4/25.
//
#include "helper.h"
#include "../models/types.h"
#include "../core/vector/vector.h"
#include "../core/coordinateSystem/coordinateSystem.h"
#include <stdlib.h>


void ForMatrixOfElementCreateCo_planarCoordinateSystem(
    const TriangleElementGeometry *triangleElementGeometries,
    const unsigned int elements_count,
    CoordinateSystem** outputCoordinateSystemCollection) {
    if (elements_count == 0) {
        return;
    }

    for (unsigned int i = 0; i < elements_count; ++i) {
        Point origin = triangleElementGeometries[i].nodes[0];
        Point pointOnX = triangleElementGeometries[i].nodes[1];
        Point pointOnXY = triangleElementGeometries[i].nodes[2];
        // Create the coordinate system for the current element
        outputCoordinateSystemCollection[i] = createCoordinateSystemFromThreeNonLinearPoints(origin, pointOnX, pointOnXY);

    }
}
void TransformPointToNewCoordinateSystem(
    const Point *point,
    const gsl_matrix *transformationMatrix,
    Point *result) {

    // Create a 3x1 matrix for the point
    gsl_matrix *pointMatrix = gsl_matrix_alloc(3, 1);
    gsl_matrix_set(pointMatrix, 0, 0, point->x);
    gsl_matrix_set(pointMatrix, 1, 0, point->y);
    gsl_matrix_set(pointMatrix, 2, 0, point->z);

    // Create a 3x1 matrix for the result
    gsl_matrix *resultMatrix = gsl_matrix_alloc(3, 1);

    // Multiply the transformation matrix with the point matrix
    gsl_blas_dgemm(CblasNoTrans, CblasNoTrans, 1.0, transformationMatrix, pointMatrix, 0.0, resultMatrix);

    // Set the result point
    result->x = gsl_matrix_get(resultMatrix, 0, 0);
    result->y = gsl_matrix_get(resultMatrix, 1, 0);
    result->z = gsl_matrix_get(resultMatrix, 2, 0);

    // Free the allocated matrices
    gsl_matrix_free(pointMatrix);
    gsl_matrix_free(resultMatrix);
}

void transformElementGeometryToNewCoordinateSystem(
    const TriangleElementGeometry *triangleElementGeometry,
    const gsl_matrix *transformationMatrix,
    TriangleElementGeometry *result) {

    TransformPointToNewCoordinateSystem(&triangleElementGeometry->nodes[0], transformationMatrix, &result->nodes[0]);
    TransformPointToNewCoordinateSystem(&triangleElementGeometry->nodes[1], transformationMatrix, &result->nodes[1]);
    TransformPointToNewCoordinateSystem(&triangleElementGeometry->nodes[2], transformationMatrix, &result->nodes[2]);
}