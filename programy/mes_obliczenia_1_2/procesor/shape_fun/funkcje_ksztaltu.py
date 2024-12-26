import numpy as np

from programy.mes_obliczenia_1_2.procesor.shape_fun.elem1d.bar import shape_fun_1d
from programy.mes_obliczenia_1_2.aproks_2d import n_point_surface_polinomial, der_x_y
import functools
import itertools


def shape_fun(type_elem, nodes_coord):
    """dobiera metodę do rodzaju elementu

    Oblicza funkcje kształtu w lokalnym ukłądzie wspłórzędnyvh.
    Układ prawoskrętny, kierunek i zwrot osi x wyznaczają dwa pierwsze
    punkty nodes. W przypadku elementów 2D dodatni za dodatni kierunek przyjmuje się
    kierunek pierwszego kolejnego, niewspółliniowego z dwoma poprzednimi
    węzła w nodes.
    Pierwszy z listy nodes_coord przyjmuje wartość 1, pozostałe 0

    Param
    -------
    dof : int
        liczba stopni swobody
    type : str
        typ elementu (dopuszczalne : 'bar'
    *nodes : tuple
        współrzędne węzłów w układzie globalnym (x, y, z)
        """
    li = []
    if type_elem == 'shield':
        tmp = fuu_val(nodes_coord)
        for zest in tmp:  # to samo co przy 'bar robią target=0, value_index=-1
            for num, row in enumerate(zest):
                zest[num] = list(row)
                zest[num].pop(2)
        for e in tmp:
            li.append(n_point_surface_polinomial(e))
        return li
    elif type_elem == 'bar':
        for e in fuu_val(nodes_coord):
            li.append(shape_fun_1d(e))
        return li
    else:
        raise ValueError('zły typ elementu')


def shape_fun_2d(*nodes):
    pass


def matr_deriv(n):
    """pochodna macierzy list współczynników wielomianów

    Działa tylko dla pochodnej jednej zmiennej

    Params
    -------
    n : array_like
        lista trzypoziomowa zawierająca współczynnki wielomianów
        [[[],[],[]...]
        [[],[],[]...]]

    Return
    -------
    list
        lista trzypoziomowa zawierająca  współczynniki pochodnej wielomianu
    """
    li = []
    for n1, e1 in enumerate(n):
        li.append([])
        for num, fun in enumerate(e1):
            li[n1].append(np.polyder(fun))
    return li


def matr_deriv_xy(n):
    li = []
    for n1, e1 in enumerate(n):
        li.append([])
        for num, fun in enumerate(e1):
            li[n1].append(der_x_y(fun[0], fun[1]))
    return li


def matr_der_ver2(n):
    li = []
    for n1, e1 in enumerate(n):
        li.append([])
        li[n1] = list(map(np.polyder, e1))
    return li


