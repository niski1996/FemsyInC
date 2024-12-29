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



Poly createPoly(int degree, double *coefficients);
void printPoly(Poly poly);
Poly addPolys(Poly poly1, Poly poly2);
Poly multiplyPolys(Poly poly1, Poly poly2);
Poly integralPolys(Poly poly);
Poly derivativePolys(Poly poly);
double evaluatePoly(Poly poly, double x);
void freePoly(Poly *poly);
int comparePoly (Poly poly1, Poly poly2);


#endif