//
// Created by kali on 1/10/25.
//

#include <gsl/gsl_matrix_double.h>
#include "logger.h"
#include "../models/types.h"



void logMatrixCollection(const gsl_matrix **matrix, const int matrixCount) {
    for (int i = 0; i < matrixCount; i++) {
        logMatrix(matrix[i]);
    }
    FILE *file = fopen(LogName, "a");
    fprintf(file, "\n");

    fclose(file);
}

void logPointCollection(const Point *pointCollection, const int pointCollectionCount) {
    logDatetime();
    FILE *file = fopen(LogName, "a");
    for (int i = 0; i < pointCollectionCount; i++) {
        fprintf(file, "Node number: %d: x: %f, y: %f, z: %f\n", i, pointCollection[i].x, pointCollection[i].y, pointCollection[i].z);
    }
    fclose(file);
}

void logElementCollection(TriangleElementGeometry *element, int elementCollectionCount) {
    for (int i = 0; i < elementCollectionCount; i++) {
        logElement(element[i], i);

    }
}
void logCoordinateSystemCollection(const CoordinateSystem **coordinateSystem, int coordinateSystemCount) {
    for (int i = 0; i < coordinateSystemCount; i++) {
        logCoordinateSystem(coordinateSystem[i]);
    }
}

void logTriangleElementShapeFunction(const PolyXY *ShapeFunctionCollection, const int ElementNumber) {
    FILE *file = fopen(LogName, "a");
    fprintf(file, "Shape functions for element %-5d:    ", ElementNumber);
    for (int i = 0; i < 3; i++) {
        logPolyXY(&ShapeFunctionCollection[i], file);

        int current_pos = ftell(file) % 50; // Pozycja karetki w linii

        // set pointer 100 further line for clarity
        for (int i = current_pos; i < 50; i++) {
            fputc(' ', file);
        }
    }
    fprintf(file, "\n");
    fclose(file);
}

void logTriangleElementCollectionShapeFunction(const PolyXY **ShapeFunctionCollection, int ElementCount) {
    for (int i = 0; i < ElementCount; i++) {
        logTriangleElementShapeFunction(ShapeFunctionCollection[i], i);
    }
}