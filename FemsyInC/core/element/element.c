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

void calculateShapeFunctionDerivativesForTriangleElementNodes(
    PolyXY *ShapeFunctionsForTriangleElement,
    PolyXY *OutputShapeFunctionsForTriangleElement) {
    for (int i = 0; i<3; i++) {

    }

}

//It applies only to triangular elements, where the shape function is of the first degree,
//so its derivative reduces to a constant.
void calculateNodeDerivativeCollection(PolyXY *poly, PolyXY ***OutputDerivativeCollection) {
    PolyXY dx = createPolyXYWithZeros(poly->degree-1);
    PolyXY dy = createPolyXYWithZeros(poly->degree-1);
    // derivativePolyXY()
}



void calculateShapeFunctionDerivativesForTriangleElementNodesCollection(
    PolyXY **ShapeFunctionCollection,
    int elementsCount,
    PolyXY **OutputShapeFunctionDerivativeCollection) {

}

