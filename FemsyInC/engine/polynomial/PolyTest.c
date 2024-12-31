#include <stdio.h>
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include "PolyHelper.h"
#include "Poly.h"
#include "PolyTest.h"

// Test functions for 1D Polynomials (Poly)
void test_createPoly();
void test_printPoly();
void test_addPolys();
void test_subtractPolys();
void test_multiplyPolys();
void test_scalePoly();
void test_integratePoly();
void test_derivatePoly();
void test_evaluatePoly();
void test_freePoly();
void test_comparePolys();

// Test functions for 2D Polynomials (PolyXY)
void test_createPolyXY();
void test_printPolyXY();
void test_addPolysXY();
void test_subtractPolysXY();
void test_multiplyPolysXY();
void test_scalePolysXY();
void test_integratePolyXY();
void test_derivatePolyXY();
void test_evaluatePolyXY();
void test_freePolyXY();
void test_comparePolysXY();

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

// void test_getPascalTriangleNLevelStartIndex() {
//     assert(getPascalTriangleNLevelStartIndex(0) == 0);
//     assert(getPascalTriangleNLevelStartIndex(1) == 0);
//     assert(getPascalTriangleNLevelStartIndex(2) == 1);
//     printf("test_getPascalTriangleNLevelStartIndex passed!\n");
// }
//
// void test_getPascalTriangleNLevelEndIndex() {
//     assert(getPascalTriangleNLevelEndIndex(0) == 0);
//     assert(getPascalTriangleNLevelEndIndex(1) == 1);
//     assert(getPascalTriangleNLevelEndIndex(2) == 2);
//     printf("test_getPascalTriangleNLevelEndIndex passed!\n");
// }
//
// void test_AdjustPoly() {
//     double coeffs[] = {1.0, 0.0, 3.0};
//     Poly poly = {2, coeffs};
//     Poly adjustedPoly = AdjustPoly(poly);
//     assert(adjustedPoly.degree == 2);
//     assert(adjustedPoly.coefficients[0] == 1.0);
//     assert(adjustedPoly.coefficients[1] == 0.0);
//     assert(adjustedPoly.coefficients[2] == 3.0);
//     printf("test_AdjustPoly passed!\n");
// }
//
// void test_AdjustPolyXY() {
//     double coeffs[] = {1.0, 0.0, 3.0, 0.0, 5.0};
//     PolyXY poly = {2, coeffs};
//     PolyXY adjustedPoly = AdjustPolyXY(poly);
//     assert(adjustedPoly.degree == 2);
//     assert(adjustedPoly.coefficients[0] == 1.0);
//     assert(adjustedPoly.coefficients[1] == 0.0);
//     assert(adjustedPoly.coefficients[2] == 3.0);
//     assert(adjustedPoly.coefficients[3] == 0.0);
//     assert(adjustedPoly.coefficients[4] == 5.0);
//     printf("test_AdjustPolyXY passed!\n");
// }
//
// void test_SwitchXWithY() {
//     double coeffs[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
//     PolyXY poly = {2, coeffs};
//     PolyXY switchedPoly = SwitchXWithY(poly);
//     assert(switchedPoly.degree == 2);
//     assert(switchedPoly.coefficients[0] == 1.0);
//     assert(switchedPoly.coefficients[1] == 2.0);
//     assert(switchedPoly.coefficients[2] == 3.0);
//     assert(switchedPoly.coefficients[3] == 4.0);
//     assert(switchedPoly.coefficients[4] == 5.0);
//     assert(switchedPoly.coefficients[5] == 6.0);
//     free(switchedPoly.coefficients);
//     printf("test_SwitchXWithY passed!\n");
// }

void PolyTest() {
    printf("poly`test\n");
    test_getPascalTriangleElementCount();
    test_getPascalTriangleLevelCount();
};