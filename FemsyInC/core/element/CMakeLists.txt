add_library(element STATIC element.c element.c elementTest.h elementTest.c)
target_link_libraries(element PUBLIC poly)