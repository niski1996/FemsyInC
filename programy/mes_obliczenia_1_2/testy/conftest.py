import pytest
import numpy as np

a = np.pi


@pytest.fixture(scope="module")
def macierz_transformacji_2x2():
    return np.array([[np.cos(a), -np.sin(a)],
                     [np.sin(a), np.cos(a)]])

@pytest.fixture(scope="module")
def krotka_wezlow_w_ukladzie_3d():
    return (2, 4, 6), (4, 6, 7), (3, 90, 34), (64, 34, 43)


@pytest.fixture(scope="module")
def krotka_wezlow_w_ukladzie_2d():
    return (2, 6), (4, 7), (3, 34), (64, 43)

@pytest.fixture(scope="module")
def krotka_wezły_wadliwe_1():
    return (3, 4, 7), (4, 67, 3), (54, 3)

@pytest.fixture(scope="module")
def macierz_transformacji_3x3_z_wspolliniowym_z():
    return np.array([[np.cos(a), -np.sin(a), 0],
                     [np.sin(a), np.cos(a), 0],
                     [0, 0, 1]])


@pytest.fixture(scope="module")
def lista_list_trzyelementowych():
    return [[3, 6, 9], [6, 32, 78], [91, 23, 6]]

@pytest.fixture(scope="module")
def lista_trzypoziomowa():
    return [[[4,3],[3,4,1]],
            [[5,3],[9,8]]]


@pytest.fixture(scope="module")
def macierz_wezlow_1():
    return np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [3, 3, 0, 0, 0, 0, 0, 0, -0.05],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0]])

@pytest.fixture(scope="module")
def macierz_elementow_1():
    return np.array([
        [2, 0, 1, 2e5, 0.001, 'bar'],
        [2, 2, 3, 2e5, 0.001, 'bar'],
        [2, 0, 2, 2e5, 0.001, 'bar'],
        [2, 1, 3, 2e5, 0.001, 'bar'],
        [2, 0, 3, 2e5, 0.001, 'bar']])


@pytest.fixture(scope="module")
def macierz_brzegowa_1():
    return np.array([[0],
                     [0],
                     [0],
                     [1],
                     [1],
                     [0],
                     [0],
                     [0],
                     [0],
                     [0],
                     [1],
                     [0],
                     ])


@pytest.fixture(scope="module")
def macierz_obciazen_1():
    return np.array([[0],
                     [0],
                     [0],
                     [0],
                     [0],
                     [0],
                     [0],
                     [-0.05],
                     [0],
                     [0],
                     [0],
                     [0],
                     ])
