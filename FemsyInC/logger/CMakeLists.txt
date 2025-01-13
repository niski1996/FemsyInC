add_library(logger STATIC
       logger.h
        customTypeLogger.c
        collectionLogger.c
        standardLogger.c
        )

target_link_libraries(logger PUBLIC GSL::gsl GSL::gslcblas)
target_link_libraries(logger PUBLIC model)
target_link_libraries(logger PUBLIC poly)