import math

import numpy as np

import biblioteki.poly_xy.poly_fuu.poly_xy_fit as fit
import biblioteki.poly_xy.poly_fuu.xyfake_roots as xyroot
from biblioteki.arrays.filter import circle_meshgrid
from programy.Visualizer.visualizer import Visual
import json


class Aproks:
    """
    Class to create and check accuracy of polynomial approksimation

    ONLY TO DOMES

    Creates Poly_XY object( f(x,y)), which aproximates `num_poi` points.
    Points are chosen by max value of x,y,z; min value of x and y, and they are
    coplement by random of left points. After that check is executed in two forms:
    -if roots in derivatives are singular in area and located in 20% wide range from region
    -if Root-mean-square deviation is smaler than 10%
    else draw points is executed again
    If condition are fill, show plot of poly, and derivatives
    If doesn't find aproksymation in 100 steps save points in json file and report error

    Parameters
    ----------
    :param bord_poi: array_like (n,3)
        array of points coordinates, contain points which coordinates ar given in data
    :param free_poi: array_like (m,3)
        array of points coordinates, contain points which coordinates ar count by program
    :param num_poi: int
        numbers of points taken to aproximation. 5 <`num_poi`< n+m

    Raises
    ------
    ValueError
        When one f(x,y) value correspond with two z values
    """

    def __init__(self, bord_poi, free_poi, num_poi, debugmode=False):

        self.bord_poi = bord_poi
        self.free = free_poi
        self.debug = debugmode

        self.iternum=0
        self.allpoi = [a for a in bord_poi]
        self.allpoi.extend([a for a in free_poi])
        self.allx = np.array([a[0] for a in self.allpoi]).reshape(len(self.allpoi), 1)
        self.ally = np.array([a[1] for a in self.allpoi]).reshape(len(self.allpoi), 1)
        self.allz = np.array([a[2] for a in self.allpoi]).reshape(len(self.allpoi), 1)


        bordx = [a[0] for a in bord_poi]
        bordy = [a[1] for a in bord_poi]
        # ustale pojedyncze wartości, nie punkty
        self.minx = float(min(bordx))
        self.maxx = float(max(bordx))
        self.miny = float(min(bordy))
        self.maxy = float(max(bordy))

        self.rx = (self.maxx - self.minx) // 2
        self.ry = (self.maxy - self.miny) // 2

        bord_poi = list(bord_poi)
        self.appr_poi = []#punkty używane do aproksymacji
        self.add_border(bord_poi)
        self.check_double_points(free_poi)  # sprawdza punkty podwójne i dodaje cztery graniczne punkty
        free_poi = list(free_poi)
        free_poi.extend(bord_poi)
        free_poi.sort(key=lambda x: x[2])
        self.czubek = free_poi[-1]
        self.appr_poi.append(free_poi.pop(-1))  # dodaje czubek

        self.pol = None
        self.set_poly(free_poi[:], num_poi)
        self.numeric_check(free_poi[:], num_poi)


    def set_poly(self, free_poi, num_poi):
        """
        add `num_poi` random points from `free_poi` to self.appr_poi, and creates approximating polynomial
        :param free_poi: array_like (n,3)
            list of points yet not included in self.appr_poi
        :param num_poi: int
            numbers of points taken to aproximation.
        :return: PolyXY object
        """
        add_idx = list(range(len(free_poi)))
        add_poi = np.random.choice(add_idx, size=num_poi - len(self.appr_poi), replace=False)
        appr_poi = self.appr_poi[:]
        appr_poi.extend([free_poi[inx] for inx in add_poi])
        xy = [(a[0], a[1]) for a in appr_poi]
        z = [a[2] for a in appr_poi]
        self.pol = fit.polfit_xy(xy, z)

        return self.pol

    def numeric_check(self, free_poi, num_poi):
        """
        check percentage difference and roots of derivatives and repeat draw points,
        until polynomial fulfill conditions

        """

        def zeros_in_range(pol, start, stop):
            """
            delete all roots that contain img part or are beoynde scope
            :param pol:
            :param start:
            :param stop:
            :return:
            """
            li = xyroot.xyfake_poly_xy_roots(pol, (start, stop), 100)
            # wybiera miejsca zerowe w zakresie
            li = list(filter(lambda a: False if a[0] > stop or a[0] < start else True, li))
            # usuwa urojone
            li = list(filter(lambda a: False if a[0].imag != 0 else True, li))
            return li

        def check_wide(rr):
            """
            check distance of roots from center line of scope
            :param rr:
            :return:
            """
            for root in rr:
                if abs(root[0] - self.rx) / self.rx > 0.2:
                    return False
            return True

        def check_rmse():
            newz = self.pol(self.allx, self.ally)
            tmp = self.allz - newz
            rmse = math.sqrt(np.sum(tmp ** 2) / len(tmp))  # Root-mean-square deviation
            if rmse > 10:
                if self.debug:
                    print("punkty rozbieżne od wilomianu. Wartość RMSE:",np.sum(rmse) )
                return False
            return True


        n=False
        bol_dx=False

        while n==False:
            xiter=0
            if self.debug:
                print("iteracja: ", self.iternum)
                self.iternum+=1
                if self.iternum==100:
                    return self.iter_error()

            while bol_dx == False:
                xiter+=1
                self.set_poly(free_poi, num_poi)
                dx = self.pol.deriv()
                xroot = zeros_in_range(dx, self.miny, self.maxy)
                bol_dx = check_wide(xroot)
            if self.debug:
                print("wykonano {} iteracji dx".format(xiter))
                print("zgodność dx")
            dy = self.pol.deriv(dx=False).rev()
            yroot = zeros_in_range(dy, self.minx, self.maxx)
            if check_wide(yroot):
                if self.debug:
                    print("zgodność dy")
                if check_rmse():
                    n=True
            bol_dx=False

        print('znaleziono wielomian aproksymujący\n\n\n\n')
        self.show(self.pol)
        # self.show(self.pol.deriv())
        # self.show(self.pol.deriv(dx=False))

    def show(self, poly, gif=False):
        """
        visualize `poly` surface on the circle meshgrid

        :return: None
        """

        dens = 100
        x = np.linspace(self.minx, self.maxx, dens)
        y = np.linspace(self.miny, self.maxy, dens)
        xx, yy = np.meshgrid(x, y)
        circle_meshgrid(max(self.rx, self.ry), (self.minx + self.rx, self.miny + self.ry), xx, yy)
        Visual(('poly', poly,
                {'xrange': (self.minx, self.maxx), 'yrange': (self.miny, self.maxy), 'zrange': (0, 200), 'setx': xx,
                 'sety': yy}), gif=gif)

    def add_border(self, bord_poi):
        """
        add border points
        :param bord_poi:
        :return:
        """
        try:
            bord_poi.sort(key=lambda x: x[0])
            self.appr_poi.append(bord_poi.pop(-1))
            self.appr_poi.append(bord_poi.pop(0))
            bord_poi.sort(key=lambda x: x[1])
            self.appr_poi.append(bord_poi.pop(-1))
            self.appr_poi.append(bord_poi.pop(0))
        except IndexError('prawdopodobnie mniej niz 4 punkty graniczne'):
            pass

    def check_double_points(self, free_poi):
        """
        check if in range set by `bord_poi`, all of `free_poi` have a smaller coord vallues.


        :param bord_poi:
        :param free_poi:
        :return:
        """
        for poi in free_poi:
            if poi[0] > self.maxx or poi[0] < self.miny:
                raise ValueError("punkty podwójne, nie mozna dopasowac wielomianu. Prawdopodobnie `rozdeło` i jednej"
                                 "wartosci x odpowiadaja dwie wartosci y")

        for poi in free_poi:
            if poi[1] > self.maxy or poi[0] < self.miny:
                raise ValueError("punkty podwójne, nie mozna dopasowac wielomianu. Prawdopodobnie `rozdeło` i jednej"
                                 "wartosci x odpowiadaja dwie wartosci y")

    def iter_error(self):
        print("osiągnięto limit rekurencji ustawiony przez użytkownika. Problematyczne dane zapisano w pliku")
        with open("error_aray.json","w") as fill:
            brd = list(map(lambda x:list(x),self.bord_poi))
            free = list(map(lambda x:list(x),self.free))
            json.dump({"bord_poi":brd, "free_poi":free},fill, indent=1)
        raise RecursionError


if __name__ == '__main__':
    from data import arr_of_const as arr11
    from data import array_of_calculeted as arr
    Aproks(arr11(), arr(), 15)
