import pytest
import numpy as np
import biblioteki.poly_xy.poly_fuu.poly_xy_fit as pl
import random


@pytest.fixture()
def rand_poi():
    return np.random.rand(random.randint(3,4),2)

@pytest.fixture()
def rand_val():
    return np.random.rand(20)


def test_random_base(rand_poi,rand_val):
    rand_val=rand_val[0:len(rand_poi)]
    pol = pl.polfit_xy(rand_poi,rand_val)
    for num, poin in enumerate(rand_poi):
        assert round(pol.point_val(poin),6) == round(rand_val[num],6)

def test_random_one_der(rand_poi,rand_val):
    rand_val=rand_val[0:len(rand_poi)]
    rand_der= [a*random.randint(1,30) for a in rand_val]
    pol = pl.polfit_xy(rand_poi,rand_val, deriv={'dy':rand_der})
    for num, poin in enumerate(rand_poi):
        assert round(pol.point_val(poin),6) == round(rand_val[num],6)



@pytest.mark.parametrize('arr',(list(range(1,100))))
def test_collapse_into_poly_like(arr):
    a=np.zeros(arr)
    pl.collapse_into_poly_like(a)
    assert True