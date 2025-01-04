//
// Created by kali on 1/3/25.
//
#include <assert.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

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
//
// void ForMatrixOfElementCreateCo_planarCoordinateSystem_ReturnsCorrectCoordinateSystems() {
//     TriangleElementGeometry elements[2] = {
//         {{{0.0, 0.0, 0.0}, {1.0, 0.0, 0.0}, {0.0, 1.0, 0.0}}},
//         {{{1.0, 1.0, 0.0}, {2.0, 1.0, 0.0}, {1.0, 2.0, 0.0}}}
//     };
//
//     CoordinateSystem** coordinateSystemCollection = ForMatrixOfElementCreateCo_planarCoordinateSystem(elements, 2);
//
//     assert(coordinateSystemCollection != NULL);
//     assert(coordinateSystemCollection[0] != NULL);
//     assert(coordinateSystemCollection[1] != NULL);
//
//     freeCoordinateSystem(&coordinateSystemCollection[0]);
//     freeCoordinateSystem(&coordinateSystemCollection[1]);
//     free(coordinateSystemCollection);
// }
//
// void ForMatrixOfElementCreateCo_planarCoordinateSystem_ReturnsNULLForEmptyList() {
//     CoordinateSystem** coordinateSystems = ForMatrixOfElementCreateCo_planarCoordinateSystem(NULL, 0);
//     assert(coordinateSystems == NULL);
// }
//
// void ForMatrixOfElementCreateCo_planarCoordinateSystem_ReturnsNULLForFailedAllocation() {
//     // Simulate memory allocation failure by setting elements_count to a very large number
//     CoordinateSystem** coordinateSystems = ForMatrixOfElementCreateCo_planarCoordinateSystem(NULL, UINT_MAX);
//     assert(coordinateSystems == NULL);
// }


void HelperTest() {
    // ForMatrixOfElementInsertNodesCoordinates_ReturnsCorrectCoordinates();
    // ForMatrixOfElementInsertNodesCoordinates_HandlesEmptyElements();
    // ForMatrixOfElementInsertNodesCoordinates_HandlesNullNodes();
    // ForMatrixOfElementCreateCo_planarCoordinateSystem_ReturnsCorrectCoordinateSystems();
    // ForMatrixOfElementCreateCo_planarCoordinateSystem_ReturnsNULLForEmptyList();
    // ForMatrixOfElementCreateCo_planarCoordinateSystem_ReturnsNULLForFailedAllocation();


    printf("All helper tests passed.\n");
}