#include <stdio.h>
#include "Poly.h"

void printPoly(Poly poly) {
    if (poly.coefficients == NULL || poly.degree == 0) {
        printf("0\n");
        return;
    }
    for (int i = 0; i <= poly.degree; i++) {
        if (poly.coefficients[i]==0) continue;
        if (poly.coefficients[i]<0) {
            printf("-");
        }
        else {
            printf("+");
        }
        printf("%.2lfx^%d ", poly.coefficients[i],i);
    }
    printf("\n");
}

void printPolyXY(PolyXY poly) {
    if (poly.coefficients == NULL || poly.degree == 0) {
        printf("0\n");
        return;
    }

    unsigned int index = 0;
    for (int totalDegree = 0; totalDegree <= poly.degree; ++totalDegree) {
        for (int i = totalDegree; i >= 0; --i) {
            int j = totalDegree - i;

            if (poly.coefficients[index] != 0) {
                if (index != 0 && poly.coefficients[index] > 0) {
                    printf(" + ");
                } else if (poly.coefficients[index] < 0) {
                    printf(" - ");
                }

                double absCoeff = (poly.coefficients[index] < 0) ? -poly.coefficients[index] : poly.coefficients[index];
                if (absCoeff != 1 || (i == 0 && j == 0)) {
                    printf("%.2lf", absCoeff);
                }

                if (i > 0) {
                    printf("x");
                    if (i > 1) {
                        printf("^%d", i);
                    }
                }
                if (j > 0) {
                    printf("y");
                    if (j > 1) {
                        printf("^%d", j);
                    }
                }
            }
            ++index;
        }
    }
    printf("\n");
}
