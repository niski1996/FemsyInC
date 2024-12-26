import numpy as np
from biblioteki.poly_xy.poly_xy_cls import PolyXYCreate
from biblioteki.poly_xy.poly_fuu.poly_xy_fit import polfit_xy
from biblioteki.area.trian import area_trian_set_by_points

def shape_fun_2d(nodes,val):
    """

    :param nodes:
    :param val:
    :return:
    """
    x=[cord[0] for cord in nodes]
    y=[cord[1] for cord in nodes]
    tmp = list(zip(x,y))
    skleton = PolyXYCreate.by_amount_sym_last_level2_(len(nodes))
    poly = polfit_xy(nodes,val,skleton)
    return poly

def triangle_coef(nodes):
    ar=area_trian_set_by_points(*nodes)
    ar=0.5
    a1=nodes[1][1]-nodes[2][1]
    a2=nodes[2][1]-nodes[0][1]
    a3=nodes[0][1]-nodes[1][1]

    b1=nodes[2][0]-nodes[1][0]
    b2=nodes[0][0]-nodes[2][0]
    b3=nodes[1][0]-nodes[0][0]

    c1 = nodes[1][0]*nodes[2][1]-nodes[2][0]*nodes[1][1]
    c2 = nodes[1][0]*nodes[2][0]-nodes[0][0]*nodes[2][1]
    c3 = nodes[1][0]*nodes[2][1]-nodes[2][0]*nodes[1][1]

    print('a: ',a1/(2*ar),a2/(2*ar),a3/(2*ar))
    print('b: ',b1/(2*ar),b2/(2*ar),b3/(2*ar))
    print('a: ',c1/(2*ar),c2/(2*ar),c3/(2*ar))


if __name__ == '__main__':
    a=shape_fun_2d([(0,45,0),(13,11,0),(0,15,0)],[1,0,0])
    print(a)