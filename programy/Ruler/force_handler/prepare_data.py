"""Moduł służy do przygotowania danych z programu `handler` do wprowaadzenia
do głównego programu oblicającego
klasy:
Details - klasa służąca do precyzowania szczegółów zadania, aktualnie niedziałająca.
    były problemy z odpaleniem okna. W tkinterze może być tylko jedno mainloop. Praowdopodobnie
    po kliknięciu 'policz' należełoby jakoś wstrzymać egzekucję programu
Conector - klasa służy do zmienienia danych z słowników przestrzeni obiktów z Pokazywacza, do danych
    zrozumiałych dla głównego programu
"""

from programy.FDens.data import DataSet
from programy.FDens.FDens import rozwiaz_zadanie
import tkinter as tk


class Details:
    "specify details for task"

    def __init__(self):
        self.window = tk.Tk()
        self.tmp_dict = {}
        frame1 = tk.Frame(master=self.window)
        frame1.pack()
        tk.Label(frame1, text='wyjście punktów na konsoli').grid(row=0, column=0)
        tk.Label(frame1, text='siły').grid(row=1, column=0)
        tk.Label(frame1, text='wyświetl na wykresie').grid(row=2, column=0)
        tk.Label(frame1, text='stwórz gifa').grid(row=3, column=0)
        tk.Label(frame1, text='zapisz dane').grid(row=4, column=0)
        tk.Label(frame1, text='inspekcja prostopadłości sił').grid(row=5, column=0)

        def bug_hack(var):
            """ tylko tak da się obejsc buga: w duzym programie nie zmienia checkboxó,
            jako staticmethod działa bez zarzótów, nw dlaczego"""

            var.myset(not var.get())

        cons_val = tk.BooleanVar()
        tk.Checkbutton(frame1, variable=cons_val, command=lambda: bug_hack(cons_val)).grid(row=0, column=1)

        wykr_val = tk.IntVar()
        tk.Checkbutton(frame1, variable=wykr_val, command=lambda: bug_hack(wykr_val)).grid(row=2, column=1)

        gif_val = tk.IntVar()
        tk.Checkbutton(frame1, variable=gif_val, command=lambda: bug_hack(gif_val)).grid(row=3, column=1)

        save_val = tk.IntVar()
        tk.Checkbutton(frame1, variable=save_val, command=lambda: bug_hack(save_val)).grid(row=4, column=1)

        def okjej():
            if cons_val.get():
                self.tmp_dict['prnt'] = True
            if wykr_val.get():
                self.tmp_dict['show'] = True
            if gif_val.get():
                self.tmp_dict['gif'] = True

            self.window.destroy()

        accept = tk.Button(frame1, text='zatwierdź', command=okjej).grid(row=6, column=1)
        self.window.mainloop()


class Conector:
    """
    Class to transform input from `przes` which is 'Pokazywacz' style of data
    :param przes: dict
    słownik przestrzeni obiktów z Pokazywacza
    :param autorun: bool
    :param root: to jest potrzebne chyba do wyświetlania dodatkowych okien (dla tkintera)
    """

    def __init__(self, przes, autorun=1, root=None):
        """
        """
        self.main_dict = przes
        self.points = None
        self.elem, self.points = self.conect()
        if autorun:
            tmp = DataSet()
            tmp.node_set(self.points)
            tmp.elem_set(self.elem)
            # det = Details() z jakiegos powodu to góeno nie działa, chyba przez mainloopa
            det = {'gif': False, 'forces':"cylinder", 'show': True, 'prnt': True, 'root': root,
                   'shape': 'aver'}  # jakies hujowe zastepstwo okienka wyboru
            rozwiaz_zadanie(tmp, **det)

    def extract(self, mtype):
        """
        extract coords of mtype from main_dict
        :return: list
        list of points with xyz coords [[],...[]]
        """
        li = []
        for key, val in self.main_dict.items():
            if mtype in val[1]['tagi']:
                li.append(val[1]['magnet_points']['konce'])
                li[-1] = li[-1][:]
                li[-1].append(key)
        return li

    def sort_points(self):
        """
        move all points with 3rd coords None to the beggining
        :return: list
        sorted list of points with xyz coords [[],...[]]
        """
        tmp = self.extract('punkt')
        tmp = [el[0] for el in tmp]
        return sorted(tmp, key=lambda x: (x[2] is not None, x[2]))

    def conect(self):
        """

        :return: list
            list of elements
        """
        elems = []
        self.points = self.sort_points()
        lines = self.extract('linia')
        for ielem in lines:
            try:
                n1 = self.points.index(list(ielem[0]))
                n2 = self.points.index(list(ielem[1]))
                q = self.main_dict[ielem[-1]][1]['property']['factor']
                elems.append([q, n1, n2])
            except ValueError:
                print("ValueError wystąpił przy lini {}".format(ielem))
        return elems, self.nodes_prepare()

    def nodes_prepare(self):
        """ check if z coords is None change all coords to one None"""
        for num, ielem in enumerate(self.points):
            if ielem[2] is None:
                self.points[num] = None
        return self.points
