#include "Poly.h"

double evaluatePoly(Poly* poly, double x) {
    double result = 0.0;
    for (int i = poly->degree; i >= 0; i--) {
        result = result * x + poly->coefficients[i];
    }
    return result;
}