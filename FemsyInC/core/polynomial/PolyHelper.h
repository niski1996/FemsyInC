#ifndef POLYHELPER_H
#define POLYHELPER_H

#include "Poly.h"

unsigned int getPascalTriangleElementCount(unsigned int levelCount);
unsigned int getPascalTriangleLevelCount(unsigned int elementCount);
unsigned int getPascalTriangleNLevelStartIndex(unsigned int level);
unsigned int getPascalTriangleNLevelEndIndex(unsigned int level);
Poly AdjustPoly(Poly poly);
void AdjustPolyXY(PolyXY *poly);
PolyXY SwitchXWithY(PolyXY *poly, PolyXY *OutputPoly);
#endif