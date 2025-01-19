//
// Created by kali on 1/2/25.
//
#include "Poly.h"
#include <stdlib.h>
#include <stdio.h>

#include "PolyHelper.h"

Poly derivatePoly(Poly poly) {
    if (poly.degree == 0) {
        if (poly.degree == 0) {
            fprintf(stderr, "Error: Cannot derive a polynomial of degree 0\n");
            exit(EXIT_FAILURE);
        }
    }
    int new_degree = poly.degree - 1;
    double *new_coefficients = (double *) calloc(new_degree + 1, sizeof(double));
    if (new_coefficients == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 1; i <= poly.degree; i++) {
        new_coefficients[i - 1] = poly.coefficients[i] * i;
    }

    Poly result = {new_degree, new_coefficients};
    return result;
}



void derivativePolyXYdy(const PolyXY *Poly, PolyXY *OutputDerivative) {
    for (int i =1; i<=Poly->degree; i++) {
        const unsigned int  start = getPascalTriangleNLevelStartIndex(i+1);
        const unsigned int end = getPascalTriangleNLevelEndIndex(i+1);
        const unsigned int LoweLevelStart = getPascalTriangleNLevelStartIndex(i);
        for (unsigned int j = start+1; j<=end; j++) {
            OutputDerivative->coefficients[LoweLevelStart+(j-start-1)] = (j-start)*Poly->coefficients[j];
        }
    }
    AdjustPolyXY(OutputDerivative);
}

void derivativePolyXYdx(const PolyXY *Poly, PolyXY *OutputDerivative) {
    PolyXY tmpPoly =createPolyXYWithZeros(Poly->degree);
    PolyXY tmpDerivPoly =createPolyXYWithZeros(OutputDerivative->degree);
    SwitchXWithY(Poly, &tmpPoly);
    derivativePolyXYdy(&tmpPoly,&tmpDerivPoly);
    SwitchXWithY(&tmpDerivPoly,OutputDerivative);
    freePolyXY(&tmpPoly);
    freePolyXY(&tmpDerivPoly);
}

void derivativePolyXY(const PolyXY *Poly, bool DxDerivative, PolyXY *OutputDerivative) {
    if (DxDerivative) {
        derivativePolyXYdx(Poly, OutputDerivative);
    } else {
        derivativePolyXYdy(Poly, OutputDerivative);
    }
}
