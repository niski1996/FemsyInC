import math

import numpy as np
import pytest

from biblioteki.area import trian


def test_tran_flat1():
    d = trian.sur_area_by_points([0, 0, 0], [0, 0, 1], [0, 1, 0])
    assert d == 0.5


def test_tran_flat1_2d():
    d = trian.sur_area_by_points([0, 0], [0, 1], [1, 0])
    assert d == 0.5


def test_tran_flat2():
    d = trian.sur_area_by_points([0, 0, 1], [0, 0, 0], [0, 1, 0])
    assert d == 0.5


def test_square_flat1():
    d = trian.sur_area_by_points([0, 0, 0], [0, 1, 0], [1, 1, 0], [1, 0, 0])
    assert d == 1


def test_square_flat2():
    d = trian.sur_area_by_points([0, 0, 1], [0, 1, 1], [1, 1, 0], [1, 0, 0])
    assert d == math.sqrt(2)


@pytest.fixture
def poi_random():
    xrange = (0, 1000)
    yrange = (0, 1000)
    dens = 100
    xstep = (xrange[1] - xrange[0]) / dens
    ystep = (yrange[1] - yrange[0]) / dens
    x = np.linspace(xrange[0], xrange[1] - xstep, dens)
    y = np.linspace(yrange[0], yrange[1] - ystep, dens)
    xleft, ydown = np.meshgrid(x, y)
    xright = xleft + xstep
    yup = ydown - ystep
    z_left_up = (np.random.random(100 * 100) * 100).reshape(100, 100)
    z_left_down = (np.random.random(100 * 100) * 100).reshape(100, 100)
    z_right_up = (np.random.random(100 * 100) * 100).reshape(100, 100)
    z_right_down = (np.random.random(100 * 100) * 100).reshape(100, 100)
    return (xleft, yup, z_left_up), (xright, yup, z_right_up), (xright, ydown, z_right_down), (
        xleft, ydown, z_left_down)


@pytest.fixture
def poi_one_trian():
    xleft = np.array([[0]])
    yup = np.array([[1]])
    z_left_up = np.array([[0]])
    xright = np.array([[1]])
    ydown = np.array([[0]])
    z_right_up = np.array([[0]])
    z_right_down = np.array([[0]])
    return (xleft, yup, z_left_up), (xright, yup, z_right_up), (xright, ydown, z_right_down)


@pytest.fixture
def poi_one_trian1():
    xleft = np.array([[0.5]])
    yup = np.array([[1]])
    z_left_up = np.array([[0]])
    xright = np.array([[1]])
    ydown = np.array([[0]])
    z_right_up = np.array([[0]])
    z_right_down = np.array([[0]])
    return (xleft, yup, z_left_up), (xright, yup, z_right_up), (xright, ydown, z_right_down)

@ pytest.fixture
def poi_one_trian2():
    return (np.array([[0]]), np.array([[0]]), np.array([[0]])), (np.array([[3]]), np.array([[2]]), np.array([[0]])), (
    np.array([[3]]), np.array([[-4]]), np.array([[0]]))


def test_area_trian_set_by_array_value(poi_one_trian):
    lu, ru, rd= poi_one_trian
    are = trian.area_trian_set_by_array(*lu, *ru, *rd)
    assert are[0][0]==0.5

def test_area_trian_set_by_array_value1(poi_one_trian1):
    lu, ru, rd = poi_one_trian1
    are = trian.area_trian_set_by_array(*lu, *ru, *rd)
    assert are[0][0] == 0.25

def test_area_trian_set_by_array_value2(poi_one_trian2):
    lu, ru, rd = poi_one_trian2
    are = trian.area_trian_set_by_array(*lu, *ru, *rd)
    assert are[0][0] == 9

def test_area_trian_set_by_array_random(poi_random):
    lu,ru,rd,ld=poi_random
    are=trian.area_trian_set_by_array(*lu,*ru,*rd)

    def format_to_points(arr_set):
        """
        change arrays of arguments to list of points
        :param arr_set:
        :return:
        """
        x = arr_set[0].flatten()
        y = arr_set[1].flatten()
        z = arr_set[2].flatten()
        return list(zip(x, y, z))

    plu = format_to_points(lu)
    pru =format_to_points(ru)
    prd = format_to_points(rd)


    poi_set = list(zip(plu, pru, prd,))
    li = []
    for pset in poi_set:
        li.append(trian.sur_area_by_points(*pset))
    poi= np.array(li).reshape(100, 100)
    assert np.array_equal(np.round(poi,2),np.round(are,2))

