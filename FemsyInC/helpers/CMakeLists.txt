add_library(helper STATIC InputHelper.c
        helper.h
        HelperTest.h
        HelperTest.c
        transformationHelper.c
)

target_link_libraries(helper PUBLIC coordinateSystem)
