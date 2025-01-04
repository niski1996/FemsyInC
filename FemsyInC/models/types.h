//
// Created by kali on 1/3/25.
//

#ifndef TYPES_H
#define TYPES_H

#include <gsl/gsl_vector.h>
typedef struct {
    double x, y, z;
} Point;

typedef struct {
    Point nodes[3];
} TriangleElementGeometry;

typedef struct {
    gsl_vector *UnitVectorX;
    gsl_vector *UnitVectorY;
    gsl_vector *UnitVectorZ;
} CoordinateSystem;
#endif //TYPES_H
