//
// Created by kali on 1/3/25.
//
#include "../models/types.h"
#include <stdio.h>
#include <stdlib.h>

TriangleElementGeometry* ForMatrixOfElementInsertNodesCoordinates(unsigned int *elements, unsigned int elements_count, Point *nodes, int *nodesCount) {
    if (elements_count == 0 || nodes == NULL) {
        *nodesCount = 0;
        return NULL;
    }

    TriangleElementGeometry *triangleElementGeometries = (TriangleElementGeometry *) malloc(elements_count * sizeof(TriangleElementGeometry));
    if (triangleElementGeometries == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    *nodesCount = 0;
    for (unsigned int i = 0; i < elements_count; i++) {
        for (unsigned int j = 0; j < 3; j++) {
            unsigned int node_index = elements[i * 3 + j];
            triangleElementGeometries[i].nodes[j] = nodes[node_index];
            (*nodesCount)++;
        }
    }

    return triangleElementGeometries;
}