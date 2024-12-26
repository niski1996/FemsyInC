import numpy as np

from biblioteki.poly_xy import poly_xy_cls as pol_cls
import itertools


def polfit_xy(points, values, skeleton=None, deriv=dict()):
    """
    xy polynomial fit to data

    Return the  PolyXY obiect of degree similar to skeleton degree,that
     fit to the data. given at points.

    :param points:array_like, shape (`M`,2)
        x-coordinates and y-coordinates of the `M` sample (data) points.
        ``((x[i], y[i]),(x[i+1], y[i+1]),...)``.
    :param values: array_like, shape (`M`,)
        z-coordinates of the sample points
    :param skeleton: poly_xy_cls.PolyXY instance
        defines which monomial will be used to interpolate i.e.
        4 points and skeleton coefficients [(1)'(1,1),(1,0,0)] gives:
        f(x,y) = a + b*x + c*y + d*x^2
        4 points and skeleton coefficients [(1)'(1,0),(1,1,0)] gives:
        f(x,y) = a + b*x + c*x^2 + d*x*y
        where a,b,c,d - free coefficients
        if skeleton is None by default takes mes_obliczenia_1_2.poly_xy.poly_xy_cls.PolyXY.by_order obiekt
    :param deriv: dict, optional
        value of derivatives in point. Keys accept 'dx' and 'dy' as
        determine of derivatives i.ei key 'dydx' mean d^2(f(x,y)/dxdy.
        values determine value of derivative in responding point in 'points'.
        None if derivative is not calculated
        ''{'dy':(None, 1, 2), 'dxdy':(None,4,None)}''

    :return:poly_xy_cls.PolyXY instance


    Raises
    ------
    Warnings
    ------
    See Also
    --------
    mes_obliczenia_1_2.poly_xy.poly_xy_cls.PolyXY
    mes_obliczenia_1_2.poly_xy.poly_xy_cls.PolyXYCreate
    mes_obliczenia_1_2.poly_xy.poly_xy_cls.PolyXYSuperSym
    """
    plen = len(points) #ilość składników podstawowych

    for der in deriv.values():  # czy każda wartość podstawowa ma jakąś pochodną ( moze byc None)
        if len(der) != plen:
            raise ValueError('zła ilość wartości w pochodnych')

    all_der = list(itertools.chain.from_iterable(deriv.values())) #wszystkie pochodne
    count_der = list(filter(lambda x: False if x is None else True, all_der)) #wszystkie pochodne inne od None
    monom_amount = len(points) + len(count_der)  # sumaryczna ilość jednomianów
    if skeleton is None:
        skeleton = pol_cls.PolyXYCreate.by_order(monom_amount)
    else:
        if not isinstance(skeleton, pol_cls.PolyXY):
            raise TypeError('skeleton must be PolyXY')
        if skeleton.monomials != monom_amount:
            raise TypeError("wymiar skeleton nie zgadza się z danymi")

    base_mart = _base_matr(points, skeleton) # macierz punktów podstawowych
    val_vec = np.array(values).reshape([len(values), 1])
    for key, val in deriv.items(): #agregacja macierzy puktów podstawowych, z macierzami pochodnych w punktach
        matr, vec = _deriv_ingr(points, key, val, skeleton)
        base_mart = np.vstack((base_mart, matr))
        val_vec = np.vstack((val_vec, vec))
    idx = np.argwhere(np.all(base_mart[..., :] == 0, axis=0))
    base_mart = np.delete(base_mart, idx, axis=1)  #usuwanie kolumn zerowych, żeby zgadzał się rząd macierzy
    base_coef = np.linalg.solve(base_mart, val_vec).flatten()
    for ind in idx:
        base_coef = np.insert(base_coef, ind, 0)#dodawanie zer w miejsce kolumn zerowych, aby zgadzał się rząd wielomianu
    return pol_cls.PolyXY(collapse_into_poly_like(base_coef))


def _deriv_ingr(poi, key, values, skeleton):
    """

    :param poi::array_like, shape (`M`,2)
        x-coordinates and y-coordinates of the `M` sample (data) points.
        ``((x[i], y[i]),(x[i+1], y[i+1]),...)``.
    :param key: str
         set derivatives order. Keys accept 'dx' and 'dy' as
        determine of derivatives i.ei key 'dydx' mean d^2(f(x,y)/dxdy.
    :param values:array_like, shape (`M`,)
        derivative value in points
    :param skeleton:poly_xy_cls.PolyXY instance
        defines which monomial will be used to interpolate i.e.
        4 points and skeleton coefficients [(1)'(1,1),(1,0,0)] gives:
        f(x,y) = a + b*x + c*y + d*x^2
        4 points and skeleton coefficients [(1)'(1,0),(1,1,0)] gives:
        f(x,y) = a + b*x + c*x^2 + d*x*y
        where a,b,c,d - free coefficients
    :return: tuple
        first value in tuple is matrix, which can be used to extend base_mart from
        polfit_xy.
        IMPORTANT values in matrix DO NOT corespond with poly_xy style of data.
        They're extendet to correspond with base_mart coefficient. Using this data outside,
        can be misleading
        second value in tuple is vactor of deratives value in points
    """
    tmp_len = np.zeros(len(skeleton.flat()))
    ext_skeleton = collapse_into_poly_like(tmp_len)  # szkielet służący do odtworzenia kształtu wielomianu
    # na końcu funkcji żeby współczynniki zgadzały się z podstawowymi
    start = 0
    end = None

    deriv_by = [key[a] + key[a + 1] for a in range(0, len(key), 2)]
    deriv_skeleton = skeleton

    for dr in deriv_by:
        if dr == 'dx':
            dx = True
            start += 1
        elif dr == 'dy':
            if end is None:
                end = 0
            dx = False
            end -= 1
        else:
            raise KeyError('zły klucz przy pochodnych')
        deriv_skeleton =deriv_skeleton.deriv(dx=dx)
    der_poi = []
    val_vect = []
    for num, val in enumerate(values):
        if val is not None:  #wybiera tylko te wartosci, których pochodne są znane w punktach
            der_poi.append(poi[num])
            val_vect.append(val)
    for mnum, mpoi in enumerate(der_poi): # wkleja wartości pochodnych do szkieletu, zeby współczynniki były
        # na odpowiednich miejcach. w tym miejscu trace zbiezność z wielomianowym stylem zapisu
        tmp = [np.copy(a) for a in ext_skeleton]
        if deriv_skeleton.point_val(mpoi[0],mpoi[1]) != 0:
            tmp_der_val = deriv_skeleton.create_own_instance(deriv_skeleton.components(mpoi))
            tmp_der_val_ext = collapse_into_poly_like(tmp_der_val.flat())
            for num, elem in enumerate(tmp_der_val_ext):
                tmp[num + start + abs(int(bool(end)))][start:end] = elem
        der_poi[mnum] = tmp
    der_matr = np.array([list(itertools.chain.from_iterable(a)) for a in der_poi]) #rozpakowuje do macierzowej formy
    return der_matr, np.array(val_vect).reshape(len(val_vect),1)


def _base_matr(points, skeleton):
    """
    marix of skeleton values


    :param points:
    :param skeleton:
    :return:
    """
    li = []
    lz=np.zeros(len(skeleton.flat()))
    for poi in points:
        tmp=(skeleton.components(poi))
        pol_tmp = skeleton.create_own_instance(tmp) #dostarczam danych o zerowych tablicach pomijanych przy components()
        tmp=np.copy(lz)
        tmp[:len(pol_tmp.flat())]=pol_tmp.flat()#poszerza instancje jak sa same zera na koncu, czyli punkt (0,0,f(x,y))
        li.append(tmp)
    return np.array(li)


def collapse_into_poly_like(arr):
    """
    transform elem1d array into poly_xy_like shape
    :param arr:
    :return:
    """
    last = 1
    step = 2
    li = [np.array([arr[0]])]
    while last < len(arr):
        frst = last
        last = frst + step
        step += 1
        li.append(arr[frst:last])
    if last != len(arr):
        raise ValueError('zły rozmiar listy')
    return li


