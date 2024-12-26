import numpy as np
import tkinter as tk
from programy.FDens import forces_iter
from programy.FDens.cylinder_force import forces as cyl
from programy.FDens.cylinder_force import warstwy as wrs

def force(mtype, nodes, val=0.01, root=None,):  # todo parser powinien wykryc zle argumenty, i pep 612
    """
    :param mtype: str
        'manual' do wprowadzani ręcznego
        'iter' do uruchomienia obliczeń sił prostopadłych do płaszczyzny o wartości 1
    :param nodes: array_like shape[n,5,3] or int for type 'manual' and 'auto_z'
        zestawy współrzędnych węzłów, które tworzą płaszczyznę. pierwszy na liście jest punkt w którym szukana będzie
        normalna do powierzchni
        [[[n1x,n1y,n1z],...[n5x,n5y,n5z]], --(dla pierwszej płaszczyzny)--
        ...]
    :param val float
        wartość sił normalnych
    :return: np.array shape(n,3)
        wartości sił
    """
    if mtype == 'auto_z':
        return auto_z(nodes, val=val)
    if mtype == 'manual':
        x = ManualNodes(nodes, root)
        return x.get_forc()
    if mtype == 'cylinder':
        x = cyl(nodes)
        return x
    if mtype == 'iter':
        x = forces_iter.Iter(nodes, val)
        return x.calculate()

def auto_z(nodes, val):
    tmp = np.zeros([nodes,3])
    for row in tmp:
        row[2]=-val
    return tmp


# class ManualNodes:
#
#     def __init__(self, row_num, root=None):
#         self.redy=False
#         self.row_num = row_num
#         self.forces_table = np.zeros([self.row_num, 3])
#         flag=0
#         if root is None:
#             self.force_window = tk.Tk()
#             flag=1
#         else:
#             self.force_window=tk.Toplevel(root)
#         self.frame1 = tk.Frame(master=self.force_window)
#         self.frame1.pack()
#         self.tkinter_menu()
#         if flag:
#             print('tworze mainloop dla forces')
#             self.force_window.mainloop()
#
#     def get_forc(self):
#         return self.forces_table
#
#     def tkinter_menu(self):
#         """ tworzy małe, niezależne okienko do wprowadzania węzłów"""
#         n = 0
#         lbx = tk.Label(master=self.frame1, text='X forces')
#         lbx.grid(row=0, column=1)
#         lby = tk.Label(master=self.frame1, text='Y forces')
#         lby.grid(row=0, column=2)
#         lbz = tk.Label(master=self.frame1, text='Z forces')
#         lbz.grid(row=0, column=3)
#         mrow = None
#         for mrow in range(self.row_num):
#             lb = tk.Label(master=self.frame1, text='węzeł numer {}'.format(n))
#             lb.grid(row=n + 1, column=0)
#             n += 1
#             for mcol in range(3):
#                 en = tk.Entry(master=self.frame1)
#                 en.grid(row=mrow + 1, column=mcol + 1)
#                 en.insert(0, '0')
#         accept = tk.Button(master=self.frame1, text="zatwierdź", command=self.accept_but)
#         accept.grid(row=mrow + 2, column=0, columnspan=4)
#
#     def accept_but(self):
#         for key in self.frame1.children:
#             # samo type() nie działa, wpisuje zły typ i błąd przy odpalaniu, nie znam poprawnego
#             if str(type(self.frame1.children[key])) == '<class \'tkinter.Entry\'>':
#                 row = self.frame1.children[key].grid_info()['row']
#                 col = self.frame1.children[key].grid_info()['column']
#                 self.forces_table[row - 1][col - 1] = float(self.frame1.children[key].get())
#         self.redy=True
#         self.force_window.destroy()


class ManualNodes:

    def __init__(self, row_num, root=None):
        self.redy = False
        self.row_num = row_num
        self.forces_table = np.zeros([self.row_num, 3])
        flag = 0
        if root is None:
            self.root = tk.Tk()
            flag=1
        else:
            self.root = root
        self.root.wm_attributes("-disabled", True)
        self.toplevel_dialog = tk.Toplevel(self.root)
        self.toplevel_dialog.transient(self.root)
        self.frame1 = tk.Frame(master=self.toplevel_dialog)
        self.frame1.pack()
        self.tkinter_menu()
        if flag:
            print('tworze mainloop dla forces')
            self.root.mainloop()

    def get_forc(self):
        return self.forces_table


    def tkinter_menu(self):
        """ tworzy małe, niezależne okienko do wprowadzania węzłów"""
        n = 0
        lbx = tk.Label(master=self.frame1, text='X forces')
        lbx.grid(row=0, column=1)
        lby = tk.Label(master=self.frame1, text='Y forces')
        lby.grid(row=0, column=2)
        lbz = tk.Label(master=self.frame1, text='Z forces')
        lbz.grid(row=0, column=3)
        mrow = None
        for mrow in range(self.row_num):
            lb = tk.Label(master=self.frame1, text='węzeł numer {}'.format(n))
            lb.grid(row=n + 1, column=0)
            n += 1
            for mcol in range(3):
                en = tk.Entry(master=self.frame1)
                en.grid(row=mrow + 1, column=mcol + 1)
                en.insert(0, '0')
        accept = tk.Button(master=self.frame1, text="zatwierdź", command=self.accept_but)
        accept.grid(row=mrow + 2, column=0, columnspan=4)


    def accept_but(self):
        for key in self.frame1.children:
            # samo type() nie działa, wpisuje zły typ i błąd przy odpalaniu, nie znam poprawnego
            if str(type(self.frame1.children[key])) == '<class \'tkinter.Entry\'>':
                row = self.frame1.children[key].grid_info()['row']
                col = self.frame1.children[key].grid_info()['column']
                self.forces_table[row - 1][col - 1] = float(self.frame1.children[key].get())
        self.redy=True
        self.root.wm_attributes("-disabled", False)  # IMPORTANT!
        self.toplevel_dialog.destroy()
        self.root.deiconify()

class Iter:
    def __init__(self, nodes_list, val, for_points = 'y'):
        self.for_poins = for_points
        self.nodes_list = nodes_list
        self.force_val = val
        self.norm_vers = None
        self.sur = None

    def callculate(self):
        """
        oblicza siły normalne
        :return: list
            lista sił współrzędnych wektora sił normalnych
        """
        li = []
        for node_set in self.nodes_list:
            if len(node_set) == 5:
                sur = surface_5_poitns(node_set)
            elif len(node_set) == 4:
                if self.for_poins == 'x':
                    sur = surface_4_poitns(node_set,True)
                elif self.for_poins == 'aver':
                    sur1=surface_4_poitns(node_set,True)
                    sur2=surface_4_poitns(node_set)
                    sur = [(sur1[x]+sur2[x])/2 for x in range(len(sur1))]
                else:
                    sur = surface_4_poitns(node_set)
            else:
                raise IndexError(' zestaw węzłów zawiera {} węzły: {}'.format(len(node_set), node_set))
            self.sur = sur
            grad = grad_5_points([*sur, -1])  # trzeba dodać ze względu na z, które przenoszę
            norm_dir = norm_in_point(grad, node_set[0])
            self.norm_vers = norm_dir / np.linalg.norm(norm_dir)
            norm_force = self.norm_vers * self.force_val
            li.append(norm_force)

        return np.array(li)

    def vect_check(self):
        tmp = vector_check(self.norm_vers, self.nodes_list[0][0], self.sur)
        print(tmp)



def surface_5_poitns(point_list):
    """
    Create equasion of surface based on points list
    :param point_list: array_like, shape(5,3)
        list of points located on a surface
    :return: list
        list of surface factors: [a,b,c,d,e], where surface equ i ax^2+by^2+cx+dy+e
    """
    no = []
    z = []
    for ll in point_list:
        row = [ll[0] ** 2, ll[1] ** 2, ll[0], ll[1], 1]
        zz = [ll[2]]
        no.append(row)
        z.append(zz)
    no = np.array(no)
    z = np.array(z)
    odw = np.linalg.inv(no)
    factors = np.matmul(odw, z)
    return factors.reshape(5)


def surface_4_poitns(point_list, missing_square_is_x=False):
    """
    Create equasion of surface based on points list
    :param point_list: array_like, shape(5,3)
        list of points located on a surface
    :param missing_square_is_x: bool
        define if square factor missing is x^2, else y^2
    :return: list
        list of surface factors: [a,b,c,d,e], where surface equ i ax^2+by^2+cx+dy+e
    """
    fac = 0
    pos=1
    if missing_square_is_x:
        fac = 1
        pos =0
    no = []
    z = []
    for ll in point_list:
        row = [ll[fac] ** 2, ll[0], ll[1], 1]
        zz = [ll[2]]
        no.append(row)
        z.append(zz)
    no = np.array(no)
    z = np.array(z)
    odw = np.linalg.inv(no)
    factors = np.matmul(odw, z)
    factors = list(factors.reshape(4))
    factors.insert(pos, 0)
    return factors


def grad_5_points(factors):
    """ liczy ogólny gradient, ale tylko dla szczególnej funkcji

    :param factors: array_like
        współczynniki [a,b,c,d,e,f], gdzie: ax^2+by^2+cx+dy+e+fz=0
    :return: list, shape(3,2)
        współczynniki [[df/dx],[df/dy],[df/dz]]
    """
    df_dx = [factors[0] * 2, factors[2]]
    df_dy = [factors[1] * 2, factors[3]]
    df_dz = [0, factors[5]]
    return [df_dx, df_dy, df_dz]


def norm_in_point(factors, point):  # Todo uwaga na zwrot
    """
    return normal vector in point
    :param factors: array_like, shape(3,2)
        współczynniki [[df/dx],[df/dy],[df/dz]],po dwa
    :param point: array_like
        coords of point [x,y,z]
    :return: list
        coords of vector [x,y,z]
    """
    vec = []
    for num, coord in enumerate(point):
        tmp_val = coord * factors[num][0] + factors[num][1]
        vec.append(tmp_val)
    return vec


def vector_check(vector, point, surface, increase=0.0000001):
    """
    check if vector is normal to surface by vector multiplication with vector of small incrise
    :param vector:array_like
        normal vector
    :param point:array_like
        tangent point
    :param surface: array_like
        list of surface factros [a,b,c,d,e] where z=ax^2+by^2+cx+dy+e
    :param increase: float
        very small value
    :return:list
        value of angle between vectors
    """
    versor = vector / np.linalg.norm(vector)

    def f(m, n):
        return surface[0] * m ** 2 + surface[1] * n ** 2 + surface[2] * m + surface[3] * n + surface[4]

    vec1 = np.array([-increase, -increase, point[2] - f(point[0] - increase, point[1] - increase)])
    vec2 = np.array([-increase, increase, point[2] - f(point[0] - increase, point[1] + increase)])
    vec3 = np.array([increase, -increase, point[2] - f(point[0] + increase, point[1] - increase)])
    vec4 = np.array([increase, increase, point[2] - f(point[0] + increase, point[1] + increase)])
    versor1 = vec1 / np.linalg.norm(vec1)
    versor2 = vec2 / np.linalg.norm(vec2)
    versor3 = vec3 / np.linalg.norm(vec3)
    versor4 = vec4 / np.linalg.norm(vec4)
    an1 = np.degrees(np.arcsin(np.linalg.norm(np.cross(versor1, versor))))  # kąt wyciągnięty z iloczynu wektorowego
    an2 = np.degrees(np.arcsin(np.linalg.norm(np.cross(versor2, versor))))
    an3 = np.degrees(np.arcsin(np.linalg.norm(np.cross(versor3, versor))))
    an4 = np.degrees(np.arcsin(np.linalg.norm(np.cross(versor4, versor))))
    return an1, an2, an3, an4


if __name__ == '__main__':
    a = np.array([4, 9, 10, 7, 12, 2, 3, 6, 7, 9, 3, 60, 7, 7, 7])
    a = a.reshape([5, 3])
    a = [a]
    mtype = 'manual'
    def h():
        if mtype == 'manual':
            x = ManualNodes(9)
            return x.get_forc()
    print(h())
