#ifndef POLY_H
#define POLY_H

#include "../../models/types.h"

typedef struct Poly
{
    unsigned int degree;
    double *coefficients; // Coefficients of the polynomial, where the index represents the power of x corresponding to the coefficient.
} Poly;

typedef struct PolyXY
{
    unsigned int degree;
    double *coefficients; // Coefficients of the polynomial, created witch pattern similar to pascal triangle {x^0+y^0, x^1+y^0, x^0+y^1, x^2+y^2,x^1+y^1 ...}
} PolyXY;



// Functions for 1D Polynomials (Poly)
Poly createPoly(int degree, double *coefficients);
void printPoly(Poly poly);
Poly addPolys(Poly poly1, Poly poly2);
Poly subtractPolys(Poly poly1, Poly poly2);
Poly multiplyPolys(Poly poly1, Poly poly2);
Poly scalePoly(Poly poly, int scale);
Poly integratePoly(Poly poly);
Poly derivatePoly(Poly poly);
double evaluatePoly(const Poly* poly, double x);
void freePoly(Poly *poly);
int comparePolys(Poly poly1, Poly poly2);

// Functions for 2D Polynomials (PolyXY)
PolyXY createPolyXY(int degree, const double *coefficients);
PolyXY createPolyXYWithZeros(const int degree);

void printPolyXY(PolyXY poly);
PolyXY addPolysXY(PolyXY poly1, PolyXY poly2);
PolyXY subtractPolysXY(PolyXY poly1, PolyXY poly2);
PolyXY multiplyPolysXY(PolyXY poly1, PolyXY poly2);
PolyXY scalePolysXY(PolyXY poly1, int scale);
PolyXY integratePolyXY(PolyXY poly);
PolyXY derivatePolyXY(PolyXY poly);
double evaluatePolyXY(const PolyXY* poly, double x, double y);
void PolyXYFit(
    TriangleElementGeometry *ElementInLocalCoordinates,
    float *functionValuesInPoint,
    PolyXY OutputPolynomialXY);

void freePolyXY(PolyXY *poly);
int comparePolysXY(PolyXY poly1, PolyXY poly2);

#endif