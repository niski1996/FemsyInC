# from mes_obliczenia.funkcje_ksztaltu import *
import pytest
# from mes_obliczenia.wyjatki_i_checki import ZlyRozmiarListyError, check_równości_pierdolonych_list
# from mes_obliczenia_1_0.conftest import *
import numpy as np


class TestFuuVal:
    """Sprawdza fuu_val

    sprawdza ilość kombinacji, wymiary macierzy wynikowej oraz niektóre wyjątki
    NIE sprawdza poprawnośći typu danych w tablicy, oraz prawdziwości wyników"""

    @pytest.mark.parametrize('nodes', ["krotka_wezlow_w_ukladzie_3d",
                                       "krotka_wezlow_w_ukladzie_2d"])
    def test_amount_of_comb(self, nodes, request):
        """sprawdza czy liczba kombinacji jest właściwa"""
        nodes = request.getfixturevalue(nodes)
        assert len(nodes) == len(fuu_val(nodes))

    @pytest.mark.parametrize('nodes', [("krotka_wezlow_w_ukladzie_3d"),
                                       ("krotka_wezlow_w_ukladzie_2d")])
    def test_shape(self, nodes, request):  # TODO niech zwraca komunikaty, bo nie daje informacji o bledach
        """sprawdza wymiary listy wynikowej"""
        nodes = request.getfixturevalue(nodes)
        dim1 = len(nodes)
        dim2 = len(nodes[0])
        target = fuu_val((nodes))
        for elem in target:
            if len(elem) != dim1:
                assert False
            else:
                for nod in elem:
                    if len(nod) != (dim2 + 1):
                        assert False
        assert True

    @pytest.mark.parametrize('nodes', ['krotka_wezły_wadliwe_1'])
    def test_wrong_input(self, nodes, request):
        """sprawdza wyjątki tabl,icy o nieprawidłowych rozmiarach"""

        nodes = request.getfixturevalue(nodes)
        with pytest.raises(ZlyRozmiarListyError):
            target = fuu_val((nodes))


@pytest.mark.parametrize('nodes,expect', [(((0, 0), (1, 1)), [1.0, 0.0]),
                                          (((0, 1), (1, 3)), [2.0, 1.0])])
def test_shape_fun_1d_simple(nodes, expect):
    x = 2
    np.testing.assert_array_almost_equal(np.array(expect), shape_fun_1d(nodes))


def test_mat_deriv(lista_trzypoziomowa):
    tmp = [[[4],[6, 4], ],
           [[5], [9]]]
    tmp2=matr_deriv(lista_trzypoziomowa)
    assert check_równości_pierdolonych_list(tmp, tmp2)

def test_mat_der_ver2(lista_trzypoziomowa):
    tmp = [[[4],[6, 4], ],
           [[5], [9]]]
    tmp2=matr_der_ver2(lista_trzypoziomowa)
    assert check_równości_pierdolonych_list(tmp, tmp2)

