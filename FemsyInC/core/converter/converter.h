//
// Created by kali on 1/12/25.
//

#ifndef CONVERTER_H
#define CONVERTER_H
#include "../../models/types.h"

int convertRawCoordinatesMatrixToPointCollection(
    const gsl_matrix *RawCoordinates,
    int PointCollectionCount,
    Point *OutputPointCollection);

int convertMatrixOfElementNumberIntoCollectionOfElements(
    const Point *NodeCollection,
    const gsl_matrix *RawElementCollection,
    int ElementCollectionCount,
    TriangleElementGeometry *OutputElementCollection);
#endif //CONVERTER_H
