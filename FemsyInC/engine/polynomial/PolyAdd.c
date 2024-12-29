#include <stdio.h>
#include <stdlib.h>
#include "Poly.h"


Poly addPolys(Poly p1, Poly p2){

    if (p1.degree = 0) return p2;
    if (p2.degree = 0) return p1;

    int degree  = max(p1.degree, p2.degree);
    double *coeff = calloc(degree + 1, sizeof(double));
    if (coeff == NULL)
    {
        fprintf(stderr, "Developer error: Memory allocation failed");
        exit(EXIT_FAILURE);
    }
    
    for (int i = 0; i <= degree; i++) {
        double c1 = (i <= p1.degree) ? p1.coefficients[i] : 0.0;
        double c2 = (i <= p2.degree) ? p2.coefficients[i] : 0.0;
        coeff[i] = c1 + c2;
    }

    Poly result = {degree, coeff};
    return result;
        
    
}