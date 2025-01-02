#include <stdio.h>
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include "PolyHelper.h"
#include "Poly.h"
#include "PolyTest.h"
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

void test_derivatePoly() {
    double coeffs[] = {1.0, 2.0, 3.0};
    Poly poly = createPoly(2, coeffs);
    Poly result = derivatePoly(poly);
    assert(result.degree == 1);
    assert(result.coefficients[0] == 2.0);
    assert(result.coefficients[1] == 6.0);
    freePoly(&poly);
    freePoly(&result);
    printf("test_derivatePoly passed!\n");
}

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
    PolyXY adjustedPoly = AdjustPolyXY(poly);
    assert(adjustedPoly.degree == 0);
    assert(adjustedPoly.coefficients[0] == 1.0);
    printf("test1_AdjustPolyXY passed!\n");
}

void test2_AdjustPolyXY() {
    double coeffs[] = {1.0, 0.1, 0.4, 0, 0, 0};
    PolyXY poly = {2, coeffs};
    PolyXY adjustedPoly = AdjustPolyXY(poly);
    assert(adjustedPoly.degree == 1);
    printf("test2_AdjustPolyXY passed!\n");
}

void test3_AdjustPolyXY() {
    double coeffs[] = {1.0, 0.1, 0.4, 0, 0, 1, 0, 0, 0, 0};
    PolyXY poly = {3, coeffs};
    PolyXY adjustedPoly = AdjustPolyXY(poly);
    assert(adjustedPoly.degree == 2);
    printf("test3_AdjustPolyXY passed!\n");
}

void test_SwitchXWithY() {
    double coeffs[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
    PolyXY poly = {2, coeffs};
    PolyXY switchedPoly = SwitchXWithY(poly);
    assert(switchedPoly.degree == 2);
    assert(switchedPoly.coefficients[0] == 1.0);
    assert(switchedPoly.coefficients[1] == 3.0);
    assert(switchedPoly.coefficients[2] == 2.0);
    assert(switchedPoly.coefficients[3] == 6.0);
    assert(switchedPoly.coefficients[4] == 5.0);
    assert(switchedPoly.coefficients[5] == 4.0);
    printf("test_SwitchXWithY passed!\n");
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
    test_derivatePoly();
    test_evaluatePoly();
    test_freePoly();
    test_comparePolys();
};

void PolyTest() {
    printf("poly`test\n");
    TestPolyOneVariable();
    TestPolyHelper();
};
