//
// Created by kali on 1/3/25.
//

#include <gsl/gsl_matrix_double.h>

#include "../../models/types.h"

#ifndef COORDINATESYSTEM_H
#define COORDINATESYSTEM_H

CoordinateSystem* createCoordinateSystemFromThreeNonLinearPoints(
    Point origin,
    Point pointOnX,
    Point pointOnXY);
void freeCoordinateSystem(
    CoordinateSystem** coordinateSystem);
void createTransformationMatrix(
    const CoordinateSystem* newCoordinateSystemInnOldLayout,
    gsl_matrix* OutputOldToNewTransformationMatrix);
void createTransformationMatrixCollectionFromGlobalToLocalCoordinateSystem(
    const CoordinateSystem** LocalCoordinateSystemCollection,
    unsigned int elementsCount,
    gsl_matrix** OutputGlobalToLocalTransformationMatrices);
#endif //COORDINATESYSTEM_H
