add_library(helper STATIC
        helper.h
        HelperTest.h
        HelperTest.c
        transformationHelper.c
)

target_link_libraries(helper PUBLIC coordinateSystem)
