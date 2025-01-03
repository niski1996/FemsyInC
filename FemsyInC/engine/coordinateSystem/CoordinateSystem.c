//
// Created by kali on 1/3/25.
//

#include "CoordinateSystem.h"

#include <gsl/gsl_vector.h>
#include <gsl/gsl_blas.h>
#include <math.h>
#include "../../models/types.h"
#include "CoordinateSystem.h"

CoordinateSystem *CreateCoordinateSystemFromThreeNonLinearPoints(Point origin, Point pointOnX, Point pointOnXY) {
    CoordinateSystem *coordinateSystem = (CoordinateSystem *)malloc(sizeof(CoordinateSystem));
    if (coordinateSystem == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    // Create vectors for the points
    gsl_vector *vecOX = gsl_vector_alloc(3);
    gsl_vector *vecOXY = gsl_vector_alloc(3);
    gsl_vector *vecZ = gsl_vector_alloc(3);
    gsl_vector *vecY = gsl_vector_alloc(3);

    // Set vecOX = pointOnX - origin
    gsl_vector_set(vecOX, 0, pointOnX.x - origin.x);
    gsl_vector_set(vecOX, 1, pointOnX.y - origin.y);
    gsl_vector_set(vecOX, 2, pointOnX.z - origin.z);

    // Set vecOXY = pointOnXY - origin
    gsl_vector_set(vecOXY, 0, pointOnXY.x - origin.x);
    gsl_vector_set(vecOXY, 1, pointOnXY.y - origin.y);
    gsl_vector_set(vecOXY, 2, pointOnXY.z - origin.z);

    // Calculate vecZ = vecOX x vecOXY (cross product)
    gsl_vector_cross(vecOX, vecOXY, vecZ);

    // Normalize vecZ to get the unit vector
    double normZ = gsl_blas_dnrm2(vecZ);
    gsl_vector_scale(vecZ, 1.0 / normZ);

    // Calculate vecY = vecZ x vecOX (cross product)
    gsl_vector_cross(vecZ, vecOX, vecY);

    // Normalize vecY to get the unit vector
    double normY = gsl_blas_dnrm2(vecY);
    gsl_vector_scale(vecY, 1.0 / normY);

    // Normalize vecOX to get the unit vector
    double normX = gsl_blas_dnrm2(vecOX);
    gsl_vector_scale(vecOX, 1.0 / normX);

    // Set the coordinate system unit vectors
    coordinateSystem->UnitVectorX.x = gsl_vector_get(vecOX, 0);
    coordinateSystem->UnitVectorX.y = gsl_vector_get(vecOX, 1);
    coordinateSystem->UnitVectorX.z = gsl_vector_get(vecOX, 2);

    coordinateSystem->UnitVectorY.x = gsl_vector_get(vecY, 0);
    coordinateSystem->UnitVectorY.y = gsl_vector_get(vecY, 1);
    coordinateSystem->UnitVectorY.z = gsl_vector_get(vecY, 2);

    coordinateSystem->UnitVectorZ.x = gsl_vector_get(vecZ, 0);
    coordinateSystem->UnitVectorZ.y = gsl_vector_get(vecZ, 1);
    coordinateSystem->UnitVectorZ.z = gsl_vector_get(vecZ, 2);

    // Free the allocated vectors
    gsl_vector_free(vecOX);
    gsl_vector_free(vecOXY);
    gsl_vector_free(vecZ);
    gsl_vector_free(vecY);

    return coordinateSystem;
}
