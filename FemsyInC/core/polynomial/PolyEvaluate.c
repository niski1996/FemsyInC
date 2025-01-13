#include <math.h>

#include "Poly.h"

double evaluatePoly(const Poly* poly, const double x) {
    double result = 0.0;
    for (int i = poly->degree; i >= 0; i--) {
        result = result * x + poly->coefficients[i];
    }
    return result;
}

double evaluatePolyXY(const PolyXY* poly, const double x, const double y) {
    double result = 0.0;
    int index = 0;
    for (unsigned int i = 0; i <= poly->degree; i++) {
        for (unsigned int j = 0; j <= i; j++) {
            result += poly->coefficients[index] * pow(x, i - j) * pow(y, j);
            index++;
        }
    }
    return result;
}