import numpy as np
import pytest
import biblioteki.poly_xy.poly_xy_cls as polyxy


class TwoPolyData10:
    def __init__(self, clss):
        self.me = clss([2, (4, 1)])
        self.other = clss([7])
        self.point1 = (0, 0)
        self.point2 = (-2, 5)
        self.clss = clss

    def result_add(self):
        return self.clss(([9, (4, 1)]))

    def result_sub(self):
        return self.clss(([(-5), (4, 1)]))

    def result_mul(self):
        return self.clss(([14, (28, 7)]))

    @staticmethod
    def result_elem_len():
        return {0: 1, 1: 2}

    @staticmethod
    def result_degree():
        return 1

    @staticmethod
    def result_monomials():
        return 3

    @staticmethod
    def result_rev():
        return [np.array([2]), np.array([1, 4])]

    @staticmethod
    def result_flat():
        return np.array([2, 4, 1])

    @staticmethod
    def result_components1():
        return [np.array([2]), np.array([0, 0])]

    @staticmethod
    def result_components2():
        return [np.array([2]), np.array([-8, 5])]

    @staticmethod
    def result_val1():
        return 2

    @staticmethod
    def result_val2():
        return -1

    @staticmethod
    def result_der_dx():
        return [np.array([4]), ]

    @staticmethod
    def result_der_dy():
        return polyxy.PolyXY([np.array([1]), ])


class TwoPolyData11(TwoPolyData10):
    def __init__(self, clss):
        super().__init__(clss)
        self.me = clss([2, (4, 1), (0, 0, 0)])
        self.other = clss([7, (0,0)])


class TwoPolyData12(TwoPolyData10):
    def __init__(self, clss):
        super().__init__(clss)
        self.me = clss([2, (0, 0, 0), (4, 1)])


class TwoPolyData20:
    def __init__(self, clss):
        self.me = clss([2, (0, 1), (3, 3, 5)])
        self.other = clss([7, (9, 8)])
        self.point1 = (0, 1)
        self.point2 = (-1, 2)
        self.clss = clss

    def result_add(self):
        return self.clss(([9, (9, 9), (3, 3, 5)]))

    def result_sub(self):
        return self.clss(([(-5), (-9, -7), (3, 3, 5)]))

    def result_mul(self):
        return self.clss(([14, (18, 23), (21, 30, 43), (27, 51, 69, 40)]))

    @staticmethod
    def result_elem_len():
        return {0: 1, 1: 1, 2: 3}

    @staticmethod
    def result_degree():
        return 2

    @staticmethod
    def result_monomials():
        return 5

    @staticmethod
    def result_rev():
        return [np.array([2]), np.array([1, 0]), np.array([5, 3, 3])]

    @staticmethod
    def result_flat():
        return np.array([2, 0, 1, 3, 3, 5])

    @staticmethod
    def result_components1():
        return [np.array([2]), np.array([0, 1]), np.array([0, 0, 5])]

    @staticmethod
    def result_components2():
        return [np.array([2]), np.array([0, 2]), np.array([3, -6, 20])]

    @staticmethod
    def result_val1():
        return 8

    @staticmethod
    def result_val2():
        return 21

    @staticmethod
    def result_der_dx():
        return [np.array([0]), np.array([6, 3])]

    @staticmethod
    def result_der_dy():
        return polyxy.PolyXY([np.array([1]), np.array([3, 10])])


class TwoPolyData30:
    def __init__(self, clss):
        self.me = clss([1, (0, 0), (0, 0, 0), (1, 0, 0, 0)])
        self.other = clss(
            [0, (0, 0), (0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1)])
        self.point1 = (0, 1)
        self.point2 = (-2, 2)
        self.clss = clss

    def result_add(self):
        return self.clss([1, (1, 0, 0, 0), (1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1)])

    def result_sub(self):
        return self.clss([1, (1, 0, 0, 0), (-1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, -1)])

    def result_mul(self):
        return self.clss(
            ([(1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1), (1, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0, 0)]))

    @staticmethod
    def result_elem_len():
        return {0: 1, 3: 1}

    @staticmethod
    def result_degree():
        return 3

    @staticmethod
    def result_monomials():
        return 2

    @staticmethod
    def result_rev():
        return [np.array([1]), np.array([0, 0, 0, 1])]

    @staticmethod
    def result_flat():
        return np.array([1, 0, 0, 0, 0, 0, 1, 0, 0, 0])

    @staticmethod
    def result_components1():
        return [np.array([1]), np.array([0, 0, 0, 0])]

    @staticmethod
    def result_components2():
        return [np.array([1]), np.array([-8, 0, 0, 0])]

    @staticmethod
    def result_val1():
        return 1

    @staticmethod
    def result_val2():
        return -7

    @staticmethod
    def result_der_dx():
        return [np.array([3, 0, 0])]

    @staticmethod
    def result_der_dy():
        return polyxy.PolyXY([np.array([0, 0, 0])])


class TwoPolyData31(TwoPolyData30):
    def __init__(self, clss):
        super().__init__(clss)
        self.me = clss([1, (1, 0, 0, 0)])


@pytest.fixture(params=[lambda: TwoPolyData10(polyxy.PolyXY),
                        lambda: TwoPolyData11(polyxy.PolyXY),
                        lambda: TwoPolyData12(polyxy.PolyXY),
                        lambda: TwoPolyData20(polyxy.PolyXY),
                        lambda: TwoPolyData30(polyxy.PolyXY),
                        lambda: TwoPolyData31(polyxy.PolyXY)])
# lambda tworzy taki mały closure, wiec za każdym razem jest wywołania i stan wielomianu się zeruje
def myset(request):
    return request.param()

