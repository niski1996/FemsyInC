import numpy as np


class ZlyRozmiarListyError(Exception):
    """lista niemożliwa do sformatowania na macierz"""
    pass

def check_lista_macierz(li):
    """ sprawdza czy liste można sformatować do macierzy

    :param
    li : list, tuple
        dowolna lista, lub krotka. Może być lista elementów, lub lista list.
        Obsługuje listy max dwuwymiarowe

    :return
    True, lub wywołuje wyjątek"""
    if (type(li) != list) and (type(li) != tuple):
        raise TypeError("""type of arg is {}, should be 'list' or 'tuple'""".format(type(li)))
    if hasattr(li[0],'__len__'):
        row_len = len(li[0])
        for e1 in li:
            if len(e1) != row_len:
                raise ZlyRozmiarListyError('dwa wiersze nie pasują do siebie\n{}\n{}'.format(li[0],e1))
            for e2 in e1:
                if hasattr(e2,'__len__'):
                    raise ZlyRozmiarListyError('jeden z elementów ma dodatkowy wymiar')
    else:
        for e1 in li:
            if hasattr(e1,'__len__'):
                raise ZlyRozmiarListyError('jeden z elementów ma dodatkowy wymiar')
    return True


def check_loc(loc):
    """sprawdza wymiary i symetrię macierzy

    Parametry
    ----------
    loc : numpy.ndarray
        macierz węzłów w ukłądzie lokalnym
    """

    a, b = loc.shape
    if not a % 2 == b % 2 == 0:
        raise ValueError('zły wymiar macierzy loc. Powinna byc kwadratowa o parzystej liczbie kolumn i wierszy')
    if not check_równości_pierdolonych_list(loc, np.transpose(loc), 4):
        raise ValueError('macierz loc jest niesymetryczna')


def check_sec(loc, node1, node2, dim):
    """sparawza poprawność wezłów i wymiarów"""
    dof = int(loc.shape[1] / 2)
    if not dim % dof == 0:
        raise ValueError('zły wymiar macierzy globalnej')
    if ((node1 + 1) * dof > dim or (node2 + 1) * dof) > dim:
        raise ValueError('jeden z węzłów poza poza macierzą globalną')
    if node1 == node2:
        raise ValueError('te same numery węzłów')


def full_check(loc, node1, node2, dim):
    check_loc(loc)
    check_sec(loc, node1, node2, dim)


def check_równości_pierdolonych_list(li1, li2, accuracy=None):
    """ porównanie na jkie niezasługujemy, ale jakiego potrzebujemy

    poruwnuje wszystkie elementy w obiektach typu array_like.
    Nie sprawdza typu obiektu, kolejność musi się zgadzać
    jak są liczby to je kurwa zaokrągla do [acuracy] miejsc po przecinku

    :param
    li1, li2 : array_like
        dowolne wymiary i typy
    accuracy : int
        dokładność zaokrąglenia przy porównaniu
        jeżeli None, to tnie zaokrągla

    :return
    bolean"""

    def rekurencja(li, li_v, li_l):
        if not hasattr(li, '__len__'):
            if accuracy is not None:
                try:
                    li_v.append(round(li, accuracy))
                    return 0
                except(ValueError, TypeError):
                    pass
            li_v.append(li)
            return 0
        else:
            li_l.append(len(li))
            for e in li:
                rekurencja(e, li_v, li_l)

    li1_val = []
    li1_len = []
    li2_val = []
    li2_len = []
    rekurencja(li1, li1_val, li1_len)
    rekurencja(li2, li2_val, li2_len)
    if li1_val == li2_val and li1_len == li2_len:
        return True
    else:
        return False

class CheckInput: #TODO    sprawdzać dane wejściowe
    """ sprawdza dane wejściowe"""

    def __init__(self, obiekt):
        """
        :param
        obiekt : obiekt zawierający dane wejściowe
        """
        self.glob_nodes_num = []
        for num, elem in enumerate(obiekt.elements):
            for nod in range(elem[0]):
                pass


    def if_number_and_equal(self, li):
        """sprawdza dwupoziomową listę, czy elementy są równe i są liczbami"""

        comp = len(li[0])
        for elem in li:
            if len(elem) != comp:
                return False
            for num in elem:
                try:
                    float(num)
                except(ValueError,TypeError):
                    return False
