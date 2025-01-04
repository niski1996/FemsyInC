//
// Created by kali on 1/3/25.
//

#ifndef HELPER_H
#define HELPER_H

#include "../models/types.h"


TriangleElementGeometry* ForMatrixOfElementInsertNodesCoordinates(
    unsigned int *elements,
    unsigned int elements_count, Point *nodes,
    int *nodesCount);
CoordinateSystem** ForMatrixOfElementCreateCo_planarCoordinateSystem(
    const TriangleElementGeometry *triangleElementGeometries,
    unsigned int elements_count);

#endif //HELPER_H
