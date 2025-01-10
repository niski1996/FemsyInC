add_library(coordinateSystem STATIC
        coordinateSystem.c
        coordinateSystem.h
        coordinateSystemTest.c
        coordinateSystemTest.h
)

target_link_libraries(coordinateSystem PUBLIC model)
target_link_libraries(coordinateSystem PUBLIC GSL::gsl GSL::gslcblas)
target_link_libraries(coordinateSystem PUBLIC vector)
target_link_libraries(coordinateSystem PUBLIC matrix)