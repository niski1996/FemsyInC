import numpy as np

from programy.Visualizer.visualizer import Visual
from programy.FDens import forces
from programy.FDens.data import create_16_point as cr16
import math
from openpyxl import Workbook

class FormFinding:

    def __init__(self, task, force=False, iter=5, root=None, ):
        self.root = root  # tylko do ręcznych
        self.task = task  # zadanie do rozwiązania
        self.node_con = None  # macierz połączeń węzłów
        self.__result = None
        self.cor_el = []
        self.force = force
        self.iter = iter
        self.root = root

    def create_node_con(self):
        """creates node conection matrix based on data in self.task"""
        none_num = self.task.nodes.count(None)
        big = np.zeros([none_num, none_num])
        short_list = [np.zeros([none_num, 3]), ]
        for el in self.task.elements:
            el = el[:]  # tworzy kopię lokalną, chroniąc dane źródłowe przed zmianą
            q = el.pop(0)  # pierwsza wartość na liście to zadany współczynnik
            tr_num = list(map((lambda x: True if x >= none_num else False), el)).count(
                True)  # sprawdza ile elementów nie jest None
            if tr_num > 1:
                raise ValueError('dwa elementy stałe śączą się ze sobą, nie wiem co się stanie')
            elif tr_num == 1:
                tmp3 = list(filter((lambda x: True if x < none_num else False), el))  # wybiera węzły niewiadome
                big[tmp3[0]][tmp3[0]] += -q
                el.remove(tmp3[0])  # wybiera znane węzły
                n = 0
                try:  # cała ta instrukcja warunkowa jest ważna, gdy jeden element niewiadomy łączy się z
                    # więcej niż jednym węzłem stałym
                    while any(short_list[n][tmp3[0]]):  # TODO     TU MOŻE BYĆ PROBLEM Z WĘZŁEM 0,0,0
                        n += 1
                except IndexError:
                    short_list.append(np.zeros([none_num, 3]))
                short_list[n][tmp3[0]] = self.task.nodes[el[0]]
            else:
                big[el[0]][el[0]] += -q
                big[el[0]][el[1]] += q
                big[el[1]][el[1]] += -q
                big[el[1]][el[0]] += q
        return big, short_list

    def result(self):
        """zwraca wyniki, zależnie od typu wybranego przy trworzeniu instancji

        UWAGA przy typie 'iter' jak wejdzie do pęti, to funkcja iteracja() zmienia wartość zmiennej
        self.force na False, co teoretycznie nie powinno mieć znaczenia, ale pozwoli uniknąć tworzenia nowego obiektu
        wewnątrz istniejącego, żeby dobrać się do rozwiązań z siłąmi zerowymi"""
        a, b = self.create_node_con()
        s = None
        for n in b:
            if s is None:
                s = n
            else:
                s += n
        inv_a = np.linalg.inv(a)
        if not self.force:
            self.__result = -np.matmul(inv_a, s)
        elif self.force == 'iter':
            self.__result = self.iteracja(inv_a, s)
        else:
            forc = forces.force(self.force, self.task.nodes.count(None), root=self.root)
            self.__result = +np.matmul(inv_a, forc) - np.matmul(inv_a, s)
        return self.__result

    # def iteracja(self, inv_a, s):
    #     nod_con = self.node_all_conect()
    #     self.force = False
    #     actual_val = self.result()
    #     iter_num = 0
    #     while iter_num < self.iter:
    #         temp_nod_con = [b[:] for b in nod_con]  # lokalna kopia do podstwień punktó z chwilowej iteracji
    #         for n in temp_nod_con:
    #             for num, el in enumerate(n):
    #                 try:  # actual value nie zawiera węzłów stałych, więc musze je brac z innej listy
    #                     n[num] = actual_val[el]
    #                 except IndexError:
    #                     n[num] = self.task.nodes[el][:]
    #         forc = forces.force('iter', temp_nod_con, shape=self.shape)
    #         actual_val = np.matmul(inv_a, forc) - np.matmul(inv_a, s)
    #         iter_num += 1
    #     return actual_val
    #

    def iteracja(self, inv_a, s):
        """

        :param inv_a:
        :param s:
        :return:
        """
        nod_con = self.node_all_conect()
        self.force = 'auto_z' #dzięki temu tworzę pierwszą, zerową iteracje, żeby mieć jakiekolwiek siły
        actual_val = self.result()
        iter_num = 0
        while iter_num < self.iter:
            temp_nod_con = [b[:] for b in nod_con]  # lokalna kopia do podstwień punktó z chwilowej iteracji
            for n in temp_nod_con:
                for num, el in enumerate(n):
                    try:  # actual value nie zawiera węzłów stałych, więc musze je brac z innej listy
                        n[num] = actual_val[el]
                    except IndexError:
                        n[num] = self.task.nodes[el][:]
            forc = forces.force('iter', (self.task.nodes[len(temp_nod_con):],actual_val))#todo sprawdź bo to są relikty
            actual_val = np.matmul(inv_a, forc) - np.matmul(inv_a, s)
            iter_num += 1
        return actual_val

    def node_all_conect(self):
        """
        create list of nodes conection, where first node is node where put force vector later
        :return: list
        [[n1,n2,n3,n4],[n2,n5,n8,n3]...]

        """
        li = []
        for elem in range(self.task.nodes.count(None)):
            tmp = [elem]
            for el in self.task.elements:
                if el[1] == elem:
                    tmp.append(el[2])
                elif el[2] == elem:
                    tmp.append(el[1])
            li.append(tmp)
        return li

    def show(self,gif):
        for el in self.task.elements:
            el.pop(0)
            tmp = []
            for num in el:
                try:
                    n1 = self.__result[num]
                except IndexError:
                    n1 = self.task.nodes[num]
                tmp.append(list(n1))
            self.cor_el.append(tmp)
        li=[['segment',elem,{'color':'red'}] for elem in self.cor_el]
        Visual(*li,gif=gif)


def rozwiaz_zadanie(task, forces=False, show=False, gif=False, prnt=False, root=None, shape=None):
    x = FormFinding(task, forces, root=root,)
    wyn = x.result()
    if prnt:
        print(wyn)
        if True:
            # def ll(x):
            #     zakres = (100, 800)
            #     d = zakres[1] - zakres[0]
            #     r = d / 2
            #     a = x - zakres[0] - r
            #     b = math.sqrt(r ** 2 - a ** 2)
            #     return b
            # li=[]
            # for row in wyn:
            #     li.append([row[0],row[1],ll(row[0])])
            # print(wyn-np.array(li))
            workbook = Workbook()
            sheet = workbook.active

            for rnum, row in enumerate(wyn):
                for cnum,val in enumerate(row):
                    sheet.cell(rnum+1,cnum+1,val)

            workbook.save(filename="hello_world.xlsx")

    if show:
        x.show(gif)
    return wyn

if __name__ == '__main__':
    print(rozwiaz_zadanie(cr16(), show=True, ))