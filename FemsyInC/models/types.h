//
// Created by kali on 1/3/25.
//

#ifndef TYPES_H
#define TYPES_H

typedef struct {
    double x, y, z;
} Point;

typedef struct {
    Point nodes[3];
} TriangleElementGeometry;

typedef struct {
    Point UnitVectorX;
    Point UnitVectorY;
    Point UnitVectorZ;
} CoordinateSystem;
#endif //TYPES_H
