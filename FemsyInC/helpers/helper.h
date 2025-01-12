//
// Created by kali on 1/3/25.
//

#ifndef HELPER_H
#define HELPER_H

#include <gsl/gsl_matrix_double.h>

#include "../models/types.h"


void createCoordinateSystemCollectionCoPlanarToElementCollection(
    const TriangleElementGeometry *triangleElementGeometries,
    unsigned int elements_count,
    CoordinateSystem** outputCoordinateSystemCollection);

TriangleElementGeometry* TransformElementCollectionToNewCoordinateSystem(
    const TriangleElementGeometry **triangleElementGeometryCollection,
    unsigned int elements_count,
    const CoordinateSystem **coordinateSystemCollection);

void TransformPointToNewCoordinateSystem(
    const Point *point,
    const gsl_matrix *transformationMatrix,
    Point *result);

void transformElementGeometryToNewCoordinateSystem(
    const TriangleElementGeometry *triangleElementGeometry,
    const gsl_matrix *transformationMatrix,
    TriangleElementGeometry *result);


#endif //HELPER_H
