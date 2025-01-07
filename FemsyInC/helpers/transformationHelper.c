//
// Created by kali on 1/4/25.
//
#include "helper.h"
#include "../models/types.h"
#include "../engine/vector/vector.h"
#include "../engine/coordinateSystem/coordinateSystem.h"
#include <stdlib.h>


CoordinateSystem** ForMatrixOfElementCreateCo_planarCoordinateSystem(const TriangleElementGeometry *triangleElementGeometries, unsigned int elements_count) {
    if (elements_count == 0) {
        return NULL;
    }

    // Allocate memory for the array of coordinate systems
    CoordinateSystem** coordinateSystemsList = malloc(elements_count * sizeof(CoordinateSystem*));
    if (coordinateSystemsList == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    // Iterate over all elements and create a coordinate system for each
    for (unsigned int i = 0; i < elements_count; ++i) {
        Point origin = triangleElementGeometries[i].nodes[0];
        Point pointOnX = triangleElementGeometries[i].nodes[1];
        Point pointOnXY = triangleElementGeometries[i].nodes[2];

        // Create the coordinate system for the current element
        coordinateSystemsList[i] = createCoordinateSystemFromThreeNonLinearPoints(origin, pointOnX, pointOnXY);

        // If the coordinate system creation failed, free allocated memory and return NULL
        if (coordinateSystemsList[i] == NULL) {
            for (unsigned int j = 0; j < i; ++j) {
                freeCoordinateSystem(&coordinateSystemsList[j]);
            }
            free(coordinateSystemsList);
            return NULL;
        }
    }

    return coordinateSystemsList;
}