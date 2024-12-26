from biblioteki.poly_xy.poly_xy_cls import PolyXY
def poly_grad(poly):
    """
    Return array `PolyXY' gradient

    :param poly: PolyXY object
    :return: list
        list contains three `PolyXY`
    """
    dx=poly.deriv()
    dy = poly.deriv(dx=False)
    dz=poly.create_own_instance([-1,])
    return dx,dy,dz


if __name__ == '__main__':
    c= PolyXY([[5,0,0,6]])
    w=poly_grad(c)
    w=poly_grad(c)

