import numpy as np
from programy.mes_obliczenia_1_2.testy.dane_test_main import Dane
from biblioteki.vectors.normal_to_dome import vers_norm
import math
from biblioteki.area.dome import DistArea
from biblioteki.area.trian import area_trian_set_by_points


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
        f = 3031
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
        return [[4e9, None, 0.4, 0.0010]]


class Walec5(Dane):
    """"""

    def nodes(self):
        return np.array([[0, 1, 0],
                         [0, 0, 0],
                         [0.384, 1, 3.901],
                         [0.384, 0, 3.901],
                         [1.522, 1, 7.653],
                         [1.522, 0, 7.653],
                         [3.37, 1, 11.111],
                         [3.37, 0, 11.111],
                         [5.857, 1, 14.142],
                         [5.857, 0, 14.142],
                         [8.888, 1, 16.629],
                         [8.888, 0, 16.629],
                         [12.346, 1, 18.477],
                         [12.346, 0, 18.477],
                         [16.098, 1, 19.615],
                         [16.098, 0, 19.615],
                         [20, 1, 20],
                         [20, 0, 20],
                         [23.901, 1, 19.615],
                         [23.901, 0, 19.615],
                         [27.653, 1, 18.477],
                         [27.653, 0, 18.477],
                         [31.111, 1, 16.629],
                         [31.111, 0, 16.629],
                         [34.142, 1, 14.142],
                         [34.142, 0, 14.142],
                         [36.629, 1, 11.11],
                         [36.629, 0, 11.11],
                         [38.477, 1, 7.653],
                         [38.477, 0, 7.653],
                         [39.616, 1, 3.901],
                         [39.616, 0, 3.901],
                         [40, 1, 0],
                         [40, 0, 0]])

    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def initial_force(self):
        f = 480
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [-0.98, 0, 0.20],
                         [-0.98, 0, 0.20],
                         [-0.92, 0, 0.38],
                         [-0.92, 0, 0.38],
                         [-0.83, 0, 0.56],
                         [-0.83, 0, 0.56],
                         [-0.71, 0, 0.71],
                         [-0.71, 0, 0.71],
                         [-0.56, 0, 0.83],
                         [-0.56, 0, 0.83],
                         [-0.38, 0, 0.92],
                         [-0.38, 0, 0.92],
                         [-0.20, 0, 0.98],
                         [-0.20, 0, 0.98],
                         [0, 0, 1],
                         [0, 0, 1],
                         [0.20, 0, 0.98],
                         [0.20, 0, 0.98],
                         [0.38, 0, 0.92],
                         [0.38, 0, 0.92],
                         [0.56, 0, 0.83],
                         [0.56, 0, 0.83],
                         [0.71, 0, 0.71],
                         [0.71, 0, 0.71],
                         [0.83, 0, 0.56],
                         [0.83, 0, 0.56],
                         [0.92, 0, 0.38],
                         [0.92, 0, 0.38],
                         [0.98, 0, 0.20],
                         [0.98, 0, 0.20],
                         [0, 0, 0],
                         [0, 0, 0]]) * f

    def bond_cond(self, obr=False):
        b = np.array([[1, 1, 1],
                      [1, 1, 1],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
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
        a = [[0, 1, 2, 0, 'shield'],
             [1, 2, 3, 0, 'shield'],
             [2, 3, 5, 0, 'shield'],
             [2, 4, 5, 0, 'shield'],
             [4, 5, 6, 0, 'shield'],
             [5, 6, 7, 0, 'shield'],
             [6, 7, 9, 0, 'shield'],
             [6, 8, 9, 0, 'shield'],
             [8, 9, 10, 0, 'shield'],
             [9, 10, 11, 0, 'shield'],
             [10, 11, 13, 0, 'shield'],
             [10, 12, 13, 0, 'shield'],
             [12, 13, 14, 0, 'shield'],
             [13, 14, 15, 0, 'shield'],
             [14, 15, 17, 0, 'shield'],
             [14, 16, 17, 0, 'shield'],
             ]
        b = [el[:] for el in a]
        for num, row in enumerate(b):
            b[num] = [row[0] + 16, row[1] + 16, row[2] + 16, row[3], row[4]]
        a.extend(b)
        return a

    def materials(self):
        return [[4e7, None, 0.4, 0.010]]


class Walec4(Dane):
    """"""

    def nodes(self):
        return np.array([[0, 1, 0],
                         [0, 0, 0],
                         [1.522, 1, 7.653],
                         [1.522, 0, 7.653],
                         [5.857, 1, 14.142],
                         [5.857, 0, 14.142],
                         [12.346, 1, 18.477],
                         [12.346, 0, 18.477],
                         [20, 1, 20],
                         [20, 0, 20],
                         [27.653, 1, 18.477],
                         [27.653, 0, 18.477],
                         [34.142, 1, 14.142],
                         [34.142, 0, 14.142],
                         [38.477, 1, 7.653],
                         [38.477, 0, 7.653],
                         [40, 1, 0],
                         [40, 0, 0]])

    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def initial_force(self):
        f = 975
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [-0.92, 0, 0.38],
                         [-0.92, 0, 0.38],
                         [-0.71, 0, 0.71],
                         [-0.71, 0, 0.71],
                         [-0.38, 0, 0.92],
                         [-0.38, 0, 0.92],
                         [0, 0, 1],
                         [0, 0, 1],
                         [0.38, 0, 0.92],
                         [0.38, 0, 0.92],
                         [0.71, 0, 0.71],
                         [0.71, 0, 0.71],
                         [0.92, 0, 0.38],
                         [0.92, 0, 0.38],
                         [0, 0, 0],
                         [0, 0, 0]]) * f

    def bond_cond(self, obr=False):
        b = np.array([[1, 1, 1],
                      [1, 1, 1],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],
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
                [6, 7, 9, 0, 'shield'],
                [6, 8, 9, 0, 'shield'],
                [8, 9, 10, 0, 'shield'],
                [9, 10, 11, 0, 'shield'],
                [10, 11, 13, 0, 'shield'],
                [10, 12, 13, 0, 'shield'],
                [12, 13, 14, 0, 'shield'],
                [13, 14, 15, 0, 'shield'],
                [14, 15, 17, 0, 'shield'],
                [14, 16, 17, 0, 'shield'],
                ]

    def materials(self):
        return [[4e7, None, 0.4, 0.010]]


class Sur1(Dane):
    """"""

    def nodes(self):
        return np.array([[0, 1, 0],
                         [0, 0, 0],
                         [1.522, 1, 7.653],
                         [1.522, 0, 7.653],
                         [5.857, 1, 14.142],
                         [5.857, 0, 14.142],
                         [12.346, 1, 18.477],
                         [12.346, 0, 18.477],
                         [20, 1, 20],
                         [20, 0, 20],
                         [27.653, 1, 18.477],
                         [27.653, 0, 18.477],
                         [34.142, 1, 14.142],
                         [34.142, 0, 14.142],
                         [38.477, 1, 7.653],
                         [38.477, 0, 7.653],
                         [40, 1, 0],
                         [40, 0, 0]])

    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def initial_force(self):
        f = 975
        return np.array([[0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [-0.92, 0, 0.38, 0, 0, 0],
                         [-0.92, 0, 0.38, 0, 0, 0],
                         [-0.71, 0, 0.71, 0, 0, 0],
                         [-0.71, 0, 0.71, 0, 0, 0],
                         [-0.38, 0, 0.92, 0, 0, 0],
                         [-0.38, 0, 0.92, 0, 0, 0],
                         [0, 0, 1, 0, 0, 0],
                         [0, 0, 1, 0, 0, 0],
                         [0.38, 0, 0.92, 0, 0, 0],
                         [0.38, 0, 0.92, 0, 0, 0],
                         [0.71, 0, 0.71, 0, 0, 0],
                         [0.71, 0, 0.71, 0, 0, 0],
                         [0.92, 0, 0.38, 0, 0, 0],
                         [0.92, 0, 0.38, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0]]) * f

    def bond_cond(self, obr=False):
        b = np.array([[1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1]])
        return b.reshape(int(len(b) * len(b[0])), 1)

    def dof(self):
        return 3

    def elements(self):
        return [[1, 2, 0, 0, 'surface'],
                [1, 2, 3, 0, 'surface'],
                [2, 3, 5, 0, 'surface'],
                [2, 4, 5, 0, 'surface'],
                [4, 5, 6, 0, 'surface'],
                [5, 6, 7, 0, 'surface'],
                [6, 7, 9, 0, 'surface'],
                [6, 8, 9, 0, 'surface'],
                [8, 9, 10, 0, 'surface'],
                [9, 10, 11, 0, 'surface'],
                [10, 11, 13, 0, 'surface'],
                [10, 12, 13, 0, 'surface'],
                [12, 13, 14, 0, 'surface'],
                [13, 14, 15, 0, 'surface'],
                [14, 15, 17, 0, 'surface'],
                [16, 14, 17, 0, 'surface'],
                ]

    def materials(self):
        return [[4e7, None, 0.4, 0.010]]


class Kop1(Dane):
    """"""

    def nodes(self):
        return np.array(
            [[0.0, 22.5, 0.0], [6.590097, 6.590097, 0.0], [22.5, 0.0, 0.0], [38.409903, 6.590097, 0.0],
             [45.0, 22.5, 0.0], [38.409903, 38.409903, 0.0], [22.5, 45.0, 0.0], [6.590097, 38.409903, 0.0],
             [1.7127109999999988, 22.5, 8.610377], [7.8011669999999995, 7.8011669999999995, 8.610377],
             [22.5, 1.7127109999999988, 8.610377], [37.198833, 7.8011669999999995, 8.610377],
             [43.287289, 22.5, 8.610377], [37.198833, 37.198833, 8.610377], [22.5, 43.287289, 8.610377],
             [7.8011669999999995, 37.198833, 8.610377], [6.590097, 22.5, 15.909903], [11.25, 11.25, 15.909903],
             [22.5, 6.590097, 15.909903], [33.75, 11.25, 15.909903], [38.409903, 22.5, 15.909903],
             [33.75, 33.75, 15.909903], [22.5, 38.409903, 15.909903], [11.25, 33.75, 15.909903],
             [13.889623, 22.5, 20.787289], [16.411544, 16.411544, 20.787289], [22.5, 13.889623, 20.787289],
             [28.588456, 16.411544, 20.787289], [31.110377, 22.5, 20.787289], [28.588456, 28.588456, 20.787289],
             [22.5, 31.110377, 20.787289], [16.411544, 28.588456, 20.787289], [22.5, 22.5, 22.5]]
        )

    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    def initial_force(self):
        p = 250
        r = 22.5
        li = []
        for node in self.nodes():
            tmp = vers_norm(node, (22.5, 22.5, 0))
            if node[2] == 0.0:
                sall = 2 * math.pi * r * r
                sup = 2 * math.pi * r * (r - 8.610377)
                sp1 = sall - sup
                f = 0
            elif node[2] == 8.610377:
                w1 = 8.610377 / 2
                w2 = 15.909903 - (15.909903 - 8.610377) / 2
                sall = 2 * math.pi * r * (r - w1)
                sup = 2 * math.pi * r * (r - w2)
                sp1 = sall - sup
                f = sp1 * p / 8
            elif node[2] == 15.909903:
                w1 = 15.909903 - (15.909903 - 8.610377) / 2
                w2 = 20.787289 - (20.787289 - 15.909903) / 2
                sall = 2 * math.pi * r * (r - w1)
                sup = 2 * math.pi * r * (r - w2)
                sp1 = sall - sup
                f = sp1 * p / 8
            elif node[2] == 20.787289:
                w1 = 20.787289 - (20.787289 - 15.909903) / 2
                w2 = r - (r - 20.787289) / 2
                sall = 2 * math.pi * r * (r - w1)
                sup = 2 * math.pi * r * (r - w2)
                sp1 = sall - sup
                f = sp1 * p / 8
            elif node[2] == 22.5:
                w1 = r - (r - 20.787289) / 2
                sall = 2 * math.pi * r * (r - w1)
                sp1 = sall
                f = sp1 * p
            li.append(tmp * f)

        return np.array(li)

    def bond_cond(self, obr=False):
        b = []
        for node in self.nodes():
            if node[2] == 0:
                b.append([1, 1, 1])
            else:
                b.append([0, 0, 0])
        b = np.array(b)

        return b.reshape(int(len(b) * len(b[0])), 1)

    def dof(self):
        return 3

    def elements(self):
        return [[15, 7, 0, 0, 'shield'], [8, 0, 15, 0, 'shield'], [8, 0, 1, 0, 'shield'], [9, 1, 8, 0, 'shield'],
                [9, 1, 2, 0, 'shield'], [10, 2, 9, 0, 'shield'], [10, 2, 3, 0, 'shield'], [11, 3, 10, 0, 'shield'],
                [11, 3, 4, 0, 'shield'], [12, 4, 11, 0, 'shield'], [12, 4, 5, 0, 'shield'], [13, 5, 12, 0, 'shield'],
                [13, 5, 6, 0, 'shield'], [14, 6, 13, 0, 'shield'], [14, 6, 7, 0, 'shield'], [15, 7, 14, 0, 'shield'],
                [23, 15, 8, 0, 'shield'], [16, 8, 23, 0, 'shield'], [16, 8, 9, 0, 'shield'], [17, 9, 16, 0, 'shield'],
                [17, 9, 10, 0, 'shield'], [18, 10, 17, 0, 'shield'], [18, 10, 11, 0, 'shield'],
                [19, 11, 18, 0, 'shield'], [19, 11, 12, 0, 'shield'], [20, 12, 19, 0, 'shield'],
                [20, 12, 13, 0, 'shield'], [21, 13, 20, 0, 'shield'], [21, 13, 14, 0, 'shield'],
                [22, 14, 21, 0, 'shield'], [22, 14, 15, 0, 'shield'], [23, 15, 22, 0, 'shield'],
                [31, 23, 16, 0, 'shield'], [24, 16, 31, 0, 'shield'], [24, 16, 17, 0, 'shield'],
                [25, 17, 24, 0, 'shield'], [25, 17, 18, 0, 'shield'], [26, 18, 25, 0, 'shield'],
                [26, 18, 19, 0, 'shield'], [27, 19, 26, 0, 'shield'], [27, 19, 20, 0, 'shield'],
                [28, 20, 27, 0, 'shield'], [28, 20, 21, 0, 'shield'], [29, 21, 28, 0, 'shield'],
                [29, 21, 22, 0, 'shield'], [30, 22, 29, 0, 'shield'], [30, 22, 23, 0, 'shield'],
                [31, 23, 30, 0, 'shield'],
                [24, 25, 32, 0, 'shield'],
                [25, 26, 32, 0, 'shield'],
                [26, 27, 32, 0, 'shield'],
                [27, 28, 32, 0, 'shield'],
                [28, 29, 32, 0, 'shield'],
                [29, 30, 32, 0, 'shield'],
                [30, 21, 32, 0, 'shield'],
                [31, 24, 32, 0, 'shield'],
                ]

    def materials(self):
        return [[450e6, None, 0.37, 0.01]]


class Kop2(Dane):
    """"""

    def nodes(self):
        li=[]
        nodes=[]
        with open('shell_3D_regular.txt','r') as file:
            for elem in file:
                li.append(elem)
            for el in li[17:74]:
                tmp=el.split(',')
                nodes.append([float(tmp[1]),float(tmp[3]),float(tmp[2])])
        nodes = np.array(nodes)/10*22.5
        return np.array(nodes)
    def initial_disp(self):
        return np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

    # def initial_force(self):
    #     area=DistArea(self.nodes(),22.6)
    #     ar=area.calculate()
    #     f = 250
    #     ar=ar*f
    #     force=[]
    #     for enum,elem in enumerate(self.nodes()):
    #         if elem[2]==0:
    #             force.append((0,0,0))
    #         else:
    #             vrs=np.array(elem)/np.linalg.norm(np.array(elem))
    #             force.append(vrs*ar[enum][0])
    #     return np.array(force)

    def initial_force(self):
        nod = self.nodes()
        area = np.zeros((len(nod),1))
        pola_elementow=[]
        elem=[]
        li=[]
        for ele in self.elements():
            li.append(nod[ele[0]])
            li.append(nod[ele[1]])
            li.append(nod[ele[2]])
            elem.append(li)
            li=[]
        for trian in elem:
            pola_elementow.append(area_trian_set_by_points(*trian))
        srodek_ciezkosci=[]
        for coord in elem:
            srodek_ciezkosci.append([(coord[0][0] + coord[1][0] + coord[2][0]) / 3,
                                     (coord[0][1] + coord[1][1] + coord[2][1]) / 3,
                                     (coord[0][2] + coord[1][2] + coord[2][2]) / 3,
                                     ])
        cosik=[]
        for ncor, cor in enumerate(elem):
            p1=np.array(cor[0])
            p2=np.array(cor[1])
            p3=np.array(cor[2])
            c=np.array(srodek_ciezkosci[ncor])
            k12=np.linalg.norm(p1-p2)
            k13=np.linalg.norm(p1-p3)
            k23=np.linalg.norm(p2-p3)
            v1c=np.linalg.norm(p1-c)
            v2c=np.linalg.norm(p2-c)
            v3c=np.linalg.norm(p3-c)
            # mat1=np.array([[0,k12,k13],
            #                 [k13,k23,0],
            #                 [k12,0,k23]])
            # wyn=np.array([[-v1c],
            # [-v3c],
            # [-v2c]])
            # d=np.linalg.inv(mat1)
            # r=np.matmul(d,wyn)
            # print((v1c+k13*r[2][0]+k12*r[1][0]))

            r1=1/v1c
            r2=1/v2c
            r3=1/v3c
            vrs=np.array([r1,r2,r3])/(r1+r2+r3)
            cosik.append(vrs)
        for nel,el in enumerate(self.elements()):
            for nwez,wez in enumerate(el[0:3]):
                area[wez]+=pola_elementow[nel]*cosik[nel][nwez]


        f = 250*2.5
        ar=area*f
        force=[]
        for enum,elem in enumerate(self.nodes()):
            if elem[2]==0:
                force.append((0,0,0))
            else:
                vrs=np.array(elem)/np.linalg.norm(np.array(elem))
                force.append(vrs*ar[enum][0])
        force=np.array(force)

        #ciezar
        ciezar = 700 * 9.81*1.35

        g=np.zeros_like(force)
        for nrow, row in enumerate(g):
            if self.nodes()[nrow][2]!=0:
                g[nrow][2]=ciezar*area[nrow]*self.materials()[0][3]
        force=force-g

        #wiatr
        fp = 212*1.5
        fs= 313*1.5
        ar=area*f
        force_w=[]
        for enum,elem in enumerate(self.nodes()):
            if elem[2]==0:
                force_w.append((0,0,0))
            elif elem[0]<-14:
                vrs=np.array(elem)/np.linalg.norm(np.array(elem))
                force_w.append((-vrs[0]*area[enum][0]*fp,0,0))
            else:
                vrs = np.array(elem) / np.linalg.norm(np.array(elem))
                force_w.append((vrs[0] * area[enum][0] * fs, 0, 0))
        force=force+np.array(force_w)

        #wiatr


        # ###ploting
        # elem=[]
        # li=[]
        # for ele in self.elements():
        #     li.append(nod[ele[0]])
        #     li.append(nod[ele[1]])
        #     li.append(nod[ele[2]])
        #     elem.append(li)
        #     li=[]
        # import matplotlib.pyplot as plt
        # plt.rcParams["figure.figsize"] = [10, 10]
        # plt.rcParams["figure.autolayout"] = True
        # for enum, elms in enumerate(elem):
        #     p1=elms[0]
        #     p2=elms[1]
        #     p3=elms[2]
        #     x_values=[p1[0],p2[0],p3[0],p1[0]]
        #     y_values=[p1[1],p2[1],p3[1],p1[1]]
        #     plt.plot(x_values, y_values, 'red', linestyle="-")
        # #     xc,yc,z= srodek_ciezkosci[enum]
        # #     plt.text(xc, yc, "{}".format(enum))
        #
        # for nodenum, node in enumerate(self.nodes()):
        #     plt.plot(node[0], node[1], 'bo', linestyle="-")
        #     plt.text(node[0]+0.25, node[1]+0.25, "{}".format(nodenum), fontsize='large',weight=1000)
        # # plt.text(point2[0] - 0.050, point2[1] - 0.25, "Point2")
        # plt.show()
        return force


    def bond_cond(self, obr=False):
        bond=[]
        for elem in self.nodes():
            if elem[2]==0:
                bond.append([1,1,1])
            else:
                bond.append([0,0,0])
        return np.array(bond).reshape(int(len(bond)*3),1)

    def dof(self):
        return 3

    def elements(self):
        li = []
        elements = []
        with open('shell_3D_regular.txt', 'r') as file:
            for elem in file:
                li.append(elem)
            for el in li[75:171]:
                tmp = el.split(',')
                elements.append([int(tmp[1])-1, int(tmp[2])-1, int(tmp[3])-1,0,'shield'])
        return elements

    def materials(self):
        return [[450e6, None, 0.4, 0.01]]

if __name__ == '__main__':
    s=Kop2()
    s.nodes()
    s.elements()
    s.forces()
    s.bond_cond()