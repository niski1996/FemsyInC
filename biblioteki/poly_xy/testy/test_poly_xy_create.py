from biblioteki.poly_xy.poly_xy_cls import PolyXYCreate
import pytest

@pytest.mark.parametrize('num',(list(range(1,100))))
def test_by_amount_sym_last_level2_(num):
    pol=PolyXYCreate.by_amount_sym_last_level2_(num)
    assert num==pol.monomials
