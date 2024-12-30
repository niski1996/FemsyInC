#include <stdlib.h>
#include "Poly.h"

void freePoly(Poly *poly) {
    if (poly != NULL) {
        free(poly->coefficients);
        poly->coefficients = NULL;
        poly->degree = 0;
    }
}

void freePolyXY(PolyXY *poly) {
    if (poly != NULL) {
        free(poly->coefficients);
        poly->coefficients = NULL;
        poly->degree = 0;
    }
}
