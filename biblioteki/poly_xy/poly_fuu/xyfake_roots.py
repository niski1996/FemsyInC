import  numpy as np
from biblioteki.poly_xy.poly_xy_cls import PolyXY
def xyfake_poly_xy_roots(poly,yrange, griddens):
    """
    find some roots of two variables polynomial

    find roots for poly_x  created by taking second value of
    poly_xy as constans for nodes in border of yrange, and density
    of griddens. i.e. for poly=f(x,y), yrange=(0,3), griddens=2
    rturn list of points which gave 0 for poly: f(x,y) where y=1 ;
    f(x,y) where y=2 ;

    :param poly: Poly_XY obiekt
    :param yrange: tuple
        range of y
    :param griddens:int
        density of grid
    :return:

    WYSOCE NIESTABILNY, ZAKRES STOSOWNAIA W GRANICACH 1-500 TO MAX 4 STOPIEŃ
    BŁĄD NARASTA WYKŁADNICZO, WIEC PRZY WIEKSZEJ ILOSCI SKLADNIKÓW WYNIKI NIE SA ZEROWE, TYLKO POJEBANE

    MOŻLIWE BŁĘDY WYNIKAJĄCE Z POMINĘCIA MIEJSC ZEROWYCH: LICZE TYLKO PO JEDNEJ POCHODNEJ, WIEC TEORETYCZNIE
    PRZY 'FALOWYM' UKŁADZIE FUNKCJI NP. X=CONST, F(X,Y)==>F(Y) FUNKCJA MOŻE BYĆ PASMOWA, WIĘC PRZY WZIĘCIU POCHODNYCH
    DX MOŻLIWE JEST, ŻE NIE WYKRYJE ŻADNYCH  MIEJSC ZEROWYCH, PODCZAS GDY ZAK NA PRAWDĘ BĘDĄ ONE ISTNIEĆ.
    """
    yr=np.linspace(yrange[0],yrange[1],griddens)


    poi_li=[]
    for const in yr:
        u=poly_xy_cross(poly,const, const_y=True)
        tmp=u.roots()
        for val in tmp:
            poi_li.append((val,const))
    return poi_li


def poly_xy_cross(poly, crossval,const_y=True):
    """
    degrades poly_xy to one variable polynomial

    return one variable polynomial by treating second variable as constans with value `crossval

    :param poly:
    :param crossval:
    :param const_y:
    :return:
    """
    if const_y:
        cmp=poly.components((1,crossval))
    elif not const_y:
        cmp = poly.components((crossval,1))
    else:
        raise ValueError
    one_poly = np.polynomial.Polynomial(0)
    for el in cmp:
        if const_y:
            tmp = np.polynomial.Polynomial(np.flip(el))
        else:
            tmp = np.polynomial.Polynomial(el)


        one_poly+=tmp
    return one_poly

# pol=PolyXY([-0,(1,1,1)])
# d=xyfake_poly_xy_roots(pol, (-10, 10), 100)
# print(d)