import pytest

import biblioteki.vectors.vect_math

from biblioteki.matr_pom.macierze_num import reduce_matrix
from programy.mes_obliczenia_1_2.transformacje_macierzy import *
from programy.mes_obliczenia_1_2.wyjatki_i_checki import check_równości_pierdolonych_list as chck


@pytest.mark.parametrize('vect', [([1, 0, 0]), ([0, 1, 0]), ([0, 0, 1]), ([-1, 0, 0]), ([0, -1, 0]), ([0, 0, -1])])
def test_lin_base_righthanded(vect):
    """sparawdza czy generowane ukłądy są prawoskrętne"""
    temp = biblioteki.vectors.vect_math.lin_base(vect)
    temp_vect = np.cross(temp[0], temp[1])
    np.testing.assert_array_equal(temp_vect, temp[2])


class TestReduceMatr:
    """testuje reduce_matr w sposób bezpośredni """

    def test_co_trzeci(self, macierz_wezlow_1):
        assert chck(reduce_matrix(macierz_wezlow_1), np.array([[0, 1, 0, 0, 0, 0],
                                                               [0, 0, 0, 0, 0, 0],
                                                               [1, 0, 0, 0, 0, 0]]))

    def test_co_drugi(self, macierz_wezlow_1):
        assert chck(reduce_matrix(macierz_wezlow_1, 2), np.array([[0, 0, 0, 0, 0],
                                                                  [3, 0, 0, 0, -0.05]]))
