import numpy as np
from biblioteki.area.poly_xy import PolyXYSurface
from biblioteki.vectors.vect_math import norm_vers

from programy.FDens.approks import Aproks

class Iter:
    """
    creates normal forces responding with area assigned to points in `nodes[0]`
    and `nodes[1]` unit forces have value of `val`
    :param nodes:
    :param val:
    """
    def __init__(self, nodes, val,):
        self.bord = nodes[0]
        self.free = nodes[1]
        self.force_val = val
        self.all_poi = list(self.bord)+list(self.free)



    def calculate(self):
        """
        start all calculation and return ready np.array of forces
        :return:
        """
        tmp= Aproks(self.bord,self.free,15)
        self.sur = tmp.pol
        dist = self.calc_area_distriution()
        vers = self.calc_vers_norm()
        dist=np.asarray(dist).reshape(len(dist),1)
        vers  =np.asarray(vers[len(self.bord):])
        return vers*dist*self.force_val

    def calc_area_distriution(self):
        """
        calculate area distribiution of self.sur
        :return:
        """
        mxx = max(self.all_poi, key=lambda x: x[0])
        mnx =min(self.all_poi, key=lambda x: x[0])
        mxy = max(self.all_poi, key=lambda x: x[1])
        mny =min(self.all_poi, key=lambda x: x[1])
        psur=PolyXYSurface(self.sur,(mxx[0],mnx[0]),(mxy[1],mny[1]),dens=100)#todo na próbe
        x= np.array([a[0] for a in self.all_poi]).reshape(1,len(self.all_poi))
        y= np.array([a[1] for a in self.all_poi]).reshape(1,len(self.all_poi))
        w=psur.distributed_area(x,y)
        print(psur.area)
        w = w[0,len(self.bord):] # wycina punkty stałe, bo siły w nich i tak bedą przekazane na podpory i nie zmienią konfiuguracji
        return w.T

    def calc_vers_norm(self):
        li=[]
        for elem in self.all_poi:
            li.append(norm_vers(self.sur,elem))
        return li





if __name__ == '__main__':
    import data
    free = data.array_of_calculeted()
    bord= data.arr_of_const()
    p=Iter((bord, free),5).calculate()
    print(p)