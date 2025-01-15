#include <stdlib.h>
#include <string.h>
#include <gsl/gsl_matrix.h>
#include "element.h"
#include "../polynomial/Poly.h"

void calculateShapeFunctionForTriangleElementNodes(TriangleElementGeometry *element, PolyXY *OutputShapeFunctionCollection) {
    if (element == NULL || OutputShapeFunctionCollection == NULL) {
        fprintf(stderr, "Invalid input to calculateShapeFunctionForTriangleElementNodes\n");
        return;
    }

    // Create function values for each node
    float functionValues[3][3] = {
        {1.0, 0.0, 0.0},
        {0.0, 1.0, 0.0},
        {0.0, 0.0, 1.0}
    };

    // Fit the shape functions using PolyXYFit
    for (int i = 0; i < 3; i++) {
        PolyXYFit(element, functionValues[i], &OutputShapeFunctionCollection[i]);
    }
}

void calculateShapeFunctionForTriangleElementNodesCollection(
    TriangleElementGeometry *element, int elementCount, PolyXY **OutputShapeFunctionCollection) {

    if (element == NULL || OutputShapeFunctionCollection == NULL) {
        fprintf(stderr, "Invalid input to calculateShapeFunctionForTriangleElementNodesCollection\n");
        return;
    }

    for (int i = 0; i < elementCount; i++) {
        calculateShapeFunctionForTriangleElementNodes(&element[i], OutputShapeFunctionCollection[i]);
    }
}