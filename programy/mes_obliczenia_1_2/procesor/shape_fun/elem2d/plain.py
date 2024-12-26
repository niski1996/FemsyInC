import numpy as np
from biblioteki.poly_xy.poly_xy_cls import PolyXYCreate
from biblioteki.poly_xy.poly_fuu.poly_xy_fit import polfit_xy
from biblioteki.area.trian import area_trian_set_by_points

def plain_shape(nodes,val,der):
    """

    :param nodes:
    :param val:
    :param der:
    :return:
    """
    dx=[n[0] for n in der]
    dy=[n[1] for n in der]
    x=[cord[0] for cord in nodes]
    y=[cord[1] for cord in nodes]
    tmp = list(zip(x,y))
    skleton = PolyXYCreate.by_amount_sym_last_level2_(len(nodes)*3)
    poly = polfit_xy(nodes,val,skleton,{'dx':dx,'dy':dy})
    return poly



der = [[1,1],
       [1,1],
        [1,1]]

if __name__ == '__main__':
    print(plain_shape(((1,2,0),(4,5,0),(8,8,0)),(911,90,9),der))