#include <stdio.h>
#include "Test.h"
#include "core/coordinateSystem/coordinateSystem.h"
#include "helpers/helper.h"
#include "input/parser.h"
#include "models/types.h"


int RunTask() {
    const char* pathNodes = "/home/kali/Desktop/cybersec/sem1/programowanie/Femsy/FemsyInC/input/example/nodes.csv";
    printf("start task from location: %s\n", pathNodes);
    printf("reading nodes from nodes.csv\n");
    const char *NodesFormat = "%lf,%lf,%lf";
    gsl_matrix *RawNodeCoordinateCollection;
    int NodeCollectionCount = 0;

    if (parse_3_columns_matrix(pathNodes, &RawNodeCoordinateCollection, &NodeCollectionCount, NodesFormat) != 0) {
        fprintf(stderr, "Error reading the matrix from the file\n");
        return -1;
    }
    gsl_matrix_free(RawNodeCoordinateCollection);

     // int pointCollectionCount = readPointsFromCSV(pathNodes, &pointCollection);
// #ifdef DEBUG
//     printf(" nodes matrix: \n");
//     for (int i = 0; i < pointCollectionCount; i++) {
//         printf("Node number: %d: x: %f, y: %f, z: %f\n",i, pointCollection[i].x, pointCollection[i].y, pointCollection[i].z);
//     }
// #endif
//     printf("Reading elements from elements.csv\n");
//     const char *pathElements = "/home/kali/Desktop/cybersec/sem1/programowanie/Femsy/FemsyInC/input/example/elements.csv";
//     unsigned int (*nodeNumberCollection)[3];
//     int elementCollectionCount = readElementsFromCSV(pathElements, &nodeNumberCollection);
// #ifdef DEBUG
//         for (int i = 0; i < elementCollectionCount; i++) {
//             printf("Element number: %d: %d, %d, %d\n",
//                    i, nodeNumberCollection[i][0], nodeNumberCollection[i][1], nodeNumberCollection[i][2]);
//         }
// #endif
//     printf("inserting nodes coordinates instead of elements numbers\n");
    // TriangleElementGeometry* elementsInGlobalCoordinates = ForMatrixOfElementInsertNodesCoordinates(&nodeNumberCollection, elementCollectionCount, pointCollection, &pointCollectionCount);
// #ifdef DEBUG
//     printf("elements in global coordinates: \n");
//     for (int i = 0; i < elementCollectionCount; i++) {
//         printf("Element number: %d: \n", i);
//         for (int j = 0; j < 3; j++) {
//             printf("Node number: %d: x: %f, y: %f, z: %f\n", j, elementsInGlobalCoordinates[i].nodes[j].x, elementsInGlobalCoordinates[i].nodes[j].y, elementsInGlobalCoordinates[i].nodes[j].z);
//         }
//     }
// #endif
//     printf("creating local coordinate systems\n");
//     CoordinateSystem** localCoordinateSystemsCollection = malloc(elementCollectionCount * sizeof(CoordinateSystem*));
//     if (localCoordinateSystemsCollection == NULL) {
//         fprintf(stderr, "Memory allocation failed\n");
//         exit(EXIT_FAILURE);
//     }
//     ForMatrixOfElementCreateCo_planarCoordinateSystem(elementsInGlobalCoordinates, elementCollectionCount, localCoordinateSystemsCollection);
//
//
// #ifdef NDEBUG
//     printf("hello release\n");
// #endif
//     free(nodeNumberCollection);
//     free(pointCollection);
//     for (int i = 0; i < elementCollectionCount; i++) {
//         free(localCoordinateSystemsCollection[i]);
//     }
    // free(localCoordinateSystemsCollection);
    return 0;
}

int main() {
    int i, j, k;
    float x, y, z;
    // RunAllTests();
    RunTask();

    return 0;
}

