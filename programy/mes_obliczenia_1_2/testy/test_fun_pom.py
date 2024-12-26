import sys
sys.path.append('/')
try:
    from programy.mes_obliczenia_1_2.wyjatki_i_checki import check_równości_pierdolonych_list
    from programy.mes_obliczenia_1_2.funkcje_pomocnicze import *
except ImportError:
    import sys, os
    # print(os.path)


#
# class TestArgDos:
#     pass
# class TestAddCon:
#     pass
#

def test_nodes_coord_separate(macierz_elementow_1, macierz_wezlow_1):
    actual = nodes_coord_separate(macierz_elementow_1,macierz_wezlow_1)
    expected = [[(0.0, 1.0, 0.0), (0.0, 0.0, 0.0)], [(3.0, 3.0, 0.0), (1.0, 0.0, 0.0)],
                    [(0.0, 1.0, 0.0), (3.0, 3.0, 0.0)], [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0)],
                    [(0.0, 1.0, 0.0), (1.0, 0.0, 0.0)]]

    assert check_równości_pierdolonych_list(actual, expected)
