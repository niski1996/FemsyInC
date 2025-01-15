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

void test_calculateShapeFunctionForTriangleElementNodes() {
    // Create a test element with known node coordinates
    TriangleElementGeometry element = {
        .nodes = {
            {0.0, 0.0},
            {1.0, 0.0},
            {0.0, 1.0}
        }
    };

    // Allocate memory for output shape functions
    PolyXY outputShapeFunctions[3];
    for (int i = 0; i < 3; i++) {
        outputShapeFunctions[i] = createPolyXYWithZeros(1); // Degree 1 for linear shape functions
    }

    // Call the function to calculate shape functions
    calculateShapeFunctionForTriangleElementNodes(&element, outputShapeFunctions);

    // Verify the output shape functions against expected values
    // Expected shape functions for a standard triangle element
    double expectedCoefficients[3][3] = {
        {1.0, -1.0, -1.0},
        {0.0, 1.0, 0.0},
        {0.0, 0.0, 1.0}
    };

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            assert(outputShapeFunctions[i].coefficients[j] == expectedCoefficients[i][j]);
        }
    }

    // Free allocated memory
    for (int i = 0; i < 3; i++) {
        freePolyXY(&outputShapeFunctions[i]);
    }

    printf("Test for calculateShapeFunctionForTriangleElementNodes passed!\n");
}


void test_calculateShapeFunctionForTriangleElementNodesCollection() {
    // Create test elements with known node coordinates
    TriangleElementGeometry elements[2] = {
        {
            .nodes = {
                {0.0, 0.0},
                {1.0, 0.0},
                {0.0, 1.0}
            }
        },
        {
            .nodes = {
                {0.0, 0.0},
                {2.0, 0.0},
                {0.0, 2.0}
            }
        }
    };

    // Allocate memory for output shape functions
    PolyXY *outputShapeFunctions[2];
    for (int i = 0; i < 2; i++) {
        outputShapeFunctions[i] = (PolyXY *)malloc(3 * sizeof(PolyXY));
        for (int j = 0; j < 3; j++) {
            outputShapeFunctions[i][j] = createPolyXYWithZeros(1); // Degree 1 for linear shape functions
        }
    }

    // Call the function to calculate shape functions
    calculateShapeFunctionForTriangleElementNodesCollection(elements, 2, outputShapeFunctions);

    // Verify the output shape functions against expected values
    // Expected shape functions for the first standard triangle element
    double expectedCoefficients1[3][3] = {
        {1.0, -1.0, -1.0},
        {0.0, 1.0, 0.0},
        {0.0, 0.0, 1.0}
    };

    // Expected shape functions for the second scaled triangle element
    double expectedCoefficients2[3][3] = {
        {1.0, -0.5, -0.5},
        {0.0, 0.5, 0.0},
        {0.0, 0.0, 0.5}
    };

    double (*expectedCoefficients[2])[3][3] = {expectedCoefficients1, expectedCoefficients2};

    for (int k = 0; k < 2; k++) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                assert(outputShapeFunctions[k][i].coefficients[j] == (*expectedCoefficients[k])[i][j]);
            }
        }
    }

    // Free allocated memory
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            freePolyXY(&outputShapeFunctions[i][j]);
        }
        free(outputShapeFunctions[i]);
    }

    printf("Test for calculateShapeFunctionForTriangleElementNodesCollection passed!\n");
}

void elementTest() {
    test_calculateShapeFunctionForTriangleElementNodes();
    test_calculateShapeFunctionForTriangleElementNodesCollection();
    printf("All element tests passed!\n");
}