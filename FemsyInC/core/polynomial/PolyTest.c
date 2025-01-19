#include <stdio.h>
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include "PolyHelper.h"
#include "Poly.h"
#include "PolyTest.h"

#include <math.h>
// add separate region here
// Test functions for 1D Polynomials (Poly)
void test_createPoly() {
    double coeffs[] = {1.0, 2.0, 3.0};
    Poly poly = createPoly(2, coeffs);
    assert(poly.degree == 2);
    assert(poly.coefficients[0] == 1.0);
    assert(poly.coefficients[1] == 2.0);
    assert(poly.coefficients[2] == 3.0);
    freePoly(&poly);
    printf("test_createPoly passed!\n");
}

void test_printPoly() {
    double coeffs[] = {1.0, 2.0, 3.0};
    Poly poly = createPoly(2, coeffs);
    printPoly(poly); // Manually verify the output
    freePoly(&poly);
    printf("test_printPoly passed!\n");
}

void test_addPolys() {
    double coeffs1[] = {1.0, 2.0, 3.0};
    double coeffs2[] = {3.0, 2.0, 1.0};
    Poly poly1 = createPoly(2, coeffs1);
    Poly poly2 = createPoly(2, coeffs2);
    Poly result = addPolys(poly1, poly2);
    assert(result.degree == 2);
    assert(result.coefficients[0] == 4.0);
    assert(result.coefficients[1] == 4.0);
    assert(result.coefficients[2] == 4.0);
    freePoly(&poly1);
    freePoly(&poly2);
    freePoly(&result);
    printf("test_addPolys passed!\n");
}

void test_subtractPolys() {
    double coeffs1[] = {3.0, 2.0, 1.0};
    double coeffs2[] = {1.0, 2.0, 3.0};
    Poly poly1 = createPoly(2, coeffs1);
    Poly poly2 = createPoly(2, coeffs2);
    Poly result = subtractPolys(poly1, poly2);
    assert(result.degree == 2);
    assert(result.coefficients[0] == 2.0);
    assert(result.coefficients[1] == 0.0);
    assert(result.coefficients[2] == -2.0);
    freePoly(&poly1);
    freePoly(&poly2);
    freePoly(&result);
    printf("test_subtractPolys passed!\n");
}

void test_multiplyPolys() {
    double coeffs1[] = {1.0, 2.0};
    double coeffs2[] = {3.0, 4.0};
    Poly poly1 = createPoly(1, coeffs1);
    Poly poly2 = createPoly(1, coeffs2);
    Poly result = multiplyPolys(poly1, poly2);
    assert(result.degree == 2);
    assert(result.coefficients[0] == 3.0);
    assert(result.coefficients[1] == 10.0);
    assert(result.coefficients[2] == 8.0);
    freePoly(&poly1);
    freePoly(&poly2);
    freePoly(&result);
    printf("test_multiplyPolys passed!\n");
}

void test_scalePoly() {
    double coeffs[] = {1.0, 2.0, 3.0};
    Poly poly = createPoly(2, coeffs);
    Poly result = scalePoly(poly, 2);
    assert(result.degree == 2);
    assert(result.coefficients[0] == 2.0);
    assert(result.coefficients[1] == 4.0);
    assert(result.coefficients[2] == 6.0);
    freePoly(&poly);
    freePoly(&result);
    printf("test_scalePoly passed!\n");
}

void test_integratePoly() {
    double coeffs[] = {1.0, 2.0, 3.0};
    Poly poly = createPoly(2, coeffs);
    Poly result = integratePoly(poly);
    assert(result.degree == 3);
    assert(result.coefficients[0] == 0.0);
    assert(result.coefficients[1] == 1.0);
    assert(result.coefficients[2] == 1.0);
    assert(result.coefficients[3] == 1.0);
    freePoly(&poly);
    freePoly(&result);
    printf("test_integratePoly passed!\n");
}

// void test_derivatePoly() {
//     double coeffs[] = {1.0, 2.0, 3.0};
//     Poly poly = createPoly(2, coeffs);
//     derivatePoly(poly);
//     Poly result = derivatePoly(poly);
//     assert(result.degree == 1);
//     assert(result.coefficients[0] == 2.0);
//     assert(result.coefficients[1] == 6.0);
//     freePoly(&poly);
//     freePoly(&result);
//     printf("test_derivatePoly passed!\n");
// }

void test_evaluatePoly() {
    double coeffs[] = {1.0, 2.0, 3.0};
    Poly poly = createPoly(2, coeffs);
    double result = evaluatePoly(&poly, 2.0);
    assert(result == 17.0); // 1 + 2*2 + 3*2^2 = 1 + 4 + 12 = 17
    freePoly(&poly);
    printf("test_evaluatePoly passed!\n");
}

void test_freePoly() {
    double coeffs[] = {1.0, 2.0, 3.0};
    Poly poly = createPoly(2, coeffs);
    freePoly(&poly);
    assert(poly.coefficients == NULL);
    assert(poly.degree == 0);
    printf("test_freePoly passed!\n");
}

//region Description
//endregion
void test_comparePolys() {
    double coeffs1[] = {1.0, 2.0, 3.0};
    double coeffs2[] = {1.0, 2.0, 3.0};
    Poly poly1 = createPoly(2, coeffs1);
    Poly poly2 = createPoly(2, coeffs2);
    assert(comparePolys(poly1, poly2) == 1);
    double coeffs3[] = {1.0, 2.0, 4.0};
    Poly poly3 = createPoly(2, coeffs3);
    assert(comparePolys(poly1, poly3) == 0);
    freePoly(&poly1);
    freePoly(&poly2);
    freePoly(&poly3);
    printf("test_comparePolys passed!\n");
}

// Test functions for 2D Polynomials (PolyXY)
void test_createPolyXY() {
    double coeffs[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
    PolyXY poly = createPolyXY(2, coeffs);
    assert(poly.degree == 2);
    assert(poly.coefficients[0] == 1.0);
    assert(poly.coefficients[1] == 2.0);
    assert(poly.coefficients[2] == 3.0);
    assert(poly.coefficients[3] == 4.0);
    assert(poly.coefficients[4] == 5.0);
    assert(poly.coefficients[5] == 6.0);
    freePolyXY(&poly);
    printf("test_createPolyXY passed!\n");
}

void test_printPolyXY() {
    double coeffs[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
    PolyXY poly = createPolyXY(2, coeffs);
    printPolyXY(poly); // Manually verify the output
    freePolyXY(&poly);
    printf("test_printPolyXY passed!\n");
}

void test_addPolysXY() {
    double coeffs1[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
    double coeffs2[] = {6.0, 5.0, 4.0, 3.0, 2.0, 1.0};
    PolyXY poly1 = createPolyXY(2, coeffs1);
    PolyXY poly2 = createPolyXY(2, coeffs2);
    PolyXY result = addPolysXY(poly1, poly2);
    assert(result.degree == 2);
    assert(result.coefficients[0] == 7.0);
    assert(result.coefficients[1] == 7.0);
    assert(result.coefficients[2] == 7.0);
    assert(result.coefficients[3] == 7.0);
    assert(result.coefficients[4] == 7.0);
    assert(result.coefficients[5] == 7.0);
    freePolyXY(&poly1);
    freePolyXY(&poly2);
    freePolyXY(&result);
    printf("test_addPolysXY passed!\n");
}

void test_subtractPolysXY() {
    double coeffs1[] = {6.0, 5.0, 4.0, 3.0, 2.0, 1.0};
    double coeffs2[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
    PolyXY poly1 = createPolyXY(2, coeffs1);
    PolyXY poly2 = createPolyXY(2, coeffs2);
    PolyXY result = subtractPolysXY(poly1, poly2);
    assert(result.degree == 2);
    assert(result.coefficients[0] == 5.0);
    assert(result.coefficients[1] == 3.0);
    assert(result.coefficients[2] == 1.0);
    assert(result.coefficients[3] == -1.0);
    assert(result.coefficients[4] == -3.0);
    assert(result.coefficients[5] == -5.0);
    freePolyXY(&poly1);
    freePolyXY(&poly2);
    freePolyXY(&result);
    printf("test_subtractPolysXY passed!\n");
}

void test_multiplyPolysXY() {
    double coeffs1[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
    double coeffs2[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
    PolyXY poly1 = createPolyXY(2, coeffs1);
    PolyXY poly2 = createPolyXY(2, coeffs2);
    PolyXY result = multiplyPolysXY(poly1, poly2);
    assert(result.degree == 4);
    assert(result.coefficients[0] == 1.0);    // x^0 y^0
    assert(result.coefficients[1] == 4.0);    // x^1 y^0
    assert(result.coefficients[2] == 6.0);    // x^0 y^1
    assert(result.coefficients[3] == 10.0);   // x^1 y^1
    assert(result.coefficients[4] == 9.0);    // x^2 y^0
    assert(result.coefficients[5] == 14.0);   // x^0 y^2
    assert(result.coefficients[6] == 8.0);    // x^2 y^1
    assert(result.coefficients[7] == 20.0);   // x^3 y^0
    assert(result.coefficients[8] == 12.0);   // x^1 y^2
    assert(result.coefficients[9] == 36.0);   // x^0 y^3
    freePolyXY(&poly1);
    freePolyXY(&poly2);
    freePolyXY(&result);
    printf("test_multiplyPolysXY passed!\n");
}

void test_scalePolysXY() {
    double coeffs[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
    PolyXY poly = createPolyXY(2, coeffs);
    PolyXY result = scalePolysXY(poly, 2);
    assert(result.degree == 2);
    assert(result.coefficients[0] == 2.0);
    assert(result.coefficients[1] == 4.0);
    assert(result.coefficients[2] == 6.0);
    assert(result.coefficients[3] == 8.0);
    assert(result.coefficients[4] == 10.0);
    assert(result.coefficients[5] == 12.0);
    freePolyXY(&poly);
    freePolyXY(&result);
    printf("test_scalePolysXY passed!\n");
}
//
// void test_integratePolyXY() {
//     double coeffs[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
//     PolyXY poly = createPolyXY(2, coeffs);
//     PolyXY result = integratePolyXY(poly);
//     // Add appropriate assertions based on the expected result
//     freePolyXY(&poly);
//     freePolyXY(&result);
//     printf("test_integratePolyXY passed!\n");
// }
//
// void test_derivatePolyXY() {
//     double coeffs[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
//     PolyXY poly = createPolyXY(2, coeffs);
//     PolyXY result = derivatePolyXY(poly);
//     // Add appropriate assertions based on the expected result
//     freePolyXY(&poly);
//     freePolyXY(&result);
//     printf("test_derivatePolyXY passed!\n");
// }
//
// void test_evaluatePolyXY() {
//     double coeffs[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
//     PolyXY poly = createPolyXY(2, coeffs);
//     double result = evaluatePolyXY(&poly, 2.0, 3.0);
//     // Add appropriate assertions based on the expected result
//     freePolyXY(&poly);
//     printf("test_evaluatePolyXY passed!\n");
// }
//
// void test_freePolyXY() {
//     double coeffs[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
//     PolyXY poly = createPolyXY(2, coeffs);
//     freePolyXY(&poly);
//     assert(poly.coefficients == NULL);
//     assert(poly.degree == 0);
//     printf("test_freePolyXY passed!\n");
// }
//
// void test_comparePolysXY() {
//     double coeffs1[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
//     double coeffs2[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
//     PolyXY poly1 = createPolyXY(2, coeffs1);
//     PolyXY poly2 = createPolyXY(2, coeffs2);
//     assert(comparePolysXY(poly1, poly2) == 1);
//     double coeffs3[] = {1.0, 2.0, 3.0, 4.0, 5.0, 7.0};
//     PolyXY poly3 = createPolyXY(2, coeffs3);
//     assert(comparePolysXY(poly1, poly3) == 0);
//     freePolyXY(&poly1);
//     freePolyXY(&poly2);
//     freePolyXY(&poly3);
//     printf("test_comparePolysXY passed!\n");
// }

//Test for PolyHelper
void test_getPascalTriangleElementCount() {
    getPascalTriangleElementCount(0);
    assert(getPascalTriangleElementCount(1) == 1);
    assert(getPascalTriangleElementCount(2) == 3);
    assert(getPascalTriangleElementCount(3) == 6);
    printf("test_getPascalTriangleElementCount passed!\n");
}

void test_getPascalTriangleLevelCount() {
    assert(getPascalTriangleLevelCount(1) == 1);
    assert(getPascalTriangleLevelCount(3) == 2);
    assert(getPascalTriangleLevelCount(6) == 3);
    printf("test_getPascalTriangleLevelCount passed!\n");
}

void test_getPascalTriangleNLevelStartIndex() {
    assert(getPascalTriangleNLevelStartIndex(1) == 0);
    assert(getPascalTriangleNLevelStartIndex(2) == 1);
    assert(getPascalTriangleNLevelStartIndex(3) == 3);
    assert(getPascalTriangleNLevelStartIndex(4) == 6);
    assert(getPascalTriangleNLevelStartIndex(5) == 10);
    printf("test_getPascalTriangleNLevelStartIndex passed!\n");
}

void test_getPascalTriangleNLevelEndIndex() {
    assert(getPascalTriangleNLevelEndIndex(1) == 0);
    assert(getPascalTriangleNLevelEndIndex(2) == 2);
    assert(getPascalTriangleNLevelEndIndex(3) == 5);
    printf("test_getPascalTriangleNLevelEndIndex passed!\n");
}

void test_AdjustPoly() {
    double coeffs[] = {1.0, 0.0, 3.0, 0.0, 0.0};
    Poly poly = {4, coeffs};
    Poly adjustedPoly = AdjustPoly(poly);
    assert(adjustedPoly.degree == 2);
    assert(poly.degree == 4);
    assert(adjustedPoly.coefficients[0] == 1.0);
    assert(adjustedPoly.coefficients[1] == 0.0);
    assert(adjustedPoly.coefficients[2] == 3.0);
    printf("test_AdjustPoly passed!\n");
}

void test1_AdjustPolyXY() {
    double coeffs[] = {1.0, 0.0, 0.0};
    PolyXY poly = {1, coeffs};
    AdjustPolyXY(&poly);
    assert(poly.degree == 0);
    assert(poly.coefficients[0] == 1.0);
    printf("test1_AdjustPolyXY passed!\n");
}

void test2_AdjustPolyXY() {
    double coeffs[] = {1.0, 0.1, 0.4, 0, 0, 0};
    PolyXY poly = {2, coeffs};
    AdjustPolyXY(&poly);
    assert(poly.degree == 1);
    printf("test2_AdjustPolyXY passed!\n");
}

void test3_AdjustPolyXY() {
    double coeffs[] = {1.0, 0.1, 0.4, 0, 0, 1, 0, 0, 0, 0};
    PolyXY poly = {3, coeffs};
    AdjustPolyXY(&poly);
    assert(poly.degree == 2);
    printf("test3_AdjustPolyXY passed!\n");
}

void test_SwitchXWithY() {
    double coeffs[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
    PolyXY poly = createPolyXY(2, coeffs);
    PolyXY switchedPoly = createPolyXYWithZeros(2);
    SwitchXWithY(&poly, &switchedPoly);
    assert(switchedPoly.degree == 2);
    assert(switchedPoly.coefficients[0] == 1.0);
    assert(switchedPoly.coefficients[1] == 3.0);
    assert(switchedPoly.coefficients[2] == 2.0);
    assert(switchedPoly.coefficients[3] == 6.0);
    assert(switchedPoly.coefficients[4] == 5.0);
    assert(switchedPoly.coefficients[5] == 4.0);
    printf("test_SwitchXWithY passed!\n");
    freePolyXY(&poly);
    freePolyXY(&switchedPoly);
}

void TestPolyHelper() {
    printf("poly`test\n");
    test_getPascalTriangleElementCount();
    test_getPascalTriangleLevelCount();
    test_getPascalTriangleNLevelStartIndex();
    test_getPascalTriangleNLevelEndIndex();
    test_AdjustPoly();
    test1_AdjustPolyXY();
    test2_AdjustPolyXY();
    test3_AdjustPolyXY();
    test_SwitchXWithY();
};

void TestPolyOneVariable() {
    test_createPoly();
    test_printPoly();
    test_addPolys();
    test_subtractPolys();
    test_multiplyPolys();
    test_scalePoly();
    test_integratePoly();
    // test_derivatePoly();
    test_evaluatePoly();
    test_freePoly();
    test_comparePolys();
};



void evaluatePolyXY_CorrectEvaluation() {
    PolyXY poly = {
        .degree = 2,
        .coefficients = (double[]){1, 2, 3, 4, 5, 6}
    };
    double result = evaluatePolyXY(&poly, 1.0, 1.0);
    assert(fabs(result - 21.0) < 1e-6);
}

void evaluatePolyXY_ZeroCoefficients() {
    PolyXY poly = {
        .degree = 2,
        .coefficients = (double[]){0, 0, 0, 0, 0, 0}
    };
    double result = evaluatePolyXY(&poly, 1.0, 1.0);
    assert(fabs(result - 0.0) < 1e-6);
}

void evaluatePolyXY_NegativeCoefficients() {
    PolyXY poly = {
        .degree = 2,
        .coefficients = (double[]){-1, -2, -3, -4, -5, -6}
    };
    double result = evaluatePolyXY(&poly, 1.0, 1.0);
    assert(fabs(result + 21.0) < 1e-6);
}

void evaluatePolyXY_HighDegree() {
    PolyXY poly = {
        .degree = 3,
        .coefficients = (double[]){1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    };
    double result = evaluatePolyXY(&poly, 1.0, 1.0);
    assert(fabs(result - 55.0) < 1e-6);
}

void evaluatePolyXY_ZeroInputs() {
    PolyXY poly = {
        .degree = 2,
        .coefficients = (double[]){1, 2, 3, 4, 5, 6}
    };
    double result = evaluatePolyXY(&poly, 0.0, 0.0);
    assert(fabs(result - 1.0) < 1e-6);
}

void test_evaluatePolyXY() {
    evaluatePolyXY_CorrectEvaluation();
    evaluatePolyXY_ZeroCoefficients();
    evaluatePolyXY_NegativeCoefficients();
    evaluatePolyXY_HighDegree();
    evaluatePolyXY_ZeroInputs();
    printf("test_evaluatePolyXY passed!\n");

}

void PolyXYFit_CorrectCoefficients() {
    TriangleElementGeometry elements[] = {
        {
            .nodes = {
                {3, -1},
                {1, 0},
                {12, 1}
            }
        },
        {
            .nodes = {
                {0, 0},
                {2, 0},
                {0, 2}
            }
        },
        {
            .nodes = {
                {4, 1},
                {2, 1},
                {1, 2}
            }
        }
    };

    float functionValues[][3] = {
        {1, 2, 3},
        {4, 8, 12},
        {-5, 10, -15}
    };

    for (int i = 0; i < 3; i++) {
        const PolyXY poly = createPolyXYWithZeros(2);

        PolyXYFit(&elements[i], functionValues[i], &poly);

        for (int j = 0; j < 3; j++) {
            assert((fabs(evaluatePolyXY(&poly, elements[i].nodes[j].x, elements[i].nodes[j].y) - functionValues[i][j]) < 1e-6));
        }

        free(poly.coefficients);
    }
}

void test_derivativePolyXY() {
    // Create a test polynomial with known coefficients
    double coefficients[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0}; // Example coefficients for a degree 2 polynomial
    PolyXY poly = createPolyXY(2, coefficients);

    // Allocate memory for the output derivative polynomial
    PolyXY outputDerivativeX = createPolyXYWithZeros(1);
    PolyXY outputDerivativeY = createPolyXYWithZeros(1);

    // Call the function to calculate the derivative with respect to x
    derivativePolyXY(&poly, true, &outputDerivativeX);

    // Expected coefficients for the derivative with respect to x
    double expectedCoefficientsX[] = {2.0, 8.0, 5.0}; // Adjust based on your specific implementation

    // // Verify the output derivative polynomial against expected values
    for (int i = 0; i < 3; i++) {
    assert(outputDerivativeX.coefficients[i] == expectedCoefficientsX[i]);
    }
    assert(outputDerivativeX.degree == 1);
    //
    // // Call the function to calculate the derivative with respect to y
    derivativePolyXY(&poly, false, &outputDerivativeY);

    // Expected coefficients for the derivative with respect to y
    double expectedCoefficientsY[] = {3.0, 5.0, 12.0}; // Adjust based on your specific implementation

    // Verify the output derivative polynomial against expected values
    for (int i = 0; i < 3; i++) {
        assert(outputDerivativeY.coefficients[i] == expectedCoefficientsY[i]);
    }
    // assert(outputDerivativeX.degree == 1);

    // Free allocated memory
    // freePolyXY(&outputDerivativeX);
    freePolyXY(&outputDerivativeY);
    freePolyXY(&poly);

    printf("Test for derivativePolyXY passed!\n");
}

void test_polyFit() {
    PolyXYFit_CorrectCoefficients();
    printf("All PolyTit tests passed.\n");
}




void TestPolyTwoVariables(){
    test_createPolyXY();
    // test_printPolyXY();
    // test_addPolysXY();
    // test_subtractPolysXY();
    // test_multiplyPolysXY();
    // test_scalePolysXY();
    // test_integratePolyXY();
    // test_derivativePolyXY();
    test_evaluatePolyXY();
    test_polyFit();
    // test_derivativePolyXY();
    // test_freePolyXY();
    // test_comparePolysXY();
}

void PolyTest() {
    printf("poly`test\n");
    TestPolyTwoVariables();
    // TestPolyOneVariable();
    TestPolyHelper();
};
