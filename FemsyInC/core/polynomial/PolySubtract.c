#include <stdio.h>
#include <stdlib.h>
#include "Poly.h"
#include "PolyHelper.h"

Poly subtractPolys(Poly poly1, Poly poly2){
    Poly negativePoly = scalePoly(poly2, -1);
    Poly output =  addPolys(poly1, negativePoly);
    freePoly(&negativePoly);
    return AdjustPoly(output);
}

PolyXY subtractPolysXY(PolyXY poly1, PolyXY poly2) {
    PolyXY negativePoly = scalePolysXY(poly2, -1);
    PolyXY result = addPolysXY(poly1, negativePoly);
    freePolyXY(&negativePoly);
    return AdjustPolyXY(result);
}