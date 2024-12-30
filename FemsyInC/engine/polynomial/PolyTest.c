#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "Poly.h"

void test_addPolys_1D() {
    double coeff1[] = {1.0, 2.0, 3.0}; // 1 + 2x + 3x^2
    double coeff2[] = {4.0, 5.0};      // 4 + 5x

    Poly p1 = {2, coeff1};
    Poly p2 = {1, coeff2};

    Poly result = addPolys(p1, p2);

    assert(result.degree == 2);
    assert(result.coefficients[0] == 5.0); // 1 + 4
    assert(result.coefficients[1] == 7.0); // 2 + 5
    assert(result.coefficients[2] == 3.0); // 3 + 0

    freePoly(&result);
    printf("test_addPolys_1D passed!\n");
}

void test_addPolys_2D() {
    double coeff1[] = {1.0, 2.0, 3.0, 4.0}; // Degree 2, Pascal Triangle {x^0+y^0, x^1+y^0, x^0+y^1, x^2}
    double coeff2[] = {5.0, 6.0, 7.0};      // Degree 1, Pascal Triangle {x^0+y^0, x^1+y^0, x^0+y^1}

    PolyXY p1 = {2, coeff1};
    PolyXY p2 = {1, coeff2};

    PolyXY result = addPolysXY(p1, p2);

    assert(result.degree == 2);
    assert(result.coefficients[0] == 6.0); // 1 + 5
    assert(result.coefficients[1] == 8.0); // 2 + 6
    assert(result.coefficients[2] == 10.0); // 3 + 7
    assert(result.coefficients[3] == 4.0); // 4 + 0

    freePolyXY(&result);
    printf("test_addPolys_2D passed!\n");
}

int main() {
    test_addPolys_1D();
    test_addPolys_2D();
    return 0;
}
