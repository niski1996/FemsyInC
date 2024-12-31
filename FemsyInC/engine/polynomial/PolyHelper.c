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
    return ((level + 1) * level) / 2 - 1;
}

Poly AdjustPoly(Poly poly)// Adjust poly degree by removing enpty slots and adjusting degree
{
    for(int i = poly.degree; i>0;i--)//TODO what with empty poly? Fuck it
    {
        if (poly.coefficients[i] == 0)
        {
            poly.degree--;
        }
        else break; 

    }
}

PolyXY SwitchXWithY(PolyXY poly) {
    PolyXY result;
    result.degree = poly.degree;
    result.coefficients = (double *)malloc(((poly.degree + 1) * (poly.degree + 2) / 2) * sizeof(double));

    unsigned int index = 0;
    for (unsigned int i = 0; i <= poly.degree; ++i) {
        for (unsigned int j = 0; j <= i; ++j) {
            unsigned int originalIndex = getPascalTriangleNLevelStartIndex(i) + j;
            result.coefficients[index++] = poly.coefficients[originalIndex];
        }
    }

    return result;
    }
