import abc
from programy.Pokazywacz import smutne_funkcje
from programy.Pokazywacz.smutne_funkcje import motion
from tkinter import TclError


class BaseObject(abc.ABC):

    def __init__(self, main_menu, canvas_obiekt, przestrzen_obiekt, generator):
        self.window = main_menu.window
        self.window_obj = main_menu
        self.canvas_obiekt = canvas_obiekt
        self.canvas = canvas_obiekt.canvas_window
        self.space = przestrzen_obiekt.przestrzen_dict
        self.object_space = przestrzen_obiekt
        self.generator = generator


class DrawObject(BaseObject, abc.ABC):

    def __init__(self, main_menu, canvas_obiekt, przestrzen_obiekt, generator,
                 nazwa, klik, metoda, *tags):
        super().__init__(main_menu, canvas_obiekt, przestrzen_obiekt, generator)
        self.metoda = metoda
        self.nazwa = self.generator.nazwa(nazwa)
        self.tags = (self.nazwa, self.__class__, *tags)
        self.klik = klik  # wymagana ilość kliknięć do zdefiniowania jakiejć figury
        self.list_of_kliks = []
        self.z = []

    def press(self, event):
        """Dodaje współrzedne obiektu do list_of_kliks"""
        self.window.bind('<Escape>', self.abandon)
        if self.klik > len(self.list_of_kliks):
            self.list_of_kliks.append(
                list(smutne_funkcje.przyciaganie(event.x, event.y, self.object_space, self.window_obj)))
            self.z.append(self.canvas_obiekt.z_coord)
        if self.klik - 1 == len(self.list_of_kliks):
            self.canvas.bind('<Motion>', self.rysuj)
        if self.klik == len(self.list_of_kliks):
            self.rysuj(event)
            self.z[1] = self.canvas_obiekt.z_coord
            self.dodawanie()
            delattr(self, 'temp_draw')
            self.list_of_kliks = []
            self.canvas.bind('<Motion>', lambda eve: motion(event, self.window_obj.pos_label))
            self.contin()

    def rysuj(self, event):
        """Steruje śledzeniem obiektu, poprzez tworzenie tymczasowych obiektów
        odpowiadających w miejscu aktualnego położenia kursora"""
        x1, y1 = motion(event, self.window_obj.pos_label)
        if hasattr(self, 'temp_draw'):  # sledzenie magnet pointsów i katów prostych
            bol1 = bool(self.canvas.type(self.temp_draw) == 'line')
            bol2 = self.object_space.straight
            if bol1 and bol2:
                x0, y0 = self.list_of_kliks[0][0], self.list_of_kliks[0][1]
                x1, y1 = smutne_funkcje.only_straight(x0, y0, x1, y1)
            if self.object_space.magnet_points:
                x1, y1 = smutne_funkcje.przyciaganie(x1, y1, self.object_space, self.window_obj)
            self.canvas.delete(self.temp_draw)
        if len(self.list_of_kliks) == self.klik:
            self.list_of_kliks[-1] = (x1, y1)
            list_of_kliks = [x for num in self.list_of_kliks for x in num]
        else:  # przepakowanie listy i dodanie położenia kursora, aby dostać tymczasowy rysunek
            list_of_kliks = [x for num in self.list_of_kliks for x in num] + [x1, y1]
        try:  # rysuje na podstawie metody podanej przy pierwszym wywołaniu
            self.temp_draw = self.metoda(*list_of_kliks, outline=self.canvas_obiekt.kolor,
                                         dash=self.canvas_obiekt.dash, width=self.canvas_obiekt.grubosc,
                                         tags=self.tags)
        except TclError:
            self.temp_draw = self.metoda(*list_of_kliks, fill=self.canvas_obiekt.kolor,
                                         dash=self.canvas_obiekt.dash, width=self.canvas_obiekt.grubosc,
                                         tags=self.tags, )

    def contin(self):
        """zamyka pętle"""
        pass

    def abandon(self, event):
        try:
            self.canvas.delete(self.temp_draw)
            delattr(self, 'temp_draw')
            self.list_of_kliks = []
            self.canvas.bind('<Motion>', lambda eve: motion(event, self.window_obj.pos_label))
            self.contin()
        except AttributeError:
            pass

    def dodawanie(self):
        """dodaje gotowy obiekt do przestrzeni obiektów. Charakterystyczne dla każdego rodzaju obiektu"""
        self.srx = (self.list_of_kliks[0][0] + self.list_of_kliks[1][0]) // 2
        self.sry = (self.list_of_kliks[0][1] + self.list_of_kliks[1][1]) // 2
        self.srz = (lambda : None if None in self.z else (self.z[1]+self.z[0]) / 2)() #musi tak byc przez
        # 'wolne węzły ' w force density

    def property(self):
        return {'grubosc': self.canvas_obiekt.grubosc, 'przerywana': self.canvas_obiekt.dash,
                'kolor': self.canvas_obiekt.kolor}
