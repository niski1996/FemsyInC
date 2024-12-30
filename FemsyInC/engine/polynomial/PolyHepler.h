#ifndef POLYHELPER_H
#define POLYHELPER_H

unsigned int getPascalTriangleElementCount(unsigned int levelCount);
unsigned int getPascalTriangleLevelCount(unsigned int elementCount);
unsigned int getPascalTriangleNLevelStartIndex(unsigned int level);
unsigned int getPascalTriangleNLevelEndIndex(unsigned int level);
Poly AdjustPoly(Poly poly);
PolyXY AdjustPolyXY(PolyXY poly);
PolyXY SwitchXWithY(PolyXY poly)
#endif