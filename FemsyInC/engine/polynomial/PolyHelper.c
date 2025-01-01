#include <math.h>
#include <stdlib.h>
#include "PolyHelper.h"
#include "Poly.h"

unsigned int getPascalTriangleElementCount(const unsigned int levelCount){
    return (levelCount)*(levelCount+1)/2;
}
unsigned int getPascalTriangleLevelCount(const unsigned int elementCount){
    return (unsigned int)(sqrt(1+8*elementCount)-1)/2;
}

unsigned int getPascalTriangleNLevelStartIndex(unsigned int level) {
    return (level * (level - 1)) / 2;
}

unsigned int getPascalTriangleNLevelEndIndex(unsigned int level) {
    return getPascalTriangleNLevelStartIndex(level+1)-1;
}

unsigned int getPascalTriangleNLevelElementCount(unsigned int level) {
    return level;
}

Poly AdjustPoly(Poly poly) // Adjust poly degree by removing empty slots and adjusting degree
{
 for (unsigned int i = poly.degree; i > 0; i--) // TODO what with empty poly? Fuck it
    {
        if (poly.coefficients[i] == 0)
        {
            poly.degree--;
        }
        else break;
    }
    return poly;
}

PolyXY AdjustPolyXY(PolyXY poly) {
    for (unsigned int i = getPascalTriangleElementCount(poly.degree); i > 0; i--) {
        if (poly.coefficients[i] == 0) {
            poly.degree--;
        } else {
            break;
        }
    }
    return poly;
}



PolyXY SwitchXWithY(PolyXY poly) {
    double buffor = 0;
    for (unsigned int i = 0; i <= poly.degree; ++i) {
        for (unsigned int j = ; j <= i; ++j) {
            unsigned int originalIndex = getPascalTriangleNLevelStartIndex(i) + j;
            poly.coefficients[index++] = poly.coefficients[originalIndex];
        }
    }
    return poly;
    }
