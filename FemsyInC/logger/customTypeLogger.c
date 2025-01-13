//
// Created by kali on 1/12/25.
//
#include "../models/types.h"
#include <gsl/gsl_matrix_double.h>
#include "logger.h"
#include "../models/types.h"

void logElement(const TriangleElementGeometry element, const int ElementNumber) {
    FILE *file = fopen(LogName, "a");
    fprintf(file, "element %d nodes : ", ElementNumber);
    for (int i = 0; i < 3; i++) {
        fprintf(file,"Node %d:     x: %lf, y: %lf, z: %lf", i, element.nodes[i].x, element.nodes[i].y, element.nodes[i].z);
    }
    fprintf(file, "\n");
    fclose(file);
}
void logCoordinateSystem(const CoordinateSystem *coordinateSystem) {
    FILE *file = fopen(LogName, "a");
    fprintf(file, "Coordinate system: x unit vector: ");
    logGlsVector(coordinateSystem->UnitVectorX, file);
    fprintf(file, " y unit vector: ");
    logGlsVector(coordinateSystem->UnitVectorY, file);
    fprintf(file, " z unit vector: ");
    logGlsVector(coordinateSystem->UnitVectorZ, file);
    fprintf(file, "\n");
    fclose(file);

}

void logPolyXY(const PolyXY* poly, FILE *file) {
    if (poly->coefficients == NULL || poly->degree == 0) {
        fprintf(file, "0");
        return;
    }

    unsigned int index = 0;
    for (int totalDegree = 0; totalDegree <= poly->degree; ++totalDegree) {
        for (int i = totalDegree; i >= 0; --i) {
            int j = totalDegree - i;

            if (poly->coefficients[index] != 0) {
                if (index != 0 && poly->coefficients[index] > 0) {
                    fprintf(file, " + ");
                } else if (poly->coefficients[index] < 0) {
                    fprintf(file, " - ");
                }

                double absCoeff = (poly->coefficients[index] < 0) ? -poly->coefficients[index] : poly->coefficients[index];
                if (absCoeff != 1 || (i == 0 && j == 0)) {
                    fprintf(file, "%.2lf", absCoeff);
                }

                if (i > 0) {
                    fprintf(file, "x");
                    if (i > 1) {
                        fprintf(file, "^%d", i);
                    }
                }
                if (j > 0) {
                    fprintf(file, "y");
                    if (j > 1) {
                        fprintf(file, "^%d", j);
                    }
                }
            }
            ++index;
        }
    }
}