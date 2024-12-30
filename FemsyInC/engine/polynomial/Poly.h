#ifndef POLY_H
#define POLY_H

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
Poly multiplyPolys(Poly poly1, Poly poly2);
Poly scalePoly(Poly poly, int scale);
Poly integralPoly(Poly poly);
Poly derivativePoly(Poly poly);
double evaluatePoly(Poly poly, double x);
void freePoly(Poly *poly);
int comparePolys(Poly poly1, Poly poly2);

// Functions for 2D Polynomials (PolyXY)
PolyXY createPolyXY(int degree, double *coefficients);
void printPolyXY(PolyXY poly);
PolyXY addPolysXY(PolyXY poly1, PolyXY poly2);
PolyXY multiplyPolysXY(PolyXY poly1, PolyXY poly2);
PolyXY scalePolysXY(PolyXY poly1, int scale);
PolyXY integralPolyXY(PolyXY poly);
PolyXY derivativePolyXY(PolyXY poly);
double evaluatePolyXY(PolyXY poly, double x, double y);
void freePolyXY(PolyXY *poly);
int comparePolysXY(PolyXY poly1, PolyXY poly2);

#endif