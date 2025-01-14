//
// Created by kali on 1/13/25.
//

#include "elementTest.h"
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "element.h"
#include "../polynomial/Poly.h"

#include <stdio.h>
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include "../polynomial/PolyHelper.h"
#include "../polynomial/Poly.h"
#include "../polynomial/PolyTest.h"

void test_calculateShapeFunctionForTriangleElementNodesCollection() {
    // Create test elements
    TriangleElementGeometry element1 = {
        .nodes = {
            {0.0, 0.0},
            {1.0, 0.0},
            {0.0, 1.0}
        }
    };

    TriangleElementGeometry element2 = {
        .nodes = {
            {0.0, 0.0},
            {2.0, 0.0},
            {0.0, 2.0}
        }
    };

    TriangleElementGeometry *elements[] = {&element1, &element2};

    // Allocate memory for output shape functions
    PolyXY *outputShapeFunctions[2];
    for (int i = 0; i < 2; i++) {
        outputShapeFunctions[i] = (PolyXY *)malloc(3 * sizeof(PolyXY));
    }

    // Call the function
    calculateShapeFunctionForTriangleElementNodesCollection(elements, 2, outputShapeFunctions);

    // Check the results (this is a simple check, you may want to add more detailed checks)
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            assert(outputShapeFunctions[i][j].degree == 1);
            assert(outputShapeFunctions[i][j].coefficients != NULL);
        }
    }

    // Free allocated memory
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            free(outputShapeFunctions[i][j].coefficients);
        }
        free(outputShapeFunctions[i]);
    }

    printf("Test passed!\n");
}

void elementTest() {
    test_calculateShapeFunctionForTriangleElementNodesCollection();
    printf("All element tests passed!\n");
}