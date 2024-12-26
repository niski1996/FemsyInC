"""liczy pole powierzchni zadanej wielomianem xy, ograniczonej przez funkcje filtrujące"""
import numpy as np

import  math
import itertools

import biblioteki.poly_xy.poly_xy_cls as pcl
import biblioteki.area.trian as tr


class FlatFilt:
    """group all function that filter flat set of points"""

    @staticmethod
    def circle(rad, center, point):
        """
        return True if `point' is not farther from `center` than `radius in xy space`
        If point is exacly on border return True

        :param rad:
        :param center, point :array_like
            2d point. if 3d third coord is omnited

        :return:bool
        """
        distance=math.sqrt((point[0]-center[0])**2+(point[1]-center[1])**2)
        if distance<=rad:
            return True
        else:
            return False

    @staticmethod
    def circle_meshgrid(rad, center, x, y):
        """

        :param rad:
        :param center:
        :param x:
        :param y:
        :return:
        """
        for rnum, row in enumerate(x):
            for cnum, col in enumerate(row):
                distance = math.sqrt((x[rnum][cnum] - center[0]) ** 2 + (y[rnum][cnum] - center[1]) ** 2)
                if distance>rad:
                    x[rnum][cnum]=None
                    y[rnum][cnum]=None



class PolyXYSurface:
    def __init__(self,poly, xrange,yrange,dens=100):
        self.poly=poly
        self.dens=dens
        lu,ru,rd,ld,c=self.char_points(xrange,yrange,dens)
        self.xc=c[0]
        self.yc=c[1]
        self.partial_surface=tr.sur_area_by_arrays(lu,ru,rd,ld)
        self.area=np.sum(self.partial_surface)





    def char_points(self,xrange,yrange,dens):
        """
        set characteristic points (corners and center) of square


        :param xrange:
        :param yrange:
        :param dens:
        :return:
        """
        xstep = (xrange[1] - xrange[0]) / dens
        ystep = (yrange[1] - yrange[0]) / dens
        x = np.linspace(xrange[0],xrange[1]-xstep, dens)
        y = np.linspace(yrange[0],yrange[1]-ystep, dens)
        xleft, ydown = np.meshgrid(x, y)
        xright=xleft+xstep
        yup=ydown-ystep
        xcenter=(xright+xleft)/2
        ycenter=(yup+ydown)/2
        z_left_up=self.poly(xleft,yup)
        z_left_down=self.poly(xleft,ydown)
        z_right_up=self.poly(xright,yup)
        z_right_down=self.poly(xright,ydown)
        return (xleft,yup,z_left_up),(xright,yup,z_right_up),(xright,ydown,z_right_down),(xleft,ydown,z_left_down),(xcenter,ycenter)

    def filter_center_points(self, filter_foo,*args,**kwargs):
        """

        :param filter_foo:
        :param args:
        :param kwargs:
        :return:
        """
        filter_foo(self.xc,self.yc,*args,**kwargs)

    def distributed_area(self,x,y):
        area=np.zeros_like(x).astype('float64')
        for nr,row in enumerate(self.partial_surface):
            for nv,val in enumerate(row):
                tmpx=np.ones_like(x)*self.xc[nr][nv]
                tmpy=np.ones_like(y)*self.yc[nr][nv]
                tx=(x-tmpx)**2
                ty=(y-tmpy)**2
                sum=tx+ty
                f=np.where(sum==np.min(sum))
                f=list(itertools.chain.from_iterable(f))
                area[f[0]][f[1]]+=val
        return area




# d=PolyXYSurface(pcl.PolyXY([6,(7,8,8,9)]),(0,100),(0,100))
# print(d.sur)
from biblioteki.arrays.filter import circle_meshgrid

d=PolyXYSurface(pcl.PolyXY([20,(1,1)]),(0,20),(0,20),dens=1000)
# # circle_meshgrid(40,(50,50),d.xc,d.yc)
# print(d.area)
# i=d.distributed_area(np.array([[1,2,3,4,5]]),np.array([[1,2,3,4,5]]))
# print(i)