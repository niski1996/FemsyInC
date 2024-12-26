import abc
import math
import numpy as np


class Dane(abc.ABC):
    def __init__(self):
        pass

    def nodes(self):
        """wczytuje tablicę węzłów

        Zwraca
        -------
        numpy.ndarray
            współrzędne x,y,z
        """
        pass

    def initial_disp(self):
        """wczytuje tablicę przemieszczen

        Zwraca
        -------
        numpy.ndarray
            przemieszczenia węzła x,y,z
        """
        pass

    def initial_force(self):
        """wczytuje tablicę sił

        Zwraca
        -------
        numpy.ndarray
            składowe sił węzła x,y,z
        """
        pass

    def initial_deflection(self):
        """wczytuje tablicę ugięć i skręceń

        Zwraca
        -------
        numpy.ndarray
            obroty wokół osi x,y,z
        """
        pass

    def initial_moment(self):
        """wczytuje tablicę momentów
        Zwraca
        -------
        numpy.ndarray
            momenty wokół osi x,y,z
        """
        pass

    def elements(self):
        """wczytuje tablicę elementów

        Zwraca
        -------
        list
            n-2 kolejnych elem. : numery węzłów
            elem. dim-1 : numer materiału w tablicy materiałów
            elem. dim : typ elementu"""
        pass

    def materials(self):
        """wczytuje tablice materiałów
        :return list
            lista własności materiałwych
                w każdym wierszu:
                [[moduł Younga,
                przekrój poprzeczny dla prętów i belek,
                współczynnik poissona,
                 grubość dla płyt i tarcz...],
                [..."""
        pass

    def bond_cond(self, obr=False):
        """Definiuje warunki brzegowe

        :rtype: numpy.array
            zwraca jednokolumnową macierz zawierającą 1 dla węzłą zablokowwanego,
            oraz 0 dla węzłą swobodnego
        """
        pass

    def forces(self):
        """Definiuje obciążenia

        :rtype: numpy.array
            zwraca jednokolumnową macierz
        """
        li = []
        # for elem in self.initial_force():
        #     li.append(elem[0])
        #     li.append(elem[1])
        #     li.append(elem[2])
        li=list(self.initial_force().flat)
        return np.array(li).reshape((len(li), 1))

    def uklad(self):
        """"Zwraca rodzaj układu elem2d lub 3d"""
        pass

    def expected_disp(self):
        """
        Zwraca oczekiwaną macierz przemieszczeń węzłowych
        :return:
        """
        pass

    def expected_K(self):
        """
        zwraca oczekiwaną macierz sztywności
        :return:
        """
        pass

    def expected_react(self):
        """
        zwraca oczekiwane reakcje
        :return:
        """
        pass

    def dof(self):
        """
        liczba stopni swobody
        :return:
        """
        pass


class Dane1(Dane):
    """Rama czterwęzłowa, źródło: https://dbc.wroc.pl/Content/970/PDF/srodka_trzy_lekcje.pdf"""

    def nodes(self):
        return np.array([[0, 1, 0],
                         [0, 0, 0],
                         [3, 3, 0],
                         [1, 0, 0]])

    def dof(self):
        return 3

    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def initial_force(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, -0.05, 0],
                         [0, 0, 0]])

    def elements(self):
        return [
            [0, 1, 0, 'bar'],
            [2, 3, 0, 'bar'],
            [0, 2, 0, 'bar'],
            [1, 3, 0, 'bar'],
            [0, 3, 0, 'bar']]

    def materials(self):
        return [[2e5, 0.001, 0.3]]

    def bond_cond(self):
        return np.array([[0],
                         [0],
                         [1],
                         [1],
                         [1],
                         [1],
                         [0],
                         [0],
                         [1],
                         [0],
                         [1],
                         [1],
                         ])

    def uklad(self):
        return 'elem2d'

    def expected_disp(self):
        return np.array([[1.34852814e-03], [5.00000000e-04], [-5.89805982e-29], [5.00000000e-14], [8.65201064e-03],
                         [-8.11161542e-03], [-5.89805982e-19], [-1.37472163e-13]])

    def expected_K(self):
        return np.array([[109.11299939578592, -45.10913060056726, 0.0, 0.0, -38.4023212771312, -25.601547518087468,
                          -70.71067811865473, 70.71067811865473],
                         [-45.10913060056726, 287.7783764640463, 0.0, -199.99999999999994, -25.601547518087468,
                          -17.067698345391644, 70.71067811865473, -70.71067811865473],
                         [0.0, 0.0, 200.0, 0.0, 0.0, 0.0, -199.99999999999994, 0.0],
                         [0.0, -199.99999999999994, 0.0, 200.0, 0.0, 0.0, 0.0, 0.0],
                         [-38.4023212771312, -25.601547518087468, 0.0, 0.0, 55.47001962252291, 51.20309503617501,
                          -17.067698345391687, -25.601547518087532],
                         [-25.601547518087468, -17.067698345391644, 0.0, 0.0, 51.20309503617501, 55.47001962252294,
                          -25.601547518087536, -38.4023212771313],
                         [-70.71067811865473, 70.71067811865473, -199.99999999999994, 0.0, -17.067698345391687,
                          -25.601547518087532, 287.77837646404635, -45.10913060056719],
                         [70.71067811865473, -70.71067811865473, 0.0, 0.0, -25.601547518087536, -38.4023212771313,
                          -45.109130600567184, 109.11299939578603]])

    def expected_react(self):
        return np.array([[-2.77555756e-17], [0.00000000e+00], [1.17961196e-16], [-1.00000000e-01], [5.55111512e-17],
                         [1.38777878e-17], [5.55111512e-17], [1.50000000e-01]])


class Dane2(Dane):
    """tarcza prostokatna, dwuelementowa, dwa przeguby z lewej strony"""

    def nodes(self):
        return np.array([[0, 0, 0],
                         [0.5, 0, 0],
                         [0.5, 0.25, 0],
                         [0, 0.25, 0]])

    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def initial_force(self):
        return np.array([[0, 0, 0],
                         [9375, 0, 0],
                         [9375, 0, 0],
                         [0, 0, 0]])

    def bond_cond(self, obr=False):
        b = np.array([[1, 1, 1],
                      [0, 0, 1],
                      [0, 0, 1],
                      [1, 1, 1]])
        return b.reshape(int(len(b) * 3), 1)

    def dof(self):
        return 3

    def elements(self):
        return [[0, 2, 3, 0, 'shield'],
                [0, 1, 2, 0, 'shield']
                ]

    def materials(self):
        return [[2.1e10, None, 0.3, 0.25]]


class Dane2_1(Dane2):
    def nodes(self):
        return np.array([[0, 0, 0],
                         [0.5, 0, 0],
                         [0.5, 0.1767, 0.1767],
                         [0, 0.1767, 0.1767]])


class Dane22(Dane2):
    def initial_force(self):
        return np.array([[0, 0, 0],
                         [0, 1, 0],
                         [0, 0, 0],
                         [0, 0, 0]])


class Dane22_1(Dane2):
    def nodes(self):
        return np.array([[0, 0, 0],
                         [0.5, 0, 0],
                         [0.5, 0.1767, 0.1767],
                         [0, 0.1767, 0.1767]])

    def initial_force(self):
        return np.array([[0, 0, 0],
                         [0, 1.41, 1.41],
                         [0, 0, 0],
                         [0, 0, 0]])


class Dane3(Dane):
    """ tarcza kwadratowa obrócona o 45 stopni,
    dwa przeguby blokujące x,y"""

    def nodes(self):
        return np.array([[0.5, 0, 0],
                         [0, 0.5, 0],
                         [0.5, 0.5, 0],
                         [1, 0.5, 0],
                         [0.5, 1, 0]])

    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def initial_force(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [100000, 0, 0]])

    def dof(self):
        return 3

    def elements(self):  # TODO przekroje i  elementy nie muszą być izometryczne, rozważyć dodanie kolejnych parametrów
        return [[0, 2, 1, 0, 'shield'],
                [1, 2, 4, 0, 'shield'],
                [2, 4, 3, 0, 'shield'],
                [0, 2, 3, 0, 'shield']]

    def bond_cond(self, obr=False):
        b = np.array([[1, 1, 1],
                      [1, 1, 1],
                      [0, 0, 1],
                      [0, 0, 1],
                      [0, 0, 1]])
        return b.reshape(int(len(b) * 3), 1)

    def materials(self):
        return [[2e11, None, 0.3, 0.01]]


class Dane4(Dane):
    """snopek 3d"""

    def nodes(self):
        return np.array([[0.32, 1.5, 0.18],
                         [0., 0, 0],
                         [0.64, 0, 0],
                         [0.32, 0, 0.55]])

    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def initial_force(self):
        return np.array([[0, 0.2, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def elements(self):
        return [[0, 1, 0, 'bar'],
                [0, 2, 0, 'bar'],
                [0, 3, 0, 'bar']]

    def bond_cond(self):
        return np.array([[0],
                         [0],
                         [0],
                         [1],
                         [1],
                         [1],
                         [1],
                         [1],
                         [1],
                         [1],
                         [1],
                         [1],
                         ])

    def materials(self):
        return [[1e7, 0.0012566]]

    def dof(self):
        return 3


class Dane5(Dane):
    """
    kostka sześcienna z zastrzałami
    """

    def nodes(self):
        return np.array([[0, 0, 0],
                         [0, 2, 0],
                         [2, 2, 0],
                         [2, 0, 0],
                         [0, 0, 2],
                         [0, 2, 2],
                         [2, 2, 2],
                         [2, 0, 2], ])

    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def initial_force(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [5, 5, 5],
                         [0, 0, 0]])

    def elements(self):
        return [[0, 1, 0, 'bar'],
                [0, 3, 0, 'bar'],
                [0, 4, 0, 'bar'],
                [0, 7, 0, 'bar'],
                [1, 2, 0, 'bar'],
                [1, 4, 0, 'bar'],
                [1, 6, 0, 'bar'],
                [1, 5, 0, 'bar'],
                [2, 3, 0, 'bar'],
                [2, 6, 0, 'bar'],
                [2, 7, 0, 'bar'],
                [3, 7, 0, 'bar'],
                [4, 5, 0, 'bar'],
                [4, 7, 0, 'bar'],
                [5, 6, 0, 'bar'],
                [6, 7, 0, 'bar']]

    def materials(self):
        return [[2.1e7, np.pi * 0.015 ** 2]]

    def bond_cond(self, obr=False):
        b = np.array([[1, 1, 1],
                      [1, 1, 1],
                      [0, 1, 1],
                      [0, 1, 1],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]])
        return b.reshape(int(len(b) * 3), 1)

    def dof(self):
        return 3


class Dane6(Dane):
    """tarcza trapezowa, dwuelementowa, dwa przeguby z lewej strony
    http://albert.kubzdela.pracownik.put.poznan.pl/p6-10.pdf"""

    def nodes(self):
        return np.array([[0, 1.5, 0],
                         [0, 0, 0],
                         [2, 0.5, 0],
                         [2, 1.5, 0]])

    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def initial_force(self):
        return np.array([[0, 0, 0],
                         [9.375, 0, 0],
                         [9.375, 0, 0],
                         [0, 0, 0]])

    def bond_cond(self, obr=False):
        b = np.array([[1, 1, 1],
                      [0, 0, 1],
                      [0, 0, 1],
                      [1, 1, 1]])
        return b.reshape(int(len(b) * 3), 1)

    def dof(self):
        return 3

    def elements(self):
        return [
            [0, 1, 2, 0, 'shield'],
            [0, 2, 3, 0, 'shield']
        ]

    def materials(self):
        return [[2.5e10, None, 0.16, 0.2]]
    # def materials(self):
    #     return [[2.1e7, np.pi * 0.015 ** 2]]


class Dane7(Dane):
    """ tarcza kwadratowa obrócona o 45 stopni,
    dwa przeguby blokujące x,y"""

    def nodes(self):
        return np.array([[0, 0, 0],
                         [0, 1, 0],
                         [1, 0, 0],
                         [0, 0, 1], ])

    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def initial_force(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [1, 0, 0]])

    def dof(self):
        return 3

    def elements(self):  # TODO przekroje i  elementy nie muszą być izometryczne, rozważyć dodanie kolejnych parametrów
        return [[0, 1, 2, 0, 'shield'],
                [0, 1, 3, 0, 'shield'],
                [0, 2, 3, 0, 'shield'],
                [1, 2, 3, 0, 'shield']]

    def bond_cond(self, obr=False):
        b = np.array([[1, 1, 1],
                      [1, 1, 1],
                      [1, 1, 1],
                      [0, 0, 0]])
        return b.reshape(int(len(b) * 3), 1)

    def materials(self):
        return [[2e7, None, 0.3, 0.1]]


class Dane7_1(Dane7):
    def nodes(self):
        return np.array([[0, 0, 0],
                         [0, 1, 0],
                         [0.707, 0, 0.707],
                         [-0.707, 0, 0.707], ])

    def initial_force(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0.707, 0, 0.707]])


class Dane2(Dane):
    """tarcza prostokatna, dwuelementowa, dwa przeguby z lewej strony"""

    def nodes(self):
        return np.array([[0, 0, 0],
                         [0.5, 0, 0],
                         [0.5, 0.25, 0],
                         [0, 0.25, 0]])

    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def initial_force(self):
        return np.array([[0, 0, 0],
                         [9.375, 0, 0],
                         [9.375, 0, 0],
                         [0, 0, 0]])

    def bond_cond(self, obr=False):
        b = np.array([[1, 1, 1],
                      [0, 0, 1],
                      [0, 0, 1],
                      [1, 1, 1]])
        return b.reshape(int(len(b) * 3), 1)

    def dof(self):
        return 3

    def elements(self):
        return [[0, 2, 3, 0, 'shield'],
                [0, 1, 2, 0, 'shield']
                ]

    def materials(self):
        return [[2.1e7, None, 0.3, 0.25]]


class Walec1(Dane):
    """"""

    def nodes(self):
        return np.array([[0, 0, 0],
                         [0, 10, 0],
                         [20, 0, 20],
                         [20, 10, 20],
                         [40, 0, 0],
                         [40, 10, 0]])

    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def initial_force(self):
        f = 4
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 1],
                         [0, 0, 1],
                         [0, 0, 0],
                         [0, 0, 0]]) * f

    def bond_cond(self, obr=False):
        b = np.array([[1, 1, 1],
                      [1, 1, 1],
                      [0, 0, 0],
                      [0, 0, 0],
                      [1, 1, 1],
                      [1, 1, 1]])
        return b.reshape(int(len(b) * 3), 1)

    def dof(self):
        return 3

    def elements(self):
        return [[0, 1, 2, 0, 'shield'],
                [1, 2, 3, 0, 'shield'],
                [2, 3, 5, 0, 'shield'],
                [2, 4, 5, 0, 'shield'],
                ]

    def materials(self):
        return [[2.1e7, None, 0.3, 0.25]]


class Walec2(Dane):
    """"""

    def nodes(self):
        return np.array([[0, 0, 0],
                         [0, 1, 0],
                         [10, 0, 17.32],
                         [10, 1, 17.32],
                         [30, 0, 17.32],
                         [30, 1, 17.32],
                         [40, 0, 0],
                         [40, 1, 0]])

    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def initial_force(self):
        f = 250
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [-0.5, 0, 0.87],
                         [-0.5, 0, 0.87],
                         [0.5, 0, 0.87],
                         [0.5, 0, 0.87],
                         [0, 0, 0],
                         [0, 0, 0]]) * f

    def bond_cond(self, obr=False):
        b = np.array([[1, 1, 1],
                      [1, 1, 1],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [1, 1, 1],
                      [1, 1, 1]])
        return b.reshape(int(len(b) * 3), 1)

    def dof(self):
        return 3

    def elements(self):
        return [[0, 1, 2, 0, 'shield'],
                [1, 2, 3, 0, 'shield'],
                [2, 3, 5, 0, 'shield'],
                [2, 4, 5, 0, 'shield'],
                [4, 5, 6, 0, 'shield'],
                [5, 6, 7, 0, 'shield'],
                ]

    def materials(self):
        return [[1e6, None, 0.3, 0.01]]


class Walec3(Dane):
    """"""

    def nodes(self):
        return np.array([[0, 1, 0],
                         [0, 0, 0],
                         [3.819, 1, 11.755],
                         [3.819, 0, 11.755],
                         [13.819, 1, 19.021],
                         [13.819, 0, 19.021],
                         [26.18, 1, 19.021],
                         [26.18, 0, 19.021],
                         [36.18, 1, 11.755],
                         [36.18, 0, 11.755],
                         [40, 1, 0],
                         [40, 0, 0]])

    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def initial_force(self):
        f = 250
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [-0.81, 0, 0.59],
                         [-0.81, 0, 0.59],
                         [-0.31, 0, 0.95],
                         [-0.31, 0, 0.95],
                         [0.31, 0, 0.95],
                         [0.31, 0, 0.95],
                         [0.81, 0, 0.59],
                         [0.81, 0, 0.59],
                         [0, 0, 0],
                         [0, 0, 0]]) * f

    def bond_cond(self, obr=False):
        b = np.array([[1, 1, 1],
                      [1, 1, 1],
                      [0, 1, 0],
                      [0, 0, 0],
                      [0, 1, 0],
                      [0, 0, 0],
                      [0, 1, 0],
                      [0, 0, 0],
                      [0, 1, 0],
                      [0, 0, 0],
                      [1, 1, 1],
                      [1, 1, 1]])
        return b.reshape(int(len(b) * 3), 1)

    def dof(self):
        return 3

    def elements(self):
        return [[0, 1, 2, 0, 'shield'],
                [1, 2, 3, 0, 'shield'],
                [2, 3, 5, 0, 'shield'],
                [2, 4, 5, 0, 'shield'],
                [4, 5, 6, 0, 'shield'],
                [5, 6, 7, 0, 'shield'],
                [6, 7, 9, 0, 'shield'],
                [6, 8, 9, 0, 'shield'],
                [8, 9, 10, 0, 'shield'],
                [9, 10, 11, 0, 'shield'],
                ]

    def materials(self):
        return [[1e6, None, 0.3, 0.01]]


class Walec31(Walec3):
    def elements(self):
        return [[2, 1, 0, 0, 'shield'],
                [3, 2, 1, 0, 'shield'],
                [2, 5, 3, 0, 'shield'],
                [4, 5, 2, 0, 'shield'],
                [6, 5, 4, 0, 'shield'],
                [5, 7, 4, 0, 'shield'],
                [6, 9, 7, 0, 'shield'],
                [6, 8, 9, 0, 'shield'],
                [8, 9, 10, 0, 'shield'],
                [9, 10, 11, 0, 'shield'],
                ]


class Tarcza3(Dane):
    """"""

    def nodes(self):
        return np.array([[0, 1, 0],
                         [0, 0, 0],
                         [3.819, 1, 0],
                         [3.819, 0, 0],
                         [13.819, 1, 0],
                         [13.819, 0, 0],
                         [26.18, 1, 0],
                         [26.18, 0, 0],
                         [36.18, 1, 0],
                         [36.18, 0, 0],
                         [40, 1, 0],
                         [40, 0, 0]])

    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def initial_force(self):
        f = 250
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 1, 0],
                         [0, 0, 0]]) * f

    def bond_cond(self, obr=False):
        b = np.array([[1, 1, 1],
                      [1, 1, 1],
                      [0, 0, 1],
                      [0, 0, 1],
                      [0, 0, 1],
                      [0, 0, 1],
                      [0, 0, 1],
                      [0, 0, 1],
                      [0, 0, 1],
                      [0, 0, 1],
                      [0, 0, 1],
                      [0, 0, 1]])
        return b.reshape(int(len(b) * 3), 1)

    def dof(self):
        return 3

    def elements(self):
        return [[0, 1, 2, 0, 'shield'],
                [1, 2, 3, 0, 'shield'],
                [2, 3, 5, 0, 'shield'],
                [2, 4, 5, 0, 'shield'],
                [4, 5, 6, 0, 'shield'],
                [5, 6, 7, 0, 'shield'],
                [6, 7, 9, 0, 'shield'],
                [6, 8, 9, 0, 'shield'],
                [8, 9, 10, 0, 'shield'],
                [9, 10, 11, 0, 'shield'],
                ]

    def materials(self):
        return [[2.1e7, None, 0.3, 0.25]]

class Tarcza31(Tarcza3):
    def elements(self):
        return [[2, 1, 0, 0, 'shield'],
                [3, 2, 1, 0, 'shield'],
                [2, 5, 3, 0, 'shield'],
                [2, 4, 5, 0, 'shield'],
                [6, 5, 4, 0, 'shield'],
                [5, 6, 7, 0, 'shield'],
                [6, 9, 7, 0, 'shield'],
                [6, 8, 9, 0, 'shield'],
                [8, 9, 10, 0, 'shield'],
                [9, 10, 11, 0, 'shield'],
                ]



