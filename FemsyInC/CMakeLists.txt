cmake_minimum_required(VERSION 3.30)
project(FemsyInC C)

set(CMAKE_C_STANDARD 23)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall")
find_package(GSL REQUIRED)
add_executable(FemsyInC main.c
        Test.c
        Test.h)
add_subdirectory(engine)
add_subdirectory(models)
add_subdirectory(helpers)
target_link_libraries(FemsyInC PRIVATE coordinateSystem)
target_link_libraries(FemsyInC PRIVATE vector)
target_link_libraries(FemsyInC PRIVATE poly)
target_link_libraries(FemsyInC PRIVATE model)
target_link_libraries(FemsyInC PRIVATE helper)
target_link_libraries(FemsyInC PRIVATE GSL::gsl GSL::gslcblas)