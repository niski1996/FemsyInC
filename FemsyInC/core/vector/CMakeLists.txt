add_library(vector STATIC
        vector.h
        product.c
        vectorTest.h
        vectorTest.c
        unitVector.c)

target_link_libraries(vector PUBLIC GSL::gsl GSL::gslcblas)