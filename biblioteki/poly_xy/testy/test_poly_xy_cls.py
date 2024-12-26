""" WAŻNE jak testy nie chcą importować, dodaj jakiś paramert i usuń __init__.py, wtedy już działa"""

from biblioteki.poly_xy.testy.fixture_polyclass import *


class TestBasePoly:


    def test_add(self, myset):
        myset.me=myset.me + myset.other
        assert myset.me == myset.result_add()

    def test_sub(self, myset):
        myset.me=myset.me - myset.other
        assert myset.me == myset.result_sub()

    def test_mul(self, myset):
        myset.me=myset.me * myset.other
        assert myset.me == myset.result_mul()

    def test_elem_len(self, myset):
        assert myset.me.elem_len == myset.result_elem_len()

    def test_degree(self,myset):
        assert myset.me.degree() == myset.result_degree()

    def test_monomials(self, myset):
        assert myset.me.monomials == myset.result_monomials()

    def test_rev(self, myset):
        tmp = [np.array_equal(myset.me.rev()[n], myset.result_rev()[n]) for n in range(len(myset.result_rev()))]
        assert all(tmp)

    def test_flat(self, myset):
        assert list(myset.me.flat()) == list(myset.result_flat())

    def test_components(self, myset): 
        tmp1 = [np.array_equal(myset.me.components(myset.point1)[n], myset.result_components1()[n]) for n in
               range(len(myset.me.value))]

        tmp2 = [np.array_equal(myset.me.components(myset.point2)[n], myset.result_components2()[n]) for n in
               range(len(myset.me.value))]
        assert all(tmp1)
        assert all(tmp2)

    def test_point_val(self, myset):
        assert myset.me.point_val(myset.point1[0],myset.point1[1]) == myset.result_val1()
        assert myset.me.point_val(myset.point2[0],myset.point2[1]) == myset.result_val2()


    # def test_der(self, myset):
    #     dx = [np.array_equal(list(myset.me.deriv())[n], myset.result_der_dx()[n]) for n in
    #           range(len(myset.result_der_dx()))]
    #     dy = [np.array_equal(list(myset.me.deriv(dx=False))[n], myset.result_der_dy()[n]) for n in
    #           range(len(myset.result_der_dy()))]
    #     assert all(dx)
    #     assert all(dy)
    def test_der(self, myset):
        # dx = [np.array_equal(list(myset.me.deriv())[n], myset.result_der_dx()[n]) for n in
        #       range(len(myset.result_der_dx()))]
        # dy = [np.array_equal(list(myset.me.deriv(dx=False))[n], myset.result_der_dy()[n]) for n in
        #       range(len(myset.result_der_dy()))]
        assert myset.me.deriv(dx=False) ==  myset.result_der_dy()
        # assert all(dy)