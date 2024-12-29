#include <math.h>
#include "PolyHepler.h"

unsigned int getPascalTriangleElementCount(unsigned int levelCount){
    return ((levelCount+1)*(levelCount+2)/2);
}
unsigned int getPascalTriangleLevelCount(unsigned int elementCount){
    return (sqrt(1+elementCount)-3)/2;
}