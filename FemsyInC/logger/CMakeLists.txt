add_library(logger STATIC
       logger.h
        gslMatrixLogger.c
        standardLogger.c)

target_link_libraries(logger PUBLIC GSL::gsl GSL::gslcblas)