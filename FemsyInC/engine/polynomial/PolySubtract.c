#include <stdio.h>
#include <stdlib.h>
#include "Poly.h"
#include "PolyHepler.h"

Poly subtractPolys(Poly poly1, Poly poly2){
    Poly negativePoly = scalePoly(poly2, -1);
    Poly output =  addPolys(poly1, negativePoly);
    return AdjustPoly(output);
}

PolyXY subtractPolysXY(PolyXY poly1, PolyXY poly2){

}