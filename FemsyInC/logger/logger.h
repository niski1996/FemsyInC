//
// Created by kali on 1/10/25.
//

#ifndef LOGGER_H
#define LOGGER_H
#include "../models/types.h"
#include <gsl/gsl_matrix.h>
extern char *LogName;
void logMatrix(const gsl_matrix *matrix);
void logDatetime();
void logMessage(const char *format, ...) ;
void logPointCollection(
    const Point *pointCollection,
    int pointCollectionCount);
void logElement(TriangleElementGeometry element);
void logElementCollection(TriangleElementGeometry *element, int elementCollectionCount);
void logCoordinateSystem(const CoordinateSystem *coordinateSystem);
void logCoordinateSystemCollection(const CoordinateSystem **coordinateSystem, int coordinateSystemCount);
void logGlsVector(const gsl_vector *vector, FILE *file);

#endif //LOGGER_H
