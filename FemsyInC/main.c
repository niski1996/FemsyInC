#include <stdio.h>
#include "Test.h"
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

    // Użycie poprawnego typu
    int (*nodeNumberCollection)[3] = NULL;

    // Wywołanie funkcji
    int elementsCount = readElementsFromCSV(pathElements, &nodeNumberCollection);
#ifdef DEBUG
        for (int i = 0; i < elementsCount; i++) {
            printf("Element number: %d: %d, %d, %d\n",
                   i, nodeNumberCollection[i][0], nodeNumberCollection[i][1], nodeNumberCollection[i][2]);
        }

#endif



#ifdef NDEBUG
    printf("hello release\n");  // Komunikat w trybie Release
#endif


    free(pointCollection);
    return 0;
}

int main() {
    printf("Start main\n");
    // RunAllTests();
    RunTask();

    return 0;
}

