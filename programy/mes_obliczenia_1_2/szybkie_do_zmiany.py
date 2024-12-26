import numpy as np
from biblioteki.poly_xy.poly_xy_cls import PolyXY
from biblioteki.area.trian import area_trian_set_by_points

from programy.mes_obliczenia_1_2.funkcje_pomocnicze import swich_poly


# def deriv_shield(n_matr):
#     res=None
#     def small_matr(poly):
#         dx = poly.deriv()
#         dy= poly.deriv(dx=False)
#         dz=poly.create_own_instance([0])
#         return np.array([[dx,0,0],
#                          [0,dy,0],
#                          [0,0,dz],
#                          [dy,dx,0],
#                          [dz,0,dx],
#                          [0,dz,dy]])
#     for el in n_matr[0]:
#         if res is None:
#             res=small_matr(el)
#         else:
#             res= np.concatenate((res,small_matr(el)), axis=1)
#     return res

def deriv_shield(n_matr):
    res = None

    def small_matr(poly):
        dx = poly.deriv()
        dy = poly.deriv(dx=False)
        dz = poly.create_own_instance([0])
        return np.array([[dx, 0],
                         [0, dy],
                         [dy, dx]])

    for el in n_matr[0]:
        if res is None:
            res = small_matr(el)
        else:
            res = np.concatenate((res, small_matr(el)), axis=1)
    return res


def set_Bq():
    a = PolyXY([(6, 0)])
    b = PolyXY([(0, 2)])
    c = PolyXY([(2, 0)])
    d = PolyXY([(0, 6)])
    e = PolyXY([(4, 4)])
    z = PolyXY([0])
    d = PolyXY([2])
    return np.array([[z, z, z, d, z, z, a, b, z],
                     [z, z, z, z, z, d, z, c, d],
                     [z, z, z, z, d, z, z, e, z]])


def set_D_kreska(e=200, h=0.3, v=0.3):
    d = (e * (h ** 3) / (12 * (1 - v ** 2)))
    m = np.array([[1, v, 0],
                  [v, 1, 0],
                  [0, 0, (1 - v) / 2]])
    return d * m



def set_k_q():
    bq = set_Bq()
    d_kr = set_D_kreska()
    tmp = np.matmul(bq.T, d_kr)
    tmp2 = np.matmul(tmp, bq)

def set_k_q_recznie2(nodes, e=200.0, h=0.3, v=0.3):
    xi = nodes[0][0]
    xj = nodes[1][0]
    xk = nodes[2][0]

    yi = nodes[0][1]
    yj = nodes[1][1]
    yk = nodes[2][1]

    A=(1/2)*((xj-xi)*(yk-yi)-(xk-xi)*(yj-yi))

    d = (e * (h ** 3) / (12 * (1 - v ** 2))) * A
    xijk=xi+xj+xk
    yijk=yi+yj+yk

    xy=xi * yi + xj * yj + xk * yk
    xx=xi*xj+xi*xk+xj*xk
    yy = yi*yj+yi*yk+yj*yk

    k44=4
    k66=k44
    k46=4*v
    k47=4*xijk
    k48=(4/3)*(yijk+v*xijk)
    k49=4*v*yijk
    k55=2*(1-v)
    k58=(4*(1-v)/3)*(xijk+yijk)
    k67=4*v*xijk

    k68=(4/3)*(v*yijk+xijk)
    k69=4*yijk
    k77=2*(xijk**2-xx)
    k78=(xijk*yijk+xy)+2*v*(xijk**2-xx)
    k79=3*v*(xijk*yijk+xy)
    k88=(2/3) * ((3-2*v)*(xijk**2-xx+yijk**2-yy)+(2-v)*(xijk*yijk+xy))
    k89=2*v*(yijk**2-yy)+(xijk*yijk+xy)
    k99=3*(yijk**2-yy)
    return d * np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, k44, 0, k46, k47, k48, k49],
                         [0, 0, 0, 0, k55, 0, 0, k58, 0],
                         [0, 0, 0, k46, 0, k66, k67, k68, k69],
                         [0, 0, 0, k47, 0, k67, k77, k78, k79],
                         [0, 0, 0, k48, k58, k68, k78, k88, k89],
                         [0, 0, 0, k49, 0, k69, k79, k89, k99]])





def set_k_q_recznie(nodes, e=200.0, h=0.3, v=0.3):
    d = (e * (h ** 3) / (12 * (1 - v ** 2))) * area_trian_set_by_points(*nodes)
    xi = nodes[0][0]
    xj = nodes[1][0]
    xk = nodes[2][0]

    yi = nodes[0][1]
    yj = nodes[1][1]
    yk = nodes[2][1]

    xijk = xi + xj + xk
    yijk = yi + yj + yk

    k44 = 4
    k66 = k44
    k46 = 4 * v
    k74 = 4 * xijk
    k48 = (4 / 3) * (yijk + v * xijk)
    k49 = 4 * v*yijk
    k55 = 2 * (1 - v)
    k58 = (4 / 3) * (1 - v) * (yijk + xijk)
    k67 = 4 * v * xijk


    k68 = (4 / 3) * (v * yijk + xijk)
    k69 = 4 * yijk
    k77 = 2 * (xijk ** 2 - xj * xi - xi * xk - xk * xj)
    k78 = (xijk * yijk + xi * yi + xj * yj + xk * yk) + v * k77
    k79 = 3 * v * (xijk * yijk + xi * yi + xj * yj + xk * yk)
    k89 = 2 * v * (yijk ** 2 - yi * yj - yi * yk - yk * yj) + (xijk * yijk + xi * yi + xj * yj + xk * yk)
    k99 = 3 * (yijk ** 2 - yi * yj - yi * yk - yk * yj)
    k88 = (2 / 3) * (
                (3 - 2 * v) * (xijk ** 2 - xi * xj - xi * xk - xj * xk + yijk ** 2 - yi * yj - yi * yk - yj * yk) + (
                    2 - v) * (xijk * yijk + xi * yi + xj * yj + xk * yk))
    return d * np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, k44, 0, k46, k74, k48, k49],
                         [0, 0, 0, 0, k55, 0, 0, k58, 0],
                         [0, 0, 0, k46, 0, k66, k67, k68, k69],
                         [0, 0, 0, k74, 0, k67, k77, k78, k79],
                         [0, 0, 0, k48, k58, k68, k78, k88, k89],
                         [0, 0, 0, k49, 0, k69, k79, k89, k99]])


def set_gi():
    a1 = PolyXY([1])
    a0 = PolyXY([0])
    ax1 = PolyXY([[1, 0]])
    ay1 = PolyXY([[0, 1]])
    asm = PolyXY([[0, 1, 0]])
    ay2 = PolyXY([[0, 0, 1]])
    ay3 = PolyXY([[0, 0, 0, 1]])
    ax2 = PolyXY([[1, 0, 0]])
    ax3 = PolyXY([[1, 0, 0, 0]])
    d1 = PolyXY([[0, 1, 1, 0]])
    d2 = PolyXY([[1, 2, 0]])
    d3 = PolyXY([[0, -2, -1]])
    mat = np.array([[a1, ax1, ay1, ax2, asm, ay2, ax3, d1, ay3],
                    [a0, a0, a1, a0, ax1, ay2 * 2, a0, d2, ay2 * 3],
                    [a0, a1 * -1, a0, ax1 * -2, ay1 * -1, a0, ax2 * -3, d3, a0]])
    return mat


# def set_g(gi, nodes):
#     return np.array([[gi[0][0](nodes[0][0],nodes[0][1])],
#                      [gi[1][0](nodes[0][0], nodes[0][1])],
#                      [gi[2][0](nodes[0][0], nodes[0][1])],
#                      [gi[0][0](nodes[1][0], nodes[1][1])],
#                      [gi[1][0](nodes[1][0], nodes[1][1])],
#                      [gi[2][0](nodes[1][0], nodes[1][1])],
#                      [gi[0][0](nodes[2][0], nodes[2][1])],
#                      [gi[1][0](nodes[2][0], nodes[2][1])],
#                      [gi[2][0](nodes[2][0], nodes[2][1])],
#                      ])
def set_g(gi, nodes):
    li0 = []
    for nod in nodes:
        for row in gi:
            li1 = []
            for elem in row:
                try:
                    elem.degree()
                    li1.append(elem(nod[0], nod[1]))
                except IndexError:
                    li1.append(0)
            li0.append(li1)
    return np.array(li0)


def gotowe_k_loc(nodes, e, h, v,):
    # for nod in nodes:
    #     for coor in nod:
    #         if coor < 0:
    #             raise Warning('wartosc mniejsza niz zero, moga byc bugi')

    xi = nodes[0][0]
    xj = nodes[1][0]-xi
    xk = nodes[2][0]-xi
    xi=0
    yi = nodes[0][1]
    yj = nodes[1][1]-yi
    yk = nodes[2][1]-yi
    yi=0
    nodes = [(xi,yi),(xj,yj),(xk,yk)]
    k_q = set_k_q_recznie(nodes, e=e, h=h, v=v)
    gi = set_gi()
    g = set_g(gi, nodes)
    l = np.linalg.inv(g)
    tmp = np.matmul(l.T, k_q)
    out = np.matmul(tmp,l)
    return out


if __name__ == '__main__':
    u=gotowe_k_loc([(0, 0, 0), (1, 1, 0), (2, 0, 0)],2.0e10,0.3,0.3)

    print(u[0:3,0:3])
    print('---------------------')
    u=gotowe_k_loc([(1, 0, 0), (2, 1, 0), (3, 0, 0)],2.0e10,0.3,0.3)

    print(u[0:3,0:3])
    # kq = set_k_q_recznie(((1, 1, 0), (4, 5, 0), (7, 2, 0)))
    # kq = set_k_q_recznie(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
    # gi = set_gi(np.array((1, 0, 0, 1, 1, 1, 0, 1, 1)).reshape(9, 1))
    # g = set_g(gi, ((1, 1, 0), (4, 5, 0), (7, 8, 0)))
