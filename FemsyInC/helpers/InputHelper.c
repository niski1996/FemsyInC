//
// Created by kali on 1/3/25.
//
#include "../models/types.h"
#include <stdio.h>
#include <stdlib.h>

TriangleElementGeometry* ForMatrixOfElementInsertNodesCoordinates(unsigned int *elements, unsigned int elements_count, Point *nodes, int *nodesCount) {
    if (elements_count == 0 || nodes == NULL) {
        *nodesCount = 0;
        return NULL;
    }

    TriangleElementGeometry *triangleElementGeometries = (TriangleElementGeometry *) malloc(elements_count * sizeof(TriangleElementGeometry));
    if (triangleElementGeometries == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    *nodesCount = 0;
    for (unsigned int i = 0; i < elements_count; i++) {
        for (unsigned int j = 0; j < 3; j++) {
            unsigned int node_index = elements[i * 3 + j];
            triangleElementGeometries[i].nodes[j] = nodes[node_index];
            (*nodesCount)++;
        }
    }

    return triangleElementGeometries;
}

int readPointsFromCSV(const char *path, Point **pointCollection) {
    FILE *file = fopen(path, "r");
    if (!file) {
        perror("Error opening file");
        return -1;
    }

    // Allocate an initial array (resizable)
    int capacity = 10;
    int count = 0;
    *pointCollection = (Point *)malloc(capacity * sizeof(Point));
    if (!*pointCollection) {
        perror("Memory allocation error");
        fclose(file);
        return -1;
    }

    // Skip the header line
    char line[256];
    if (fgets(line, sizeof(line), file) == NULL) {
        fclose(file);
        return -1;
    }

    // Read each row
    while (fgets(line, sizeof(line), file)) {
        if (count >= capacity) {
            capacity *= 2;
            *pointCollection = (Point *)realloc(*pointCollection, capacity * sizeof(Point));
            if (!*pointCollection) {
                perror("Memory allocation error");
                fclose(file);
                return -1;
            }
        }

        // Parse the line
        if (sscanf(line, "%d,%lf,%lf,%lf",
                   &count,
                   &(*pointCollection)[count].x,
                   &(*pointCollection)[count].y,
                   &(*pointCollection)[count].z) != 4) {
            fprintf(stderr, "Error parsing line: %s\n", line);
            continue;
                   }

        count++;
    }

    fclose(file);
    return count; // Return the number of pointCollection read
}
