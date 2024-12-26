import numpy as np

from biblioteki.poly_xy.poly_fuu import grad


def lin_base(vec):
    """nowa baza współliniowa z vec

    tworzy bazę, w której vec wyznacza wersor x.
    Jeśli to możliwe, osie z się pokrywają

    Params
    -------
    vec : array_like, shape (3,)
        wektor dowolny

    Return
    numpy.ndarray
        wektory nowego ukłądu w staryn, czyli właściwie
        macierz cosinusów kierunkowych"""
    versor_x = vec / np.linalg.norm(vec)
    versor_temp_y = versor_x / 1  # dzięki temu kopiuje wektor
    if (versor_temp_y[0] == 0) and (versor_temp_y[2] == 0):
        versor_temp_y[0] += 1  # generowanie plaszczyzny xy
    else:
        versor_temp_y[1] += 1  # generowanie plaszczyzny xy
    versor_temp_z = np.cross(versor_x, versor_temp_y)
    versor_z = versor_temp_z / np.linalg.norm(versor_temp_z)
    versor_y = np.cross(versor_z, versor_x)
    return np.array([versor_x, versor_y, versor_z])


def lin_base_2vec(vec1, vec2):
    """nowa baza współliniowa z vec1 i vec2

    tworzy bazę, w której vec1 wyznacza wersor x,
    a vec2 wersor y

    Params
    -------
    vec : array_like, shape (3,)
        wektor dowolny

    Return
    numpy.ndarray
        wektory nowego ukłądu w staryn, czyli właściwie
        macierz cosinusów kierunkowych"""
    versor_x = vec1 / np.linalg.norm(vec1)
    versor_temp_y = vec2 / np.linalg.norm(vec2)
    try:
        if np.testing.assert_array_equal(versor_x, versor_temp_y):  # TODO brzydkie
            raise ValueError('węzły są współliniowe')
    except AssertionError:
        pass
    versor_temp_z = np.cross(versor_x, versor_temp_y)
    versor_z = versor_temp_z / np.linalg.norm(versor_temp_z)
    versor_y = np.cross(versor_z, versor_x)
    return np.array([versor_x, versor_y, versor_z])


def norm_vers(poly, point):
    """
    Return vector normal to surface set by `poly` in point. Turn is set by right
    hand regule of any lines on surface in `point`
    :param poly:
    :param point:
    :return:
    """
    grd = grad.poly_grad(poly)
    vec = np.array([grd[0](point[0], point[1] ),
                       grd[1](point[0], point[1] ),
                       grd[2](point[0], point[1])])
    return vec / np.linalg.norm(vec)


if __name__ == '__main__':
    from biblioteki.poly_xy.poly_xy_cls import PolyXY

    c = PolyXY([[5, 0, 0, 6]])
    f = norm_vers(c, (6, 6, 6))
    print(f)
    f = norm_vers(c, (0,1, 6))
    print(f)
    from programy.FDens.data import arr_of_const, array_of_calculeted

    poly = PolyXY([-0.012045535070196164, (0.00010955639307702763, 0.00010978615070158813),
                   (-2.404907912859456e-07, -2.526179357506328e-07, -2.577939959502564e-07),
                   (-4.100503389459874e-11, 6.568043634343362e-10, 4.974225347425486e-10, 8.432532261108681e-11),
                   (1.4793584953046583e-13, -4.4914388461441725e-13, -8.294387748834831e-13, -1.6995985984850315e-13,
                    -6.588170524380142e-14,)])
    xb= [a[0] for a in arr_of_const()]
    xc= [a[0] for a in array_of_calculeted()]

    yb= [a[1] for a in arr_of_const()]
    yc= [a[1] for a in array_of_calculeted()]

    zb=poly(xb,yb)
    zc=poly(xc,yc)