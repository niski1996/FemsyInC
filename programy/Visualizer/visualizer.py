import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import numbers


class Visual:
    """
    Base clas in 'projekt ostateczny' to visualize input and output

    paint 3d objects on one canvas. Once call, no posibilyty for re-call.

    object aviable:

    sphere - call by using keywords:('kula', 'sfera', 'przegub', 'ball')
    example set:
        ('kula', ((0, 0, 0),), { 'scale': 0.5})

    arrow - call by using keywords:('strzalka', 'wektor', 'sila_wezlowa', 'vector', 'nodal_force', 'arrow')
    example set:
        ('wektor', ((0, 0, 0),), { 'end'=(5,0,1)})
        ('arrow', ((0, 0, 0),), { 'increase'=(5,0,1),'scale': 0.5})




    """
    def __init__(self, *paint_sets, gif=False,):
        """

        :param paint_sets: tuple
            painting set (type:str - type of element, data:tuple - characteristic  3d points , keywords: dict)
        """
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(projection='3d')
        max_x, min_x, max_y, min_y, max_z, min_z = (1, -1, 1, -1, 1, -1,)
        for paint in paint_sets:
            if paint[0] not in ('poly','poly_xy','surface','wielomian','powierzchnia',):#ustawiagranice widoku
                for data in paint[1]:
                    if data[0] > max_x:
                        max_x = data[0]
                    elif data[0] < min_x:
                        min_x = data[0]
                    if data[1] > max_y:
                        max_y = data[1]
                    elif data[1] < min_y:
                        min_y = data[1]
                    if data[2] > max_z:
                        max_z = data[2]
                    elif data[2] < min_z:
                            min_z = data[2]
        margin = 1
        self.ax.set_xlim3d(min_x * margin, max_x * margin)
        self.ax.set_ylim3d(min_y * margin, max_y * margin)
        self.ax.set_zlim3d(min_z * margin, max_z * margin)

        # self.ax.set_xlim3d(0,4)
        # self.ax.set_ylim3d(-1,2)
        # self.ax.set_zlim3d(0,40)

        for el in paint_sets:
            self.match_method(el)
        if gif:
            self.gif()
        # self.ax.view_init(elev=0., azim=90 )

        plt.show()

    def match_method(self, paint_set):
        if paint_set[0] in ('strzalka', 'wektor', 'sila_wezlowa', 'vector', 'nodal_force', 'arrow'):
            self.paint_arrow(paint_set[1][0], **paint_set[2])
        elif paint_set[0] in ('kostka', 'utwierdzenie', 'szescian', 'cube'):
            self.paint_cube(paint_set[1][0], **paint_set[2])
        elif paint_set[0] in ('odcinek', 'linia', 'segment', 'line'):
            self.paint_segment(paint_set[1][0], paint_set[1][1], **paint_set[2])
        elif paint_set[0] in ('kula', 'sfera', 'przegub', 'ball'):
            self.paint_sphere(paint_set[1][0], **paint_set[2])
        elif paint_set[0] in ('poly','poly_xy','surface','wielomian','powierzchnia'):
            self.paint_poly(paint_set[1], **paint_set[2])
        elif paint_set[0] in ('points', 'punkty'):
            self.paint_point(*paint_set[1],**paint_set[2])

    def paint_point(self,x,y,z):
        self.ax.scatter(x, y, z, marker='o')
        self.ax.set_xlim3d(0, 450)
        self.ax.set_ylim3d(0, 450)
        self.ax.set_zlim3d(0, 200)

    def paint_sphere(self, center, radius=1, color='r',scale=1):
        radius=scale*radius
        u = np.linspace(0, 2*np.pi, 100)
        v = np.linspace(0, 2*np.pi, 100)
        x = radius * np.outer(np.cos(u), np.sin(v)) + center[0]
        y = radius * np.outer(np.sin(u), np.sin(v)) + center[1]
        z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
        self.ax.plot_surface(x, y, z, color=color)


    def paint_poly(self,poly, dens=40, xrange=(0,50), yrange=(0,50), zrange=(0,50), setx=None, sety=None, **kwargs):
        x=np.linspace(*xrange,dens)
        y=np.linspace(*yrange,dens)
        xx,yy = np.meshgrid(x,y)
        if sety is not None:
            yy=sety
        if setx is not None:
            xx=setx
        z=poly(xx,yy)
        #pozbywa się nan-ów
        for rnum, row in enumerate(z):
            for cnum, col in enumerate(row):
                if np.isnan(col):
                    z[rnum][cnum]=0
        # z=np.ones_like(xx)
        self.ax.plot_surface(xx, yy, z, cmap=plt.cm.coolwarm,**kwargs)
        self.ax.set_xlim3d(xrange[0], xrange[1])
        self.ax.set_ylim3d(yrange[0], yrange[1])
        self.ax.set_zlim3d(zrange[0], zrange[1])


    def paint_arrow(self, begin, end=None, increase=None, scale=1,**kwrd):
        """
        paint one arrow 3d in scale

        :param begin: tuple
            touchdown point of arrow
        :param end: tuple
            replaceble with "increase" parameter,coords of arrow end
        :param increase:
            replaceble with "end" parameter, magnitiude of increase
        :param scale: float
            arrow scale
        :return: None
        """

        if end is not None and increase is not None:
            raise Warning('there are both, end and increase parametre. Result may be misleading ')
        if end is not None:
            increase = (end[0] - begin[0], end[1] - begin[1], end[2] - begin[2])
        elif increase is not None:
            end = [begin[0] + increase[0], begin[1] + increase[1], begin[2] + increase[2]]
        lenght = math.sqrt((end[0] - begin[0]) ** 2 + (end[1] - begin[1]) ** 2 + (end[2] - begin[2]) ** 2) * scale

        # heads of the arrows with adjusted arrow head length
        self.ax.quiver(begin[0], begin[1], begin[2], increase[0], increase[1], increase[2],
                       length=lenght, normalize=True, arrow_length_ratio=0.15, **kwrd)

    def paint_cube(self, center, edge=1, color='b', scale=1):
        edge = scale * edge
        r = [-edge / 2, edge / 2]
        x, y = np.meshgrid(r, r)
        one = np.ones(4).reshape(2, 2) + edge / 2 - 1
        self.ax.plot_surface(x + center[0] , y + center[1]  , one + center[2], alpha=1,
                             color=color)
        self.ax.plot_surface(x + center[0] , y + center[1] , -one + center[2], alpha=1,
                             color=color)
        self.ax.plot_surface(x + center[0] , -one + center[1] , y + center[2], alpha=1,
                             color=color)
        self.ax.plot_surface(x + center[0] , one + center[1], y + center[2], alpha=1,
                             color=color)
        self.ax.plot_surface(one + center[0], x + center[1], y + center[2], alpha=1,
                             color=color)
        self.ax.plot_surface(-one + center[0] , x + center[1], y + center[2], alpha=1,
                             color=color)

    def paint_segment(self, start, end, **kwrd):
        tmp = list(zip(start, end))
        self.ax.plot(*tmp, **kwrd)

    def gif(self):
        def init():
            return self.fig,

        def animate(i):
            self.ax.view_init(elev=30., azim=1.8 * i)
            return self.fig,

        ani = animation.FuncAnimation(self.fig, animate, init_func=init,
                                      frames=100, interval=100, blit=True)

        ani.save('the_movie.gif', writer='pillow', fps=30)

#
# ar1 = ('cube', ((0, 10, 0),), { 'scale': 0.5})
# ar2 = ('cube', ((2, 0, 0),), { 'scale': 0.5})
# ar3 = ('cube', ((2, 2, 0),), { 'scale': 0.5})
# ar4 = ('cube', ((0, 0, 0),), { 'scale': 0.5})
#
# d = Visual(ar1, ar2, ar3, ar4, )
#
# d.paint_arrow((0, 0, 0), end=(0, 1, 0))
# d.paint_arrow((0, 0, 0), end=(0,0 , 1))
# d.paint_arrow((0, 0, 0), end=(1, 0, 0))
