import itertools

class Generator:
    def __init__(self):
        self._przestrzen_nazw = {}

    def inspect(self):
        for key in self._przestrzen_nazw:
            print('Nazaw klucza: ', key)
            for name in self._przestrzen_nazw[key]:
                print(name)

    def nazwa(self, nazwa: str):
        if nazwa in self._przestrzen_nazw.keys():
            last = len(self._przestrzen_nazw[nazwa]) - 1
            num = int(self._przestrzen_nazw[nazwa][last].replace(nazwa, ''))
            self._przestrzen_nazw[nazwa].append(nazwa + str(num + 1))
            return nazwa + str(num + 1)
        else:
            self._przestrzen_nazw[nazwa] = [nazwa + str(1)]
            return nazwa + str(1)

    def add_val(self,mkey, mval):
        if mkey not in self._przestrzen_nazw.keys():
            self._przestrzen_nazw[mkey]=[]
        self._przestrzen_nazw[mkey].append(mval)

# Druga klasa zapasowa, ale przed implementacją trzeba sprawdzić, czy przy otwieraniu praestrzeń nazw się uzupełni,
#bo wydaje mi się, że źle tam zaimplementowałem - mianowicie główna instrukcja jest w tamtym skrypcie i  odwołuje się
#tylko do prostych metod klasy Generator

class G:
    def __init__(self):
        self._przestrzen_nazw = {}

    def nazwa(self,name):
        if name not in self._przestrzen_nazw.keys():
            self._przestrzen_nazw[name] = self.gen(name)
        return next(self._przestrzen_nazw[name])
    def gen(self,name,start=0):
        num = itertools.count(start)
        while True:
            yield name+str(next(num))




