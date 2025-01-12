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
}