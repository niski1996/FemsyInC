//
// Created by kali on 12/31/24.
//
#include <stdio.h>
#include "core/polynomial/PolyTest.h"
#include "core/element/elementTest.h"
#include  "helpers/HelperTest.h"
#include "core/vector/vectorTest.h"
#include "core/coordinateSystem/coordinateSystemTest.h"
#include "core/matrix/matrixTest.h"

void RunAllTests() {
    PolyTest();
    elementTest();
    // coordinateSystemTest();
    // vectorTest();
    // HelperTest();
    // matrixTest();
}
