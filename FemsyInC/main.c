#include <stdio.h>

#include "Test.h"
#include "core/coordinateSystem/coordinateSystem.h"
#include "helpers/helper.h"
#include "input/parser.h"
#include "logger/logger.h"
#include "models/types.h"
#include "core/converter/converter.h"


int RunTask() {
    remove("log.log");
    //begin of input reading
    //read nodes from csv
    const char* pathNodes = "/home/kali/Desktop/cybersec/sem1/programowanie/Femsy/FemsyInC/input/example/nodes.csv";
    logMessage("start RunTask");
    logMessage("path for Nodes: %s", pathNodes);
    gsl_matrix *RawNodeCoordinateCollection;
    int NodeCollectionCount = 0;

    if (parse_3_columns_matrix(pathNodes, &RawNodeCoordinateCollection, &NodeCollectionCount) != 0) {
        fprintf(stderr, "Error reading the matrix from the file\n");
        logMessage("An error occurred while reading the nodes matrix from the file");
        return -1;
    }
    logMessage("finished reading nodes. Nodes count: %d node matrix: ", NodeCollectionCount);
    logMatrix(RawNodeCoordinateCollection);

    //read elements from csv
    const char *pathElements = "/home/kali/Desktop/cybersec/sem1/programowanie/Femsy/FemsyInC/input/example/elements.csv";
    logMessage("path for Elements: %s", pathElements);
    gsl_matrix *RawElementCollection;
    int ElementCollectionCount = 0;
    if (parse_3_columns_matrix(pathElements, &RawElementCollection, &ElementCollectionCount) != 0) {
        fprintf(stderr, "Error reading the matrix from the file\n");
        logMessage("An error occurred while reading the matrix elements from the file");
        return -1;
    }

    logMessage("finished reading Elements. Elements count: %d node matrix: ", ElementCollectionCount);
    logMatrix(RawElementCollection);
    //end of input reading


    Point *NodesCollection = malloc(NodeCollectionCount * sizeof(Point));
    logMessage("converting the matrix to the point collection");
    if (convertRawCoordinatesMatrixToPointCollection(RawNodeCoordinateCollection, NodeCollectionCount, NodesCollection) != 0) {
        fprintf(stderr, "Error converting the matrix to the point collection\n");
        logMessage("An error occurred while converting the matrix to the point collection");
        return -1;
    }
    logMessage("finished converting the matrix to the point collection. Nodes count: %d  Points array: ", NodeCollectionCount);
    logPointCollection(NodesCollection, NodeCollectionCount);



    logMessage("instering nodes coordinates instead of elements numbers");
    TriangleElementGeometry *ElementInGlobalCoordinatesCollection = malloc(ElementCollectionCount * sizeof(TriangleElementGeometry));
    convertMatrixOfElementNumberIntoCollectionOfElements(
        NodesCollection,
        RawElementCollection,
        ElementCollectionCount,
        ElementInGlobalCoordinatesCollection);
    logElementCollection(ElementInGlobalCoordinatesCollection, ElementCollectionCount);



    logMessage("creating local coordinate systems");
    CoordinateSystem **LocalCoordinateSystemsCollection = malloc(ElementCollectionCount * sizeof(CoordinateSystem));
    createCoordinateSystemCollectionCoPlanarToElementCollection(ElementInGlobalCoordinatesCollection, ElementCollectionCount, LocalCoordinateSystemsCollection);
    logMessage("local coordinate systems created:");
    logCoordinateSystemCollection(LocalCoordinateSystemsCollection, ElementCollectionCount);




    for (int i =0; i<ElementCollectionCount; i++) {
        freeCoordinateSystem(&LocalCoordinateSystemsCollection[i]);
    }
    free(LocalCoordinateSystemsCollection);
    free(ElementInGlobalCoordinatesCollection);
    free(NodesCollection);
    gsl_matrix_free(RawElementCollection);
    gsl_matrix_free(RawNodeCoordinateCollection);

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

