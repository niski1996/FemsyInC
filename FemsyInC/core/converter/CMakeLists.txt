add_library(converters STATIC collectionConverter.c converter.h)

target_link_libraries(converters PUBLIC model)
target_link_libraries(coordinateSystem PUBLIC GSL::gsl GSL::gslcblas)