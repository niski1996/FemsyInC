//
// Created by kali on 1/3/25.
//
#include "../models/types.h"
#include <stdlib.h>

TriangleElementGeometry* ForMatrixOfElementInsertNodesCoordinates(unsigned int *elements, unsigned int elements_count, Node *nodes, int *nodesCount) {
    TriangleElementGeometry *triangleElementGeometries = (TriangleElementGeometry *) malloc(elements_count * sizeof(TriangleElementGeometry));
    *nodesCount = 0;
    for (int i = 0; i < elements_count; i++) {
        TriangleElementGeometry triangleElementGeometry;
        for (int j = 0; j < 3; j++) {
            Node node = nodes[elements[i * 3 + j]];
            triangleElementGeometry.nodes[j] = node;
            (*nodesCount)++;
        }
        triangleElementGeometries[i] = triangleElementGeometry;
    }
    return triangleElementGeometries;
}