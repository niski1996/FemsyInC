#include <stdio.h>
#include "Test.h"
#include "engine/coordinateSystem/coordinateSystem.h"
#include "helpers/helper.h"
#include "models/types.h"


int RunTask() {
    const char* pathNodes = "/home/kali/Desktop/cybersec/sem1/programowanie/Femsy/FemsyInC/input/example/nodes.csv";
    printf("start task from location: %s\n", pathNodes);
    printf("reading nodes from nodes.csv\n");
    Point *pointCollection;
    int pointCollectionCount = readPointsFromCSV(pathNodes, &pointCollection);
#ifdef DEBUG
    printf(" nodes matrix: \n");
    for (int i = 0; i < pointCollectionCount; i++) {
        printf("Node number: %d: x: %f, y: %f, z: %f\n",i, pointCollection[i].x, pointCollection[i].y, pointCollection[i].z);
    }
#endif
    printf("Reading elements from elements.csv\n");
    const char *pathElements = "/home/kali/Desktop/cybersec/sem1/programowanie/Femsy/FemsyInC/input/example/elements.csv";
    unsigned int (*nodeNumberCollection)[3];
    int elementCollectionCount = readElementsFromCSV(pathElements, &nodeNumberCollection);
#ifdef DEBUG
        for (int i = 0; i < elementCollectionCount; i++) {
            printf("Element number: %d: %d, %d, %d\n",
                   i, nodeNumberCollection[i][0], nodeNumberCollection[i][1], nodeNumberCollection[i][2]);
        }
#endif
    printf("inserting nodes coordinates instead of elements numbers\n");
    TriangleElementGeometry* elementsInGlobalCoordinates = ForMatrixOfElementInsertNodesCoordinates(&nodeNumberCollection, elementCollectionCount, pointCollection, &pointCollectionCount);
#ifdef DEBUG
    printf("elements in global coordinates: \n");
    for (int i = 0; i < elementCollectionCount; i++) {
        printf("Element number: %d: \n", i);
        for (int j = 0; j < 3; j++) {
            printf("Node number: %d: x: %f, y: %f, z: %f\n", j, elementsInGlobalCoordinates[i].nodes[j].x, elementsInGlobalCoordinates[i].nodes[j].y, elementsInGlobalCoordinates[i].nodes[j].z);
        }
    }
#endif
    printf("creating local coordinate systems\n");
    CoordinateSystem** coordinateSystemsList = malloc(elementCollectionCount * sizeof(CoordinateSystem*));
    if (coordinateSystemsList == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    ForMatrixOfElementCreateCo_planarCoordinateSystem(elementsInGlobalCoordinates, elementCollectionCount, coordinateSystemsList);


#ifdef NDEBUG
    printf("hello release\n");
#endif

    // free(localCoordinateSystemCollection);

    free(nodeNumberCollection);
    free(pointCollection);
    for (int i = 0; i < elementCollectionCount; i++) {
        free(coordinateSystemsList[i]);
    }
    free(&elementCollectionCount);

    return 0;
}

int main() {
    printf("Start main\n");
    // RunAllTests();
    RunTask();

    return 0;
}

