add_library(model STATIC types.h
        types.c
)
target_link_libraries(model PUBLIC GSL::gsl GSL::gslcblas)