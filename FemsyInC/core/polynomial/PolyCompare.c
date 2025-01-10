#include <stdio.h>
#include <stdlib.h>
#include "Poly.h"

// Generic function for comparing two polynomials
static int comparePolysGeneric(unsigned int degree1, double *coeff1, unsigned int degree2, double *coeff2) {
    if (degree1 != degree2) {
        return 0;  // Degrees are different, polynomials are not equal
    }
    for (int i = 0; i <= degree1; i++) {
        if (coeff1[i] != coeff2[i]) {
            return 0;  // Coefficients differ, polynomials are not equal
        }
    }
    return 1;  // Polynomials are identical
}

// Function to compare 1D polynomials (Poly)
int comparePolys(Poly p1, Poly p2) {
    return comparePolysGeneric(p1.degree, p1.coefficients, p2.degree, p2.coefficients);
}

// Function to compare 2D polynomials (PolyXY)
int comparePolysXY(PolyXY p1, PolyXY p2) {
    return comparePolysGeneric(p1.degree, p1.coefficients, p2.degree, p2.coefficients);
}