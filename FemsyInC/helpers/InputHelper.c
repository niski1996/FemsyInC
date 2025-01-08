//
// Created by kali on 1/3/25.
//
#include "../models/types.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

TriangleElementGeometry* ForMatrixOfElementInsertNodesCoordinates(
    unsigned int (**nodeNumberCollection)[3],
    unsigned int elements_count, Point *nodes,
    int *nodesCount) {
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
            unsigned int node_index = (*nodeNumberCollection)[i][j];
            triangleElementGeometries[i].nodes[j] = nodes[node_index];
            (*nodesCount)++;
        }
    }
    return triangleElementGeometries;
}

const char* getfield(char* line, int num) {
    const char* tok;
    for (tok = strtok(line, ","); tok && *tok; tok = strtok(NULL, ",\n")) {
        if (!--num)
            return tok;
    }
    return NULL;
}

int readElementsFromCSV(const char *path, unsigned int (**nodeNumberCollection)[3]) {
    FILE *stream = fopen(path, "r");
    if (!stream) {
        perror("Error opening file");
        return -1;
    }

    int capacity = 10;
    int rowCount = 0;

    *nodeNumberCollection = (unsigned int (*)[3]) malloc(capacity * sizeof(int[3]));
    if (!*nodeNumberCollection) {
        perror("Memory allocation error");
        fclose(stream);
        return -1;
    }

    char line[1024];
    if (fgets(line, sizeof(line), stream) == NULL) {
        fclose(stream);
        free(*nodeNumberCollection);
        return -1;
    }

    while (fgets(line, sizeof(line), stream)) {
        if (rowCount >= capacity) {
            capacity *= 2;
            int (*temp)[3] = (int (*)[3]) realloc(*nodeNumberCollection, capacity * sizeof(int[3]));
            if (!temp) {
                perror("Memory allocation error during reallocation");
                free(*nodeNumberCollection);
                fclose(stream);
                return -1;
            }
            *nodeNumberCollection = temp;
        }

        char *tmp = strdup(line);
        if (!tmp) {
            perror("Memory allocation error");
            free(*nodeNumberCollection);
            fclose(stream);
            return -1;
        }

        (*nodeNumberCollection)[rowCount][0] = atoi(getfield(tmp, 1));
        free(tmp);

        tmp = strdup(line);
        (*nodeNumberCollection)[rowCount][1] = atoi(getfield(tmp, 2));
        free(tmp);

        tmp = strdup(line);
        (*nodeNumberCollection)[rowCount][2] = atoi(getfield(tmp, 3));
        free(tmp);

        rowCount++;
    }

    fclose(stream);
    return rowCount;
}

int readPointsFromCSV(const char *path, Point **pointCollection) {
    FILE* stream = fopen(path, "r");
    if (!stream) {
        perror("Error opening file");
        return -1;
    }

    int capacity = 10;
    int rowCount = 0;
    *pointCollection = (Point *)malloc(capacity * sizeof(Point));
    if (!*pointCollection) {
        perror("Memory allocation error");
        fclose(stream);
        return -1;
    }

    // Skip the header line
    char line[1024];
    if (fgets(line, sizeof(line), stream) == NULL) {
        fclose(stream);
        return -1;
    }

    // Read each row
    while (fgets(line, sizeof(line), stream)) {
        if (rowCount >= capacity) {
            capacity *= 2;
            Point *temp = (Point *)realloc(*pointCollection, capacity * sizeof(Point));
            if (!temp) {
                perror("Memory allocation error");
                free(*pointCollection);
                fclose(stream);
                return -1;
            }
            *pointCollection = temp;
        }

        char* tmp = strdup(line);
        if (!tmp) {
            perror("Memory allocation error");
            free(*pointCollection);
            fclose(stream);
            return -1;
        }

        (*pointCollection)[rowCount].x = atof(getfield(tmp, 2));
        free(tmp);

        tmp = strdup(line);
        (*pointCollection)[rowCount].y = atof(getfield(tmp, 3));
        free(tmp);

        tmp = strdup(line);
        (*pointCollection)[rowCount].z = atof(getfield(tmp, 4));
        free(tmp);

        rowCount++;
    }

    fclose(stream);

    return rowCount;
}
