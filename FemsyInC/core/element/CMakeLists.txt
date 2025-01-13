add_library(element STATIC element.c element.c elementTest.h elementTest.c)
link_libraries(element PUBLIC poly)