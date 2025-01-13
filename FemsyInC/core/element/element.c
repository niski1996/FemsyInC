#include <stdlib.h>
#include <string.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_linalg.h>
#include <gsl/gsl_permutation.h>
#include "element.h"
#include "../polynomial/Poly.h"

void calculateShapeFunctionForTriangleElementNodes(TriangleElementGeometry *element, PolyXY *OutputShapeFunctionCollection) {
    if (element == NULL || OutputShapeFunctionCollection == NULL) {
        fprintf(stderr, "Invalid input to calculateShapeFunctionForTriangleElementNodes\n");
        return;
    }

    // Initialize shape functions
    for (int i = 0; i < 3; i++) {
        OutputShapeFunctionCollection[i].degree = 1;
        OutputShapeFunctionCollection[i].coefficients = (double*)malloc(3 * sizeof(double));
        memset(OutputShapeFunctionCollection[i].coefficients, 0, 3 * sizeof(double));
    }

    // Create function values for each node
    float functionValues[3][3] = {
        {1.0, 0.0, 0.0},
        {0.0, 1.0, 0.0},
        {0.0, 0.0, 1.0}
    };

    // Fit the shape functions using PolyXYFit
    for (int i = 0; i < 3; i++) {
        PolyXYFit(element, functionValues[i], OutputShapeFunctionCollection[i]);
    }
}

void calculateShapeFunctionForTriangleElementNodesCollection(
    TriangleElementGeometry **element, int elemntCount, PolyXY **OutputShapeFunctionCollection) {

    if (element == NULL || OutputShapeFunctionCollection == NULL) {
        fprintf(stderr, "Invalid input to calculateShapeFunctionForTriangleElementNodesCollection\n");
        return;
    }

    for (int i = 0; i < elemntCount; i++) {
        calculateShapeFunctionForTriangleElementNodes(element[i], OutputShapeFunctionCollection[i]);
    }
}