cmake_minimum_required(VERSION 3.30)
project(FemsyInC C)

set(CMAKE_C_STANDARD 23)

add_executable(FemsyInC main.c
        Test.c
        Test.h
)
add_subdirectory(engine)
target_link_libraries(FemsyInC PRIVATE poly)
