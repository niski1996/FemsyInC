"""
=================================================
Two Variables Power Series
=================================================

This module provides a number of objects useful for
dealing with two variable polynomials including  'Poly_XY' class
that encapsulate a few  usual arithmetic operations
"""
import itertools

import numpy as np
from abc import ABC
import numbers

import biblioteki.matr_pom.macierze_num as mtnum


class PolyXYCreate(ABC):  # todo testy, bo się pogubie
    """
    Group methods to create and operate on two variable polynomial
    """

    @staticmethod
    def by_level(level):
        li = []
        for num in range(level):
            li.append(np.ones(num + 1))
        return PolyXY(li)

    @staticmethod
    def by_amount_sym_last_level(num):
        """
        Create symmetric xy polynomial with num or num+1 ingredients

        for every level of polynimian, where summary of the ingredients
        lower than num gives monomial with coeficient = 1. For rest takes
        last level which cannot be taken all, and take ingridients
        as close as possible to axis of symmetry.
        (*) If, due to asymmetry, it's impossible took n+1 paraametres,
        where on the last level,  there are two with coefficients 0.5.
        One of poly ingrideints  then should be understend as average
        of two with coeff 0.5. i.e. for num=2 poly coefficients = [(1),(0.5,0.5)]
        meaning f(x,y) = 1 + 1*(0.5x^1*y^0 + 0.5*x^0*y^1)

        :param num:
        :return:


        WARNING
        these type of data is cerated epecially to polynomial interpolation used in MES.
        Using this poly in other type of calculation can be misleadnig and causin
        unexpected and hard to debug misteake

        """

        """
        
        Stara dokumentacja
        
        zwraca modyfikowany trójkąt pascala dla obliczeń numerycznych

        dla określonej liczby jednomianów określa stopień  potęgi x i y w poszczególnych jednomianach
        wykorzystywany przy obliczeniach aproksymacyjnych płąszczyzn

        :param num: int
            ilość współczynników
        :return: array
            lista tablic współczynników

        Uwagi
        --------
        dla każdego wyrazu oprócz pierwszego, wyraz oznacza tylko współczynnki jednoimienne.
        w celu uzyskania pełnego wyrazu tego stopnia należy odwrócić wyraz i pomnożyć z poprzednim.
        Przykład - jeden z wyrazów to [1,1,0]. sumaryczny stopień to len(li)-1=2.
        Jawnie należy rozumieć go jako [x^2, x, 0]. w celu otrzymania pełnego wyrazu odwracamy go zastępująz x przez y
        i mnożymy:
        [x^2, x^1, x^0]
        [y^0, y^1, y^2] --> najprostsze mnożenie góra z dołem daje  x^2 + x*y + y^2

        Jeżeli występują wskaźniki 0.5 znaczy że jeden wyraz jest średnią tych dwóch składników
        """
        pasc = [[1], [1, 1]]
        while num > len(list(itertools.chain.from_iterable(pasc))):
            pasc.append(pasc[-1][:])
            pasc[-1].append(1)
        left = num - len(list(itertools.chain.from_iterable(pasc[:-1])))
        if left % 2 == len(pasc[-1]) % 2:
            border = left
        else:
            border = left + 1
        while pasc[-1].count(1) > border:
            pasc[-1].reverse()
            zerowana = pasc[-1].index(1)
            pasc[-1][zerowana] = 0
        if left % 2 == len(pasc[-1]) % 2:
            return PolyXYSuperSym(pasc)
        elif len(pasc[-1]) % 2 == 1:
            pasc[-1][len(pasc[-1]) // 2] = 0
            return PolyXYSuperSym(pasc)
        else:
            pasc[-1][len(pasc[-1]) // 2] = 0.5
            pasc[-1][len(pasc[-1]) // 2 - 1] = 0.5
            return PolyXYSuperSym(pasc)


    @staticmethod
    def by_amount_sym_last_level2_(num):
        """
        Create symmetric xy polynomial with num or num+1 ingredients

        for every level of polynimian, where summary of the ingredients
        lower than num gives monomial with coeficient = 1. For rest takes
        last level which cannot be taken all, and take ingridients
        as close as possible to axis of symmetry.
        (*) If, due to asymmetry, it's impossible took n+1 paraametres,
        where on the last level,  there are two with coefficients 0.5.
        One of poly ingrideints  then should be understend as average
        of two with coeff 0.5. i.e. for num=2 poly coefficients = [(1),(0.5,0.5)]
        meaning f(x,y) = 1 + 1*(0.5x^1*y^0 + 0.5*x^0*y^1)

        :param num:
        :return:


        WARNING
        these type of data is cerated epecially to polynomial interpolation used in MES.
        Using this poly in other type of calculation can be misleadnig and causin
        unexpected and hard to debug misteake

        """

        """
        
        Stara dokumentacja
        
        zwraca modyfikowany trójkąt pascala dla obliczeń numerycznych

        dla określonej liczby jednomianów określa stopień  potęgi x i y w poszczególnych jednomianach
        wykorzystywany przy obliczeniach aproksymacyjnych płąszczyzn

        :param num: int
            ilość współczynników
        :return: array
            lista tablic współczynników

        Uwagi
        --------
        dla każdego wyrazu oprócz pierwszego, wyraz oznacza tylko współczynnki jednoimienne.
        w celu uzyskania pełnego wyrazu tego stopnia należy odwrócić wyraz i pomnożyć z poprzednim.
        Przykład - jeden z wyrazów to [1,1,0]. sumaryczny stopień to len(li)-1=2.
        Jawnie należy rozumieć go jako [x^2, x, 0]. w celu otrzymania pełnego wyrazu odwracamy go zastępująz x przez y
        i mnożymy:
        [x^2, x^1, x^0]
        [y^0, y^1, y^2] --> najprostsze mnożenie góra z dołem daje  x^2 + x*y + y^2

        Jeżeli występują wskaźniki 0.5 znaczy że jeden wyraz jest średnią tych dwóch składników
        """
        pasc = [[1], [1, 1]]
        #tworzy pełne piętra
        while num > len(list(itertools.chain.from_iterable(pasc))):
            pasc.append(pasc[-1][:])
            pasc[-1].append(1)
        left = num - len(list(itertools.chain.from_iterable(pasc[:-1]))) #pozostała ilość jedynek
        if left % 2 == len(pasc[-1]) % 2:#zapobiega nieymetrycznym rozkladom
            border = left
        else:
            border = left - 1
        while pasc[-1].count(1) > border:
            pasc[-1].reverse()
            zerowana = pasc[-1].index(1)
            pasc[-1][zerowana] = 0
        left=left-pasc[-1].count(1)#ile zostało niewykorzystanych jedynek
        if left==0:
            return PolyXYSuperSym(pasc)
        elif len(pasc[-1]) % 2 == 1:
            pasc[-1][len(pasc[-1]) // 2] = 0#zeruje srodkowy
            if pasc[-1][(len(pasc[-1]) // 2)-1]==0:  #jeżeli same zera w liscie
                jedynkowana=(len(pasc[-1]) // 2)-1
            else:
                jedynkowana = pasc[-1].index(1)
            pasc[-1][jedynkowana-1] = 1# za środkowy
            pasc[-1].reverse()
            pasc[-1][jedynkowana-1] = 1  # za left
            return PolyXYSuperSym(pasc)
        else:
            pasc.append([0 for n in range(len(pasc[-1]))])
            pasc[-1].append(0)
            pasc[-1][len(pasc[-1])//2]=1
            return PolyXYSuperSym(pasc)

    @staticmethod
    def by_order(num, by_x=True):

        """create xy polynomial by taking n next ingridients by x or by y

        :param num:
        :param by_x:
        :return: """
        li = []
        n = 1
        while True:
            li.append(np.ones(n))
            num -= n
            if num < n + 2:
                on = np.ones(num)
                zr = np.zeros(n + 1 - num)
                if by_x:
                    li.append(np.hstack((on, zr)))
                else:
                    li.append(np.hstack((zr, on)))
                break
            n += 1
        return PolyXY(li)

    @staticmethod
    def poly_to_numpy_shape(pol):
        """
        Turn PolyXY style of data to numpy style


        :param pol:array_like
            Series of array_like with coefficients of f(x,y) polynomial
            len(coef_arr[n]) degree i.e. [(2),(2,3),(9,8,7)] gives:
            '2*P_0(x)*P_0(y)' + '2*P_1(x)*P_0(y) + 3*P_0(x)*P_1(y)' +
            '9*P_2(x)*P_0(y) + 8*P_1(x)*P_1(y) + 7*P_0(x)*P_2(y)' , where
            ``P_i`` is the basis polynomials of degree ``i``.
        :return:array_like
        Array of coefficients ordered so that the coefficient of the term
        of multi-degree i,j is contained in `c[i,j]`.

        Examples
    --------
    >> poly_to_numpy_shape([1,(2,3),(4,5,6)])  # 1+2x+3y+4x^2+5xy+6y^2
    np.array([[1,2,4],
              [3,5,0],
              [6,0,0]])
        """
        mat_pol = np.zeros([(len(pol[-1])), (len(pol[-1]))])
        for flor in pol:
            xpos = 0  # moze byc ze xpos oznacze pozycje y, bo zmienialem na pale, na szybko
            ypos = len(flor) - 1
            for ing in range(ypos + 1):
                mat_pol[xpos][ypos] = flor[ypos]
                ypos -= 1
                xpos += 1
        mat_pol = mtnum.del_last_with_val(mat_pol)
        mat_pol = mtnum.del_last_with_val(mat_pol, ax=1)
        return mat_pol


class PolyXY:
    """
    A two variables power series class

    The Poly_XY class provides standard Python numerical methods
    '+', '-', '*',

    :param coef_arr: array_like
        Series of array_like with coefficients of f(x,y) polynomial
        len(coef_arr[n]) degree i.e. [(2),(2,3),(9,8,7)] gives:
        '2*P_0(x)*P_0(y)' + '2*P_1(x)*P_0(y) + 3*P_0(x)*P_1(y)' +
        '9*P_2(x)*P_0(y) + 8*P_1(x)*P_1(y) + 7*P_0(x)*P_2(y)' , where
        ``P_i`` is the basis polynomials of degree ``i``.

    """

    def __init__(self, coef_arr):
        self.__value = self.entry_validate(list(coef_arr))
        self.iternum = None

    def entry_validate(self, coef_arr):
        """
        Check array shape and type. If diffrent change to ndarray

        :param coef_arr: array_like
            array containing elem1d vectos of coefficients

        :return: list of elem1d ndarray
            list of coefficient copleated to requested dimension by vectors containing zeros
        """
        for num, el in enumerate(coef_arr):  # unikanie problemów z powodu różnicy między (int), a (int,)
            if isinstance(el, numbers.Number):
                coef_arr[num] = (el,)
        self.value = []
        len_li = []  # czy tablice konkretnych stopni sie nie powtarzają
        for row in coef_arr:
            len_li.append(len(row))
            if type(row) != np.ndarray:
                row = np.array(row, dtype='float64')
            if len(row.shape) == 1:
                self.value.append(row)
            else:
                raise ValueError('Tablica ma wiecej niż jeden wymiar')
        if len(len_li) != len(set(len_li)):
            raise ValueError("dwa zestawy współczynnikow mają ten sam stopien")
        tmp = self.flat()
        for val in tmp:
            if not isinstance(val, numbers.Number):
                raise TypeError("jakieś dziwne współczynniki")
        # if not any(tmp):
        #     raise Warning("wielomian zerowy")

        return self.__compress()

    def __eq__(self, other):
        if list(other.flat()) == list(self.flat()):
            return True
        else:
            return False


    def __add__(self, other):
        if isinstance(other, numbers.Number):
            other = self.create_own_instance([other])
        a = self.create_own_instance(self.copy_val())
        for elem in other:
            try:
                ind = [len(i) for i in a.value].index(len(elem))
                a.value[ind] += np.array(elem)
            except ValueError:
                a.value.append(np.array(elem))
        a.__compress()
        return a

    def __sub__(self, other):
        for row in other:
            for num, val in enumerate(row):
                row[num] = -1 * val
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            other = self.create_own_instance([other])
        a = self.create_own_instance(self.copy_val())
        ing_list = []
        for ingr1 in a.value:
            for ingr2 in other:
                ing_list.append(a.mul_two_single_poly(ingr1, ingr2))
        ing_list.sort(key=len)
        a.value = []
        tmp = itertools.groupby(ing_list, key=len)
        tmp = [list(elem[1]) for elem in tmp]
        for elem in tmp:
            pol_sum = np.zeros(len(elem[0]))
            for poly_set in elem:
                pol_sum += poly_set
            a.value.append(pol_sum)
        self.__compress()
        return a

    def __str__(self):
        str_out = ''
        for row in self.value:
            mymin = 0
            mymax = len(row) - 1
            for elem in row:
                if elem != 0:
                    str_out += str(elem)
                    if mymax == 0:
                        pass
                    elif mymax == 1:
                        str_out += 'x'
                    else:
                        str_out += '(x^{})'.format(mymax)
                    if mymin == 0:
                        pass
                    elif mymin == 1:
                        str_out += 'y'
                    else:
                        str_out += '(y^{})'.format(mymin)
                    str_out += " + "
                mymin += 1
                mymax -= 1

        return str_out[:-2]

    def __call__(self, *args, **kwargs):
        return self.point_val(*args)

    def __iter__(self):
        self.iternum = len(self.value)
        return self

    def __next__(self):
        if self.iternum > 0:
            self.iternum -= 1
            return self.value[len(self.value) - self.iternum - 1]
        else:
            raise StopIteration

    def copy_val(self):
        return [a.copy() for a in self.value]

    @classmethod
    def create_own_instance(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    @property
    def elem_len(self):
        """

        :return: dict
            key is polynomial degree, value is amount of polynomials
        Warnings
        ------
        may retrurn diffrent value depend on self.long value


        """
        dii = {}
        for elem in self.value:
            dii[len(elem) - 1] = np.count_nonzero(elem)
        return dii

    @property
    def monomials(self):
        """

        :return: int
            amount of monomials
        """

        return np.count_nonzero(self.flat())
    @property
    def coef(self):
        return self.flat()

    def rev(self):

        return self.create_own_instance([np.flip(a) for a in self.value])

    def degree(self):
        """

        :return: int
        degree of polynomial
        """
        return len(self.value[-1]) - 1

    def flat(self):
        self.value.sort(key=len)
        li = []
        icount_iter = itertools.count(1)
        for num, elem in enumerate(self.value):
            icount_it = next(icount_iter)
            if len(elem) == icount_it:
                li.append(elem)
            else:
                while len(elem) > icount_it:
                    li.append(np.zeros(icount_it))
                    icount_it = next(icount_iter)
                li.append(elem)
        return np.array(list(itertools.chain.from_iterable(li)))

    def __cut_zeros(self, ):
        """

        :return:
        """
        pass

    def __compress(self):
        """

        :return:
        """
        del_arr = []
        for num, elem in enumerate(self.value):
            if not any(elem):
                del_arr.append(num)

        for el_num in sorted(del_arr, reverse=True):
            self.value.pop(el_num)
        self.value.sort(key=len)
        return self.value

    @staticmethod
    def mul_two_single_poly(arr1, arr2):
        sum_li = []
        for num, val in enumerate(np.flip(arr2)):
            tmp = arr1[:]
            for mnum in range(num):
                tmp = np.append(tmp, 0)
            sum_li.append(tmp * val)
        target_len = len(max(sum_li, key=len))
        for num, arr in enumerate(sum_li):
            while len(arr) < target_len:
                arr = np.insert(arr, 0, 0)
            sum_li[num] = arr

        return np.sum(sum_li, axis=0)

    def components(self, point):
        """
        value of polynomial component in points
        :param point: array_like shape()=2
            params x and y

        :return: array_like
        array of components polynomial in point.
        shape of array is identical as self.value
        """

        def jednomiany_wielomianu(val, factors):
            """
            zwraca wartość jednomianów wielominu dla zadanej wartości

            :param val:
            :param factors:
            :return:
            """
            factors=factors.astype('float64')#czasem sie dane nie mieszcza
            for num, fac in enumerate(factors):
                factors[num] = factors[num] * val ** (len(factors) - num - 1)
            return factors

        lv = []
        for level in self.value:
            lev = level.copy().astype('longdouble')
            x = jednomiany_wielomianu(float(point[0]), lev) #TODO tu czasem pojawia sie blad przepełnienia, float to poprawia
            y = jednomiany_wielomianu(float(point[1]), np.ones(len(lev)))
            lv.append(x * np.flip(y))
        return lv

    def point_val(self, x, y):
        """
        use np.polynomial.polynomial.polyval2d to calculete value

        :param x, y: array_like, compatible objects
            The two dimensional series is evaluated at the points `(x, y)`,
            where `x` and `y` must have the same shape. If `x` or `y` is a list
            or tuple, it is first converted to an ndarray, otherwise it is left
            unchanged and, if it isn't an ndarray, it is treated as a scalar.
        :return: ndarray, compatible object
            The values of the two dimensional polynomial at points formed with
            pairs of corresponding values from `x` and `y`.
        """
        poly = PolyXYCreate.poly_to_numpy_shape(self.copy_val())
        return np.polynomial.polynomial.polyval2d(x, y, poly)

    def deriv(self, dx=True):
        if dx:
            iterval = self.value
        else:
            iterval = self.rev()
        li_der = []
        for elem in iterval:
            elem = np.delete(elem, -1)
            for num, val in enumerate(np.flip(elem)):
                elem[-num - 1] = val * (num + 1)
            if len(elem) != 0:
                li_der.append(elem)
        if not dx:
            return self.create_own_instance([np.flip(a) for a in li_der])
        return self.create_own_instance(li_der)


class PolyXYSuperSym(PolyXY):
    """Special class for dangerous monomial which have n ingridients,
    but can use n+1 coefficients"""

    def __compleat(self):  # todo niech zwraca kopie
        """
                Fill gap in poly by vectors containing zeros

                take max vector in self.value, and check if all levels exist.
                If not add vector filled by zeros. Overrite self.value

                :return: self.value
                    polynomial coefficient
                """
        tmp = [len(i) for i in self.value]
        if len(tmp) == 1:
            r_num = tmp[0]
        else:
            r_num = max(*tmp)
        for num in range(1, r_num):
            if num not in tmp:
                self.value.append(np.zeros(num))
        self.value.sort(key=len)
        return self.value
