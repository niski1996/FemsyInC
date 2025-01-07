add_library(matrix STATIC
        matrix.h
        matrixHelper.c
        matrixTest.c
        matrixTest.h)

target_link_libraries(matrix PUBLIC GSL::gsl GSL::gslcblas)