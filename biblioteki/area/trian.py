""" contain all mrthot to calculate area using trangle"""
import math

import numpy as np


def sur_area_by_points(*points):
    """
    count area of any figure defined by points

    count approximate area of figure by addition trangles spread on first point and two adjacent points
    Non-convent figure are not allowed. Points must be in the order. Points on straight line are allowed

    :param points:array_like
        2D or 3D points
    :return:float
        area
    """
    first = points[0]
    area = 0
    for num in range(len(points) - 2):
        area += area_trian_set_by_points(first, points[num + 1], points[num + 2])
    return area


def area_trian_set_by_points(*points):
    """

    :param points:
    :return:
    """
    if len(points) != 3:
        raise ValueError('zła ilość punktów do obliczeń pola')
    vec1 = np.array(points[0]) - np.array(points[1])
    vec2 = np.array(points[1]) - np.array(points[2])
    area = np.linalg.norm(np.cross(vec1, vec2)) / 2
    return area


def sur_area_by_arrays(*points):
    """
    count area of any figure defined by points

    count approximate area of figure by addition trangles spread on first point and two adjacent points
    Non-convent figure are not allowed. Points must be in the order. Points on straight line are allowed

    :param points:array_like
        2D or 3D points
    :return:float
        area
    """
    first = points[0]
    area = 0
    for num in range(len(points) - 2):
        area += area_trian_set_by_array(*first, *points[num + 1], *points[num + 2])
    return area


def area_trian_set_by_array(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    """
    count area of triangles

    returns array of triangle areas, whear corner points are passed in shape of arrays.

    :param x1:
    :param y1:
    :param z1:
    :param x2:
    :param y2:
    :param z2:
    :param x3:
    :param y3:
    :param z3:
    :return:
    """
    vec1x = x1 - x2
    vec1y = y1 - y2
    vec1z = z1 - z2

    vec2x = x1 - x3
    vec2y = y1 - y3
    vec2z = z1 - z3

    i = vec1y * vec2z - vec1z * vec2y
    j = vec1z * vec2x - vec1x * vec2z
    k = vec1x * vec2y - vec1y * vec2x

    i = i ** 2
    j = j ** 2
    k = k ** 2

    sum = i + k + j
    return sum ** (0.5) / 2

# x0=np.linspace(0,1000,1000)
# y0=np.linspace(0,1000,1000)
#
# x1,y1=np.meshgrid(x0,y0)
#
# z1=(x1+y1)*4
# z1=(x1+y1)*4
# area_trian_set_by_array(x1,y1,z1,x1*2,y1*3,z1*4,x1*5,y1*6,z1*7)
