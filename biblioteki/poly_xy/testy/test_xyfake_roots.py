import pytest
import numpy as np
from biblioteki.poly_xy.poly_fuu.xyfake_roots import *
from biblioteki.poly_xy.poly_fuu.poly_xy_fit import collapse_into_poly_like
from biblioteki.poly_xy.poly_xy_cls import PolyXY


@pytest.fixture(params=(range(1,30)))
def random_poly(request):
    n=2+request.param
    while True:
        try:
            n+=1
            p=collapse_into_poly_like(np.random.randint(-100,100,size=n))
            p=collapse_into_poly_like(list(range(n)))
            return PolyXY(p)
        except ValueError:
            pass
# def test_poly_xy_cross():
#     pol = PolyXY([6,(1,1),(4,0,0)])
#     assert poly_xy_cross(pol,1)==np.polynomial.Polynomial((7,1,4))
#
# def test_poly_xy_cross2():
#     pol = PolyXY([6,(1,1),(4,0,0)])
#     assert poly_xy_cross(pol,1,False)==np.polynomial.Polynomial((11,1))
#
# def test_poly_xy_cross3 ():
#     pol = PolyXY([6,(1,1),(4,0,0)])
#     assert poly_xy_cross(pol,10)==np.polynomial.Polynomial((16,1,4))
#
# def test_poly_xy_cross4 (random_poly):
#     rar=np.random.randint(1000,1000000000,2)
#     xpol = poly_xy_cross(random_poly, rar[1])
#     assert abs( (xpol(rar[0]) - random_poly(*rar)) / float(xpol(rar[0])) ) <= 0.02


#test nie bedzie przechodził, służy do wyznaczenia zakresu stoswania funkcji
@pytest.mark.xfail
def test_xyfake_poly_xy_roots(random_poly):
    tmp=xyfake_poly_xy_roots(random_poly,(1,500),2)
    zz=list(random_poly([complex(a[0]) for a in tmp], [complex(a[1]) for a in tmp]))
    for num, v in enumerate(zz):
        assert round(v,1)==0

