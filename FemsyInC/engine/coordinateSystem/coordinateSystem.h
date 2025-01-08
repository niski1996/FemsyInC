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
void forCollectionOfCoordinateSystemsCreateTransformationMatrices(
    const CoordinateSystem** coordinateSystems,
    unsigned int count,
    gsl_matrix** OutputTransformationMatrices);
#endif //COORDINATESYSTEM_H
