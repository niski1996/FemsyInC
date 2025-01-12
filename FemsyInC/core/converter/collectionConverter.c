//
// Created by kali on 1/12/25.
//

#include <gsl/gsl_matrix_double.h>
#include "converter.h"
#include "../../models/types.h"

int convertRawCoordinatesMatrixToPointCollection(const gsl_matrix *RawCoordinates, const int PointCollectionCount,
                                                 Point *OutputPointCollection) {
    for (int i = 0; i < PointCollectionCount; i++) {
        OutputPointCollection[i].x = gsl_matrix_get(RawCoordinates, i, 0);
        OutputPointCollection[i].y = gsl_matrix_get(RawCoordinates, i, 1);
        OutputPointCollection[i].z = gsl_matrix_get(RawCoordinates, i, 2);
    }
    return 0;
}


int convertMatrixOfElementNumberIntoCollectionOfElements(
    const Point *NodeCollection,
    const gsl_matrix *RawElementCollection,
    const int ElementCollectionCount,
    TriangleElementGeometry *OutputElementCollection) {
    for (unsigned int i = 0; i < ElementCollectionCount; i++) {
        for (unsigned int j = 0; j < 3; j++) {
            const unsigned int node_index = (int) gsl_matrix_get(RawElementCollection, i, j);
            OutputElementCollection[i].nodes[j] = NodeCollection[node_index];
        }
    }
    return 0;
}
