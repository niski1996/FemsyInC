//
// Created by kali on 1/3/25.
//

#ifndef TYPES_H
#define TYPES_H

typedef struct {
    double x, y, z;
} Node;

typedef struct {
    Node nodes[3];
} TriangleElementGeometry;
#endif //TYPES_H
