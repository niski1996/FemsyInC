#include <stdio.h>
#include "Test.h"
#include "helpers/helper.h"
#include "models/types.h"


int RunTask() {
    const char* path = "/home/kali/Desktop/cybersec/sem1/programowanie/Femsy/FemsyInC/input/example/nodes.csv";
    printf("start task from location: %s\n", path);
    printf("reading nodes from nodes.csv\n");
    Point *pointCollection;
    int pointCollectionCount = readPointsFromCSV(path, &pointCollection);
#ifdef DEBUG
    printf(" nodes matrix: \n");
    for (int i = 0; i < pointCollectionCount; i++) {
        printf("Node number: %d: x: %f, y: %f, z: %f\n",i, pointCollection[i].x, pointCollection[i].y, pointCollection[i].z);
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

