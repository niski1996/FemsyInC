import numpy as np

from programy.mes_obliczenia_1_2.wyjatki_i_checki import check_lista_macierz


def shape_fun_1d(nodes, val):
    """

    :param nodes:
    :param val:
    :return:
    """
    x=[cord[0] for cord in nodes]
    y=[cord[1] for cord in nodes]
    z=[cord[2] for cord in nodes]
    if not all([(lambda: True if round((z[0]-a),4) == 0 else False)() for a in z]):
        raise ValueError("układ lokalny nie jest poprawny, cos jest krzywo")
    if not all([(lambda: True if round((y[0]-a),4) == 0 else False)() for a in y]):
        raise ValueError("układ lokalny nie jest poprawny, cos jest krzywo")
    return np.polynomial.Polynomial(np.flip(np.polyfit(x, val, (len(x) - 1))))



# def fuu_val(nodes_coord):
#     """ustala wartości funkcji w węzłach
#
#     Zwraca wszystkie możliwe kombinacje węzłów, w których jeden wezęł przyjmuje
#     wartość 1, a wszystkie inne 0. Wartość funkcji (val) dodawana jest na ostatniej pozycji,
#     za współrzędnymi zadanymi węzła
#
#     :param
#     nodes_coord : array_like
#         tablica współrzędnych wezłów [[współrzedne wezła 1],[współrzedne wezła 2],...]
#
#     :return
#     list
#         lista kombinacji współrzędnych węzłów (x,y,...,n) powiększonych o zadaną wartość (val) funkcji w punkcie
#         [[[x1,y1,...,n1,1],[x2,y2,...,n2,0]...],
#            x1,y1,...,n1,0],[x2,y2,...,n2,1]...],...]
#     """
#
#     check_lista_macierz(nodes_coord)  # Sprawdza rozmiary listy
#     polylist = []
#     for num in range(len(nodes_coord)):
#         temp = []
#         for num2 in range(len(nodes_coord)):
#             if num == num2:
#                 temp.append((*nodes_coord[num], 1))
#             else:
#                 temp.append((*nodes_coord[num2], 0))
#         polylist.append(temp)
#     return polylist