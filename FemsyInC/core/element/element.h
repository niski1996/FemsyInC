//
// Created by kali on 1/13/25.
//

#ifndef ELEMENT_H
#define ELEMENT_H

#include "../../models/types.h"
#include "../polynomial/Poly.h"

void calculateShapeFunctionForTriangleElementNodes(
    TriangleElementGeometry *element, PolyXY *shapeFunction);

void calculateShapeFunctionForTriangleElementNodesCollection(
    TriangleElementGeometry *element, int elementCount, PolyXY **OutputShapeFunctionCollection);

#endif //ELEMENT_H
