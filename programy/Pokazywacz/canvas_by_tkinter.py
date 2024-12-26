"""Klasy:
CanvasClass - główne płótno programu. Wspiera metody działające bezpośrednio na widgecie canvas
    metody:
    siatka - tworzy siatkę
    usun_klik_bezpośredni - usuwa obiekt na ktory kliknięto lpm

DrawObject - klasa bazowa dla wszystkich obiektów rysunkowych
    metody:
    nazwa - tworzy nazwe obiektu
    press - wywoływana po wcisnieciu lpm, zczytuje aktualną pozycje kursora i zapisuje do list_of_kliks
    rysuj - tworzy obiekt rysunkowy
    contin - określa procedury po zakonczeniu wprowadzania obiektu
    dodawanie - dodaje obiekt do przestrzeni

Line - tworzy linie
Prostokat - tworzy prostokaty"""
from tkinter import *
from programy.Pokazywacz.abstract import DrawObject
from programy.Pokazywacz import przestrzen_obiektow

from programy.Pokazywacz.smutne_funkcje import motion


class CanvasClass:

    def __init__(self, menu, window):
        self.main_menu = menu
        self.window = window
        self.canvas_window = Canvas(window, bg="#142727")
        self.canvas_window.pack(fill=BOTH, expand=YES)
        self.przestrzen_obiektow = przestrzen_obiektow.PrzestrzenObiektow()
        self.__z_coord = 0
        self.__kolor = 'white'
        self.__grubosc = 2
        self.__dash = None

    def clear_canvas(self):
        self.canvas_window.delete(ALL)
        self.przestrzen_obiektow.przestrzen_obiektow = {}

    def etykiety(self):
        if len(self.canvas_window.children) !=0:
            children = list(self.canvas_window.children.keys())
            for child in children:
                self.canvas_window.children[child].destroy()
            return None
        for keys in self.przestrzen_obiektow.przestrzen_dict:
            widget = Label(self.canvas_window, text=keys, fg='white', bg='black')
            try:
                x,y,z=self.przestrzen_obiektow.przestrzen_dict[keys][1]['magnet_points']['srodki'][0]
                widget.place(x=x,y=y)
            except KeyError:
                x,y,z=self.przestrzen_obiektow.przestrzen_dict[keys][1]['magnet_points']['konce'][0]
                widget.place(x=x,y=y)




    def siatka(self, skok=50, kolor="#142710"):
        """Tworzy siatke. Obiekty nie są przyciągane"""
        start_val = 0
        end_val = 5000
        for x in range(start_val, end_val, skok):
            self.canvas_window.create_line(x, 0, x, end_val, fill=kolor, tags='canv_mesh')
            self.canvas_window.create_line(0, x, end_val, x, fill=kolor, tags='canv_mesh')

    def usun_klik_bezposredni(self, event):
        """Usuwa obiekt najbliższy od miejsca kliknięcia"""
        x, y = event.x, event.y
        tagged_item = self.canvas_window.find_closest(x, y)
        taglist = self.canvas_window.gettags(tagged_item)
        for key in self.przestrzen_obiektow.przestrzen_dict:
            if key in taglist:
                del self.przestrzen_obiektow.przestrzen_dict[key]
                break
        self.canvas_window.delete(tagged_item)
    @property
    def z_coord(self):
        return self.__z_coord
    @z_coord.setter
    def z_coord(self,z):
        self.__z_coord = z
    @property
    def kolor(self):
        return self.__kolor

    @kolor.setter
    def kolor(self, kolor):
        self.__kolor = kolor

    @property
    def grubosc(self):
        return int(self.__grubosc)

    @grubosc.setter
    def grubosc(self, grubosc):
        self.__grubosc = grubosc

    @property
    def dash(self):
        return self.__dash

    @dash.setter
    def dash(self, dash):
        if dash == 0:
            self.__dash = None
        else:
            self.dash = dash

class Point(DrawObject):
    def contin(self):
        self.window_obj.punkt()

    def press(self, event):
        x, y = event.x, event.y
        self.z.append(self.canvas_obiekt.z_coord)
        self.list_of_kliks.append([x,y])
        self.canvas.create_oval((x-self.canvas_obiekt.grubosc,y-self.canvas_obiekt.grubosc,
                                 x+self.canvas_obiekt.grubosc,y+self.canvas_obiekt.grubosc),
                                fill=self.canvas_obiekt.kolor, tags = self.tags)
        self.dodawanie()
        self.list_of_kliks = []
        self.canvas.bind('<Motion>', lambda eve: motion(event, self.window_obj.pos_label))
        self.contin()
    def dodawanie(self):
        self.list_of_kliks[0].append(self.z[0])
        self.object_space.dodawanie_do_przestrzeni(self, self.nazwa,
                                                   magnet_points={'konce': self.list_of_kliks},
                                                   tagi=self.tags,
                                                   property=super().property()
                                                   )

class Line(DrawObject):

    def contin(self):
        self.window_obj.linia()

    def dodawanie(self):
        super().dodawanie()
        srodek = [(self.srx, self.sry,self.srz)]
        self.object_space.dodawanie_do_przestrzeni(self, self.nazwa,
                                                   magnet_points={'konce': list(zip(*list(zip(*self.list_of_kliks)), self.z)), 'srodki': srodek},
                                                   tagi=self.tags,
                                                   property=super().property()
                                                   )


class Prostokat(DrawObject):

    def contin(self):
        self.window_obj.prostokąt()

    def dodawanie(self):
        super().dodawanie()
        centrum = [(self.srx, self.sry)]
        konce = [self.list_of_kliks[0],
                 (self.list_of_kliks[1][0], self.list_of_kliks[0][1]),
                 self.list_of_kliks[1],
                 (self.list_of_kliks[0][0], self.list_of_kliks[1][1])
                 ]
        srodki = []
        for num in range(len(konce)): #todo dołożyć parametr z
            x = (konce[num - 1][0] + konce[num - 2][0]) / 2
            y = (konce[num - 1][1] + konce[num - 2][1]) / 2
            srodki.append((x, y))
        self.object_space.dodawanie_do_przestrzeni(self, self.nazwa,
                                                   magnet_points={'konce': konce, 'srodki': srodki, 'centrum': centrum},
                                                   tagi=self.tags,
                                                   property=super().property()
                                                   )


class Okrag(DrawObject):

    def contin(self):
        self.window_obj.left_d_t.okrąg()
