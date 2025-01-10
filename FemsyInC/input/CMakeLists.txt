add_library(parser STATIC
parser.c
parser.h
)

target_link_libraries(parser PUBLIC GSL::gsl GSL::gslcblas)
