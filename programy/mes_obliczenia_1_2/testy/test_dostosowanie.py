import pytest
import numpy as np
import programy.mes_obliczenia_1_2.funkcje_pomocnicze as pom



@pytest.mark.parametrize('local,node1,node2,dim,res', [
    (np.array([[1, -1],
               [-1, 1]]), 0, 2, 4, np.array([[1, 0, -1, 0],
                                             [0, 0, 0, 0],
                                             [-1, 0, 1, 0],
                                             [0, 0, 0, 0]])),
    (np.array([[1, 2, 8, 3],
               [2, 4, 24, 4],
               [8, 24, 3, 32],
               [3, 4, 32, 23]]), 0, 2, 8, np.array([[1, 2, 0, 0, 8, 3, 0, 0],
                                                    [2, 4, 0, 0, 24, 4, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0],
                                                    [8, 24, 0, 0, 3, 32, 0, 0],
                                                    [3, 4, 0, 0, 32, 23, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0]])),
    (np.array([[7, -1],
               [-1, 9]]), 0, 3, 4, np.array([[7, 0, 0, -1],
                                             [0, 0, 0, 0],
                                             [0, 0, 0, 0],
                                             [-1, 0, 0, 9]]))])
def test_dostosowanie(local, node1, node2, dim, res):
    np.testing.assert_array_equal(pom.lokalne_dostosowanie(local, node1, node2, dim), res)


@pytest.mark.parametrize('loc,dim, res, nodes, ', [
    (np.array([[1, -1, 6],
               [-1, 1, 9],
               [6, 9, 19]]), 6, np.array([[1, -1, 0, 0, 0, 6],
                                          [-1, 1, 0, 0, 0, 9],
                                          [0, 0, 0, 0, 0, 0, ],
                                          [0, 0, 0, 0, 0, 0, ],
                                          [0, 0, 0, 0, 0, 0, ],
                                          [6, 9, 0, 0, 0, 19]]), (0, 1, 5)), ])
def test_agreg_dostosowania(loc, dim, res, nodes):
    print('test')
    np.testing.assert_array_equal(pom.agreg_dostosowania(loc, dim, *nodes), res)
