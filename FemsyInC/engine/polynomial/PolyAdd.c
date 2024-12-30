#include <stdio.h>
#include <stdlib.h>
#include "PolyHepler.h"
#include "Poly.h"
#include "math.h"


static double* addCoefficients(double* coefficients1, unsigned int numberOfCoeff1, double* coefficients2, unsigned int numberOfCoeff2){

    unsigned int size = (int)fmax(numberOfCoeff1, numberOfCoeff2);
    double *coeff = calloc(size, sizeof(double));
    if (coeff == NULL)
    {
        fprintf(stderr, "Developer error: Memory allocation failed");
        exit(EXIT_FAILURE);
    }
    
    for (int i = 0; i <= size; i++) {
        double c1 = (i <= numberOfCoeff1) ? coefficients1[i] : 0.0;
        double c2 = (i <= numberOfCoeff2) ? coefficients2[i] : 0.0;
        coeff[i] = c1 + c2;
    }
    return coeff;
    
}

Poly addPolys(Poly p1, Poly p2){

    if (p1.degree == 0) return p2;
    if (p2.degree == 0) return p1;

    double* coeff = addCoefficients(p1.coefficients, p1.degree + 1, p2.coefficients, p2.degree + 1);
    int degree  = (int)fmax(p1.degree, p2.degree);

    Poly result = {degree, coeff};
    return result;

}
PolyXY addPolysXY(PolyXY p1, PolyXY p2){

    if (p1.degree == 0) return p2;
    if (p2.degree == 0) return p1;

    double* coeff = addCoefficients(p1.coefficients, getPascalTriangleElementCount(p1.degree), p2.coefficients, getPascalTriangleElementCount(p2.degree));
    int degree  = (int)fmax(p1.degree, p2.degree);

    PolyXY result = {degree, coeff};
    return result;

}
