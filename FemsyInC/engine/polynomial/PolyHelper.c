#include <math.h>
#include "PolyHepler.h"
#include "Poly.h"

unsigned int getPascalTriangleElementCount(unsigned int levelCount){
    return ((levelCount+1)*(levelCount+2)/2);
}
unsigned int getPascalTriangleLevelCount(unsigned int elementCount){
    return (sqrt(1+elementCount)-3)/2;
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
