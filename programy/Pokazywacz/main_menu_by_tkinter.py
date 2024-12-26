from pathlib import Path

from programy.Pokazywacz.canvas_by_tkinter import *

import tkinter.colorchooser as cch
from programy.Pokazywacz import generator_nazw
from programy.Pokazywacz import sysinfo
from programy.Pokazywacz import pickle_magic
from programy.Pokazywacz import smutne_funkcje
from programy.Pokazywacz.butt_oper import butt_entry
from programy.Pokazywacz import ikony


slownik_obiektow = {}  # globalna zmienna zmieniana w trakccie egzekucji programu
# przykład złego programowania
ikony = []


class MainWindow:

    def __init__(self):
        """Tworzy główne okno programu.
        
        W przypadku dwóch monitorów, okno jest wysunięte możliwie najbardziej w lewo
        """

        self.window = Tk()
        width = 600
        height = 600
        self.temp_method = None
        self.x_coord, self.y_coord = sysinfo.main_window_position(height, width)
        self.window.geometry("%dx%d+%d+%d" % (width, height, self.x_coord, self.y_coord))
        self.temporairy_conainer = None
        self.prop_top = None
        self.generator = generator_nazw.Generator()
        self.frames()
        self.obiekt_canvas = CanvasClass(self, self.ctr_mid)
        self.menu(self.window)
        self.canvas = self.obiekt_canvas.canvas_window
        self.przestrzen = self.obiekt_canvas.przestrzen_obiektow
        self.button_bars()
        self.window.bind('<Motion>', self.motion)
        self.down()
        mainloop()

    @staticmethod
    def pomocnicza_do_ikon(nazwa, wielkosc):
        """Zwraca wskaźnik do obiektu obrazkowego png przygotowanego do podania jako ikona przycisku.
        Jako nazwa należy podać nazwe ikony umieszczonej w folderze ikony w głownym folderze.
         globalna lista konieczna, inaczej garbage collector niszczy obiekty i mam puste ramki w oknie"""
        str_nazwa = str(nazwa)
        kon_path = ".png"

        str_pocz_path = r""  # TODO zmienic sposób importu
        path = str_pocz_path + str(Path(__file__).parent) + "\\ikony\\" + str_nazwa + kon_path

        obraz = PhotoImage(file=path)
        nazwa = obraz.subsample(wielkosc, wielkosc)
        ikony.append(nazwa)
        return ikony[len(ikony) - 1]

    def motion(self, event):  # todo flag_motion motion powtórzony
        x, y = event.x, event.y
        self.pos_label.config(text='x={}; y={}'.format(x, y))
        return x, y

    def auto_butt(self, frame, tuptus):
        """automatycznie tworzy przyciski z listy tuptus w ramce frame"""
        for widget in frame.winfo_children():
            widget.destroy()
        for butt in tuptus:
            def foo(se):
                return eval('se.' + butt[0])  # jako se podaje obiekt, któy ma metode butt[0], a eval sciaga nawiasy

            x = foo(self)  # closures?

            ttub = Button(frame, text=butt[0], width=10, command=x)
            ttub.grid(row=butt[1], column=butt[2])

    # Tworzenie okna głownego

    @staticmethod
    def menu(window):
        """tworzy głowne okno i zagospodarowuje gorny pasek menu kaskadowego"""
        window.title("Krzykacz")  # ustawia nazwę programu
        menubar = Menu(window)  # tworzenie menu
        window.config(menu=menubar)  # wpakowanie menu
        file_menu = Menu(menubar)  # musi tak być inaczej mi sie bedzie powtarzać

        edit_menu = Menu(menubar)
        paint_menu = Menu(menubar)
        elem_menu = Menu(paint_menu)

        file_menu.add_command(label="nieaktywne:Zapisz", underline=0)
        file_menu.add_command(label="nieaktywne:Zapisz jako", underline=0)
        file_menu.add_command(label="nieaktywne:Otworz", underline=0)
        file_menu.add_command(label="nieaktywne:Nowy", underline=0)
        file_menu.add_command(label="nieaktywne:Drukuj", underline=0)

        edit_menu.add_command(label="nieaktywne:powtorz")
        edit_menu.add_command(label="nieaktywne:cofnij")
        edit_menu.add_separator()
        edit_menu.add_command(label="nieaktywne:kopiuj")
        edit_menu.add_command(label="nieaktywne:wklej")
        edit_menu.add_command(label="nieaktywne:wytnij")

        paint_menu.add_cascade(label="elementy rysunkowe", menu=elem_menu)
        paint_menu.add_command(label="niekatywne:siatka")

        elem_menu.add_command(label="niekatywne:linia")
        elem_menu.add_cascade(label="niekatywne:okrąg")
        elem_menu.add_cascade(label="niekatywne:prostokąt")

        menubar.add_cascade(label="plik", menu=file_menu)
        menubar.add_cascade(label="edycja", menu=edit_menu)
        menubar.add_cascade(label='rysuj', menu=paint_menu)

    def frames(self):
        """zagospodarowuje przestrzeń głownego okna ramkami i operuje na ich mechanizmach
        rozciągaia, aby odpowiednio wypełniały przestrzeń po rozciągnięciu. Ramki umieszczone dwupoziomowo."""
        top_frame = Frame(self.window, bg="dark slate gray", width=450, height=50)
        center = Frame(self.window, bg='gray2', width=50, height=40)
        self.btm_frame = Frame(self.window, bg='white', width=450, height=45)

        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        top_frame.grid(row=0, sticky="ew")
        center.grid(row=1, sticky="nsew")
        self.btm_frame.grid(row=3, sticky="ew")

        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)

        self.rysuj_container = Frame(top_frame, width=50, height=50, padx=3)
        self.rysuj_container.grid(row=0, column=0)
        self.modyfikuj_container = Frame(top_frame, width=50, height=50)
        self.modyfikuj_container.grid(row=0, column=1)
        self.ustawienia_container = Frame(top_frame, width=50, height=50, padx=3)
        self.ustawienia_container.grid(row=0, column=2)
        self.test_container = Frame(top_frame, width=50, height=50, padx=3)
        self.test_container.grid(row=0, column=3)

        self.ctr_left = Frame(center, bg='black')
        self.ctr_mid = Frame(center, bg='black', width=250, height=190)
        self.ctr_right = Frame(center, bg='black', width=100, height=190)
        self.ctr_left.grid(row=0, column=0, sticky="ns")
        self.ctr_mid.grid(row=0, column=1, sticky="nsew")
        self.ctr_right.grid(row=0, column=2, sticky="ns")

    def button_bars(self):
        wielkosc = 23
        # self potrzebne w module force density
        self.przyciski_rysuj = smutne_funkcje.butt_grid_org('punkt', 'linia', 'prostokąt', 'funkcja', 'właściwości_r',
                                                            'wymaż')
        przycisk_modyfikuj = smutne_funkcje.butt_grid_org('skaluj', 'przesuń')
        przycisk_ustawienia = smutne_funkcje.butt_grid_org('zapisz', 'otwórz')
        przycisk_test = smutne_funkcje.butt_grid_org('zgodność_linii')

        Button(self.rysuj_container, text='rysuj',
               command=lambda: self.auto_butt(self.ctr_left, self.przyciski_rysuj),
               image=MainWindow.pomocnicza_do_ikon('draw', 10)).grid(row=0, column=0)
        Button(self.modyfikuj_container, text='modyfikuj',
               command=lambda: self.auto_butt(self.ctr_left, przycisk_modyfikuj),
               image=MainWindow.pomocnicza_do_ikon('modify', 85)).grid(row=0, column=0)
        Button(self.ustawienia_container, text='ustawienia',
               command=lambda: self.auto_butt(self.ctr_left, przycisk_ustawienia),
               image=MainWindow.pomocnicza_do_ikon('ustawienia', wielkosc)).grid(row=0, column=0)
        Button(self.test_container, text='test',
               command=lambda: self.auto_butt(self.ctr_left, przycisk_test),
               image=MainWindow.pomocnicza_do_ikon('test', 72)).grid(row=0, column=0)

        def mp(mself, button):
            """"""
            if mself.przestrzen.magnet_points:
                button.config(fg='gray74')
            else:
                button.config(fg='black')
            mself.przestrzen.magnet_points = not mself.przestrzen.magnet_points

        r1 = Button(self.ctr_right, text='przyciągaj', width=10,
                    command=lambda: mp(self, r1))
        r1.grid(row=0, column=0, columnspan=2)

        def str(mself, button):
            if mself.przestrzen.straight:
                button.config(fg='gray74')
            else:
                button.config(fg='black')
            mself.przestrzen.straight = not mself.przestrzen.straight

        r2 = Button(self.ctr_right, text='proste', width=10, fg='gray74',
                    command=lambda: str(self, r2))
        r2.grid(row=1, column=0, columnspan=2)
        self.pos_label = Button(self.ctr_right, text='pozycja', width=10, command=lambda: butt_entry.CoordsByHand(
            self.pos_label, self, None, entry_width=8, mtyp=None))
        self.pos_label.grid(row=2, column=0, columnspan=2)
        self.z_button = Button(self.ctr_right, text=self.obiekt_canvas.z_coord, width=10,
                               command=lambda: butt_entry.Checker(self.z_button, self.obiekt_canvas, 'z_coord',
                                                                  entry_width=6))
        self.z_button.grid(row=3, column=0, columnspan=2)
        z_label = Label(self.ctr_right, text='z :')  # rysuje NA self.z_button
        z_label.grid(row=3, column=0, sticky=W)
        self.auto_butt(self.ctr_left, self.przyciski_rysuj)

    # Toolbar option
    def down(self):
        little_inspect = Button(self.btm_frame, text="info",
                                command=self.obiekt_canvas.przestrzen_obiektow.inspect_main)
        little_inspect.grid(row=0, column=0)
        details = Button(self.btm_frame, text='szczegóły', command=self.obiekt_canvas.przestrzen_obiektow.inspect_det)
        details.grid(row=0, column=1)
        labels = Button(self.btm_frame, text="Etykiety", command=self.obiekt_canvas.etykiety)
        labels.grid(row=0, column=2)

    # Toolbar rysuj
    def punkt(self):
        self.temp_method = Point(self, self.obiekt_canvas, self.przestrzen, self.generator, 'punkt', 1, None,
                                 'punkt', )
        self.canvas.bind("<Button-1>", self.temp_method.press)

    def linia(self):
        """wywołanie linii."""
        self.temp_method = Line(self, self.obiekt_canvas, self.przestrzen, self.generator, 'linia', 2,
                                self.canvas.create_line,
                                'linia', )
        self.canvas.bind("<Button-1>", self.temp_method.press)

    def prostokąt(self):

        self.temp_method = Prostokat(self, self.obiekt_canvas, self.przestrzen, self.generator, 'prostokat', 2,
                                     self.canvas.create_rectangle,
                                     'prostokat')
        self.canvas.bind("<Button-1>", self.temp_method.press)

    def okrąg(self):
        pass

    def funkcja(self):
        pass

    def właściwości_r(self):
        self.prop_top = Toplevel()
        width, height = 100, 100
        x_coord, y_coord = self.x_coord - width - 20, height
        self.prop_top.geometry("%dx%d+%d+%d" % (width, height, x_coord, y_coord))
        self.prop_top.title("Właściwości")

        kolor = Label(self.prop_top, text='kolor:')
        kolor.grid(row=0, column=0, sticky=E)
        self.kolor_button = Button(self.prop_top, bg=self.obiekt_canvas.kolor,
                                   width=2, height=1, command=self.kolory)
        self.kolor_button.grid(row=0, column=1)

        grubosc = Label(self.prop_top, text='grubość:')
        grubosc.grid(row=1, column=0, sticky=E)
        self.grubosc_button = Button(self.prop_top, text=self.obiekt_canvas.grubosc,
                                     width=2, height=1,
                                     command=lambda: butt_entry.Checker(self.grubosc_button, self.obiekt_canvas,
                                                                        'grubosc'))
        self.grubosc_button.grid(row=1, column=1)

        rodzaj = Label(self.prop_top, text='przerwy')
        rodzaj.grid(row=2, column=0, sticky=E)
        self.dash_button = Button(self.prop_top, text=self.obiekt_canvas.dash,
                                  width=2, height=1, command=self.dash)
        self.dash_button.grid(row=2, column=1)
        return self.prop_top

    # Toolbar linia
    # Toolbar prostokąt
    # Toolbar okrąg
    # Toolbar funkcja
    # Toolbar właściwości_r
    def kolory(self):
        kolor = cch.askcolor()
        if kolor:
            self.obiekt_canvas.kolor = kolor[1]
            self.kolor_button.destroy()
            self.kolor_button = Button(self.prop_top, bg=self.obiekt_canvas.kolor,
                                       width=2, height=1, command=self.kolory)
            self.kolor_button.grid(row=0, column=1)

    def dash(self):
        pass

    # Toolbar wymaż
    def wymaż(self):
        self.canvas.bind("<Button-1>", self.obiekt_canvas.usun_klik_bezposredni)
        del_name_list = (('pojedynczo', 0, 0), ('grupa', 1, 0), ('przez_tagi', 2, 0))
        self.auto_butt(self.ctr_left, del_name_list)

    def pojedynczo(self):
        pass

    def grupa(self):
        pass

    def przez_tagi(self):
        pass

    # Toolbar modyfikuj
    def skaluj(self):
        pass

    def przesuń(self):
        pass

    # Toolbar ustawienia
    def zapisz(self):
        pickle_magic.save(self)

    def otwórz(self):
        pickle_magic.open_fil(self)


if __name__ == "__main__":
    main_menu = MainWindow()
