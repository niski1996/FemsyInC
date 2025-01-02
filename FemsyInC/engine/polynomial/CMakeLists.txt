add_library(poly STATIC
        PolyCompare.c
        PolyAdd.c
        PolyCreate.c
        PolyFree.c
        PolyHelper.c
        PolyHelper.c
        PolyMultiply.c
        PolyHelper.h
        Poly.h
        PolyPrint.c
        PolySubtract.c
        PolyTest.c
        PolyTest.h
        PolyEvaluate.c
        PolyDerivate.c
        PolyIntegrate.c)

target_link_libraries(poly m)