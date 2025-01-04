//
// Created by kali on 1/3/25.
//

#include "../../models/types.h"

#ifndef COORDINATESYSTEM_H
#define COORDINATESYSTEM_H

CoordinateSystem *createCoordinateSystemFromThreeNonLinearPoints(Point origin, Point pointOnX, Point pointOnXY);
void freeCoordinateSystem(CoordinateSystem** coordinateSystem);
#endif //COORDINATESYSTEM_H
