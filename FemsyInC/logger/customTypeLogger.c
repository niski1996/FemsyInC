//
// Created by kali on 1/12/25.
//
#include "../models/types.h"
#include <gsl/gsl_matrix_double.h>
#include "logger.h"
#include "../models/types.h"

void logElement(const TriangleElementGeometry element) {
    FILE *file = fopen(LogName, "a");
    fprintf(file, "Element nodes: ");
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