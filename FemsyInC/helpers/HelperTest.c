//
// Created by kali on 1/3/25.
//
#include <assert.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <fcntl.h>

#include "HelperTest.h"
#include "../helpers/helper.h"
#include "../models/types.h"
#include "../engine/vector/vector.h"
#include "../engine/coordinateSystem/coordinateSystem.h"

void ForMatrixOfElementInsertNodesCoordinates_ReturnsCorrectCoordinates() {
    Point nodes[] = {
        {0.0, 0.0, 0.0},
        {1.0, 0.0, 0.0},
        {0.0, 1.0, 0.0},
        {1.0, 1.0, 0.0}
    };

    unsigned int elements[] = {
        0, 1, 2,
        1, 3, 2
    };

    int nodesCount = 4;
    TriangleElementGeometry *coords = ForMatrixOfElementInsertNodesCoordinates(elements, 2, nodes, &nodesCount);

    assert(coords != NULL);
    assert(coords[0].nodes[0].x == 0.0 && coords[0].nodes[0].y == 0.0 && coords[0].nodes[0].z == 0.0);
    assert(coords[0].nodes[1].x == 1.0 && coords[0].nodes[1].y == 0.0 && coords[0].nodes[1].z == 0.0);
    assert(coords[0].nodes[2].x == 0.0 && coords[0].nodes[2].y == 1.0 && coords[0].nodes[2].z == 0.0);

    assert(coords[1].nodes[0].x == 1.0 && coords[1].nodes[0].y == 0.0 && coords[1].nodes[0].z == 0.0);
    assert(coords[1].nodes[1].x == 1.0 && coords[1].nodes[1].y == 1.0 && coords[1].nodes[1].z == 0.0);
    assert(coords[1].nodes[2].x == 0.0 && coords[1].nodes[2].y == 1.0 && coords[1].nodes[2].z == 0.0);

    free(coords);
}

void ForMatrixOfElementInsertNodesCoordinates_HandlesEmptyElements() {
    Point nodes[] = {
        {0.0, 0.0, 0.0},
        {1.0, 0.0, 0.0},
        {0.0, 1.0, 0.0},
        {1.0, 1.0, 0.0}
    };

    unsigned int elements[] = {};

    int nodesCount = 4;
    TriangleElementGeometry *coords = ForMatrixOfElementInsertNodesCoordinates(elements, 0, nodes, &nodesCount);

    assert(coords == NULL);
}

void ForMatrixOfElementInsertNodesCoordinates_HandlesNullNodes() {
    unsigned int elements[] = {
        0, 1, 2,
        1, 3, 2
    };

    int nodesCount = 0;
    TriangleElementGeometry *coords = ForMatrixOfElementInsertNodesCoordinates(elements, 2, NULL, &nodesCount);

    assert(coords == NULL);
}

void ForMatrixOfElementCreateCo_planarCoordinateSystem_ReturnsCorrectCoordinateSystems() {
    TriangleElementGeometry elements[2] = {
        {{{0.0, 0.0, 0.0}, {1.0, 0.0, 0.0}, {0.0, 1.0, 0.0}}},
        {{{1.0, 1.0, 0.0}, {2.0, 1.0, 0.0}, {1.0, 2.0, 0.0}}}
    };

    CoordinateSystem** coordinateSystemCollection = ForMatrixOfElementCreateCo_planarCoordinateSystem(elements, 2);

    assert(coordinateSystemCollection != NULL);
    assert(coordinateSystemCollection[0] != NULL);
    assert(coordinateSystemCollection[1] != NULL);

    freeCoordinateSystem(&coordinateSystemCollection[0]);
    freeCoordinateSystem(&coordinateSystemCollection[1]);
    free(coordinateSystemCollection);
}


void ForMatrixOfElementCreateCo_planarCoordinateSystem_ReturnsNULLForFailedAllocation() {
    CoordinateSystem** coordinateSystems = ForMatrixOfElementCreateCo_planarCoordinateSystem(NULL, UINT_MAX);
    assert(coordinateSystems == NULL);
}

void TransformPointToNewCoordinateSystem_ReturnsCorrectCoordinates() {
    Point point = {1.0, 2.0, 3.0};
    gsl_matrix *transformationMatrix = gsl_matrix_alloc(3, 3);
    gsl_matrix_set_identity(transformationMatrix);
    Point result;

    TransformPointToNewCoordinateSystem(&point, transformationMatrix, &result);

    assert(result.x == 1.0);
    assert(result.y == 2.0);
    assert(result.z == 3.0);

    gsl_matrix_free(transformationMatrix);
}

void TransformPointToNewCoordinateSystem_HandlesZeroMatrix() {
    Point point = {1.0, 2.0, 3.0};
    gsl_matrix *transformationMatrix = gsl_matrix_alloc(3, 3);
    gsl_matrix_set_zero(transformationMatrix);
    Point result;

    TransformPointToNewCoordinateSystem(&point, transformationMatrix, &result);

    assert(result.x == 0.0);
    assert(result.y == 0.0);
    assert(result.z == 0.0);

    gsl_matrix_free(transformationMatrix);
}

void TransformElementGeometryToNewCoordinateSystem_ReturnsCorrectCoordinates() {
    TriangleElementGeometry triangleElementGeometry = {
        .nodes = {
            {1.0, 2.0, 3.0},
            {4.0, 5.0, 6.0},
            {7.0, 8.0, 9.0}
        }
    };
    gsl_matrix *transformationMatrix = gsl_matrix_alloc(3, 3);
    gsl_matrix_set_identity(transformationMatrix);
    TriangleElementGeometry result;

    transformElementGeometryToNewCoordinateSystem(&triangleElementGeometry, transformationMatrix, &result);

    assert(result.nodes[0].x == 1.0);
    assert(result.nodes[0].y == 2.0);
    assert(result.nodes[0].z == 3.0);
    assert(result.nodes[1].x == 4.0);
    assert(result.nodes[1].y == 5.0);
    assert(result.nodes[1].z == 6.0);
    assert(result.nodes[2].x == 7.0);
    assert(result.nodes[2].y == 8.0);
    assert(result.nodes[2].z == 9.0);

    gsl_matrix_free(transformationMatrix);
}

void TransformElementGeometryToNewCoordinateSystem_HandlesZeroMatrix() {
    TriangleElementGeometry triangleElementGeometry = {
        .nodes = {
            {1.0, 2.0, 3.0},
            {4.0, 5.0, 6.0},
            {7.0, 8.0, 9.0}
        }
    };
    gsl_matrix *transformationMatrix = gsl_matrix_alloc(3, 3);
    gsl_matrix_set_zero(transformationMatrix);
    TriangleElementGeometry result;

    transformElementGeometryToNewCoordinateSystem(&triangleElementGeometry, transformationMatrix, &result);

    assert(result.nodes[0].x == 0.0);
    assert(result.nodes[0].y == 0.0);
    assert(result.nodes[0].z == 0.0);
    assert(result.nodes[1].x == 0.0);
    assert(result.nodes[1].y == 0.0);
    assert(result.nodes[1].z == 0.0);
    assert(result.nodes[2].x == 0.0);
    assert(result.nodes[2].y == 0.0);
    assert(result.nodes[2].z == 0.0);

    gsl_matrix_free(transformationMatrix);
}



void HelperTest() {
    TransformPointToNewCoordinateSystem_ReturnsCorrectCoordinates();
    TransformPointToNewCoordinateSystem_HandlesZeroMatrix();
    TransformElementGeometryToNewCoordinateSystem_ReturnsCorrectCoordinates();
    TransformElementGeometryToNewCoordinateSystem_HandlesZeroMatrix();
    ForMatrixOfElementInsertNodesCoordinates_ReturnsCorrectCoordinates();
    ForMatrixOfElementInsertNodesCoordinates_HandlesEmptyElements();
    ForMatrixOfElementInsertNodesCoordinates_HandlesNullNodes();
    ForMatrixOfElementCreateCo_planarCoordinateSystem_ReturnsCorrectCoordinateSystems();
    // ForMatrixOfElementCreateCo_planarCoordinateSystem_ReturnsNULLForFailedAllocation();


    printf("All helper tests passed.\n");
}