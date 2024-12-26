"""importowany przez wielu, nie potrzebuje nikogo
tablice obiektow z ktorych można odtwożyć cały wygląd planszy"""


class WrongLenghtException(Exception):
    """Neasted element has wrong lenght. Should be exactly 2"""
    pass


class AccesDenied(Exception):
    pass


class PrzestrzenObiektow:

    def __init__(self):
        self.__przestrzen_dict = {}
        self.__zakres = 40
        self.__list_of_magnet_val = {'konce': [1, 0], 'srodki': [1, 1], 'centrum': [1, 2]}  # [priorytet, status]
        self.__magnet_points = True
        self.__straight = False

    def inspect_main(self):
        print("Liczba obiektów na planszy:", len(self.__przestrzen_dict))
    def inspect_det(self):
        for key in self.__przestrzen_dict:
            print(key, end=' :')
            print('\npunkty charakterystyczne', end=': ')
            for mg in self.przestrzen_dict[key][1]['magnet_points']:
                print(mg, end=': ')
                print(self.przestrzen_dict[key][1]['magnet_points'][mg], end='; ')
            print('\ntagi:',end=' ')
            for tg in self.przestrzen_dict[key][1]['tagi']:
                print(tg, end='; ')
            print('')
            print('')



    @property
    def zakres(self):
        return self.__zakres

    @zakres.setter
    def zakres(self, arg):
        if type(arg) is (int or float):
            self.__zakres = arg
        else:
            print('Zły argument. Musi być int lub float')

    @property
    def list_of_magnet_val(self):
        return self.__list_of_magnet_val

    @property
    def przestrzen_dict(self):
        return self.__przestrzen_dict

    def podmien(self, new_dict):
        self.__przestrzen_dict=new_dict
    @property
    def magnet_points(self):
        return self.__magnet_points

    @property
    def straight(self):
        return self.__straight

    @straight.setter
    def straight(self, new_val):
        self.__straight = new_val

    @magnet_points.setter
    def magnet_points(self, new_val):
        self.__magnet_points = new_val

    def dodawanie_do_przestrzeni(self, obiekt, nazwa, **kwargs):
        """Forma przechowywania w przestrzeni:(
            obiekt, nazwa_obiektu, magnet_points={
                'konce': [(),()], 'srodki': [(),()]}
                )
                """
        self.przestrzen_dict[nazwa] = [obiekt, kwargs]

    def del_elem(self, name):
        self.__przestrzen_dict.pop(name)

    def add_free_kwd(self, name, kwd, item):
        self.__przestrzen_dict[name][1][kwd] = item

    def del_free_kwd(self, name, kwd, ):
        self.__przestrzen_dict[name][1].pop(kwd)

    def get_free_kwd(self, name, kwd, ):
        """name = NameOrNumber"""
        return self.__przestrzen_dict[name][1][kwd]

    def add_tags(self, name, *tags):
        """Add tags
        """
        for arg in tags:
            if type(arg) is not str:
                raise TypeError('tag must be str')
        if 'tagi' not in self.__przestrzen_dict[name][1].keys():
            self.__przestrzen_dict[name][1]['tagi'] = []
        for tg in tags:
            self.__przestrzen_dict[name][1]['tagi'].append(tg)

    def add_prop(self,name_obj,name,val):
        name = str(name)
        self.__przestrzen_dict[name_obj][1]['property'][name]=val

    def del_tags(self, name, *tags):
        """Delete tags
        """
        for arg in tags:
            if type(arg) is not str:
                raise TypeError('tag must be str')
        if 'tagi' not in self.__przestrzen_dict[name][1].keys():
            raise KeyError('object has no tags')
        for tg in tags:
            index = self.get_free_kwd(name, 'tagi').index(tg)
            if index != (0 and 1 and 2):
                self.__przestrzen_dict[name][1]['tagi'].remove(tg)
            else:
                raise AccesDenied("""you're tying delate default tags name or type. Acction forbbiden""")

    def all_withtag(self, tag: str):
        """return list of num elements with tag"""
        tagged = []
        for num, elem in enumerate(self.__przestrzen_dict):
            if tag in elem[2]['tagi']:
                tagged.append(num)
        return tagged

    def przyblizanie(self):
        pass

    def obroty(self):
        pass


def priority_change(lista, change_elem, priority):
    for elem in lista:
        if elem[1] == priority:
            (change_elem[1], elem[1]) = ([elem[1], change_elem[1]])
            return 0
    print('brak takiego priorytetu')


def sort_priority_list(lis):
    """sortuje litę wg priorytetów, gdzie lista jest w postaci[[a,b],]
    a priorytet jest wartością b.
    Jeśl ipierwsza cyfra to 0, usuwa z listy jako wyłączony.
    Na poz 2 podaje oryginalną pozycję elmentu"""
    lista = [ele[:] for ele in lis]
    for elem in lista:
        for val in elem:
            if not isinstance(val, int):
                raise TypeError
        if len(elem) != 2:
            raise WrongLenghtException
        elif not isinstance(elem, list):
            raise TypeError
        elem.append(lista.index(elem))
    lista.sort()
    for elem in lista:
        if elem[0] != 0:
            breaking = lista.index(elem)
            break
    lista = lista[breaking:]
    return lista
