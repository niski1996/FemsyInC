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
    return level == 1? 0:getPascalTriangleNLevelStartIndex(level+1)-1;
}

unsigned int getPascalTriangleLevelNumerosity(unsigned int level) {
    return getPascalTriangleNLevelEndIndex(level)- getPascalTriangleNLevelStartIndex(level)+1;
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
    for (unsigned int i = 0; i <= poly.degree; ++i) {
        unsigned int startIndex = getPascalTriangleNLevelStartIndex(i+1);
        unsigned int endIndex = getPascalTriangleNLevelEndIndex(i+1);
        for (unsigned int j = 0 ; j < getPascalTriangleLevelNumerosity(i+1)/2; ++j) {
            double buffer = poly.coefficients[startIndex+j];
            poly.coefficients[startIndex+j]=poly.coefficients[endIndex-j];
            poly.coefficients[endIndex-j]=buffer;

        }
    }
    return poly;
    }
