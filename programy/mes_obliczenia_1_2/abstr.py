import abc


class DeklaracjaZmiennych(abc.ABC):
    """metaklasa do definiowania klasy MesMain"""

    def __init__(self):
        # coordinates params
        self.nodes = []  # tablica węzłów
        self.initial_disp = [] #początkowe przemieszczenia węzłów
        self.initial_force=[] #początkowe siły w węzłach
        self.initial_deflection = [] #początkowe ugięcia(obroty)
        self.initial_moment = [] #początkowe momenty w węzłąch
        self.node_glob = []  # współrzędne elementów w GUW
        self.elem_loc = []  # współrzędne elemenrów w lokalnym układzie związanym z nimi samymi
        self.cos_oldtonew = []  # macierz przejścia z ukłądu stsrego do nowego
        self.only_nodes = []  # tablica zawierająca tylko węzły

        # elements params
        self.elements = []  # tablica elementów
        self.materials =[] #tablica materiałów
        self.n_loc_element = []  # tablica funkcji kształtu w ukłądzie lokalnym dla wszystkich elementów
        self.k_e_loc = []  # macierz sztywności elementu w ukłądzie lokalnym
        self.k_e_glob = []  # macierz sztywności elementu w układzie globalnym
        self.EA = []
        self.L = []  # długość elementów dla 'bar'
        self.A= [] #powierzchnia elementów dla 'shield'
        self.V = [] #objętość elementów
        self.el_type = None  # typ elementu

        # inne
        self.D = []# macierz sprężystości
        self.k = []  # macierz sztywności
        self.k_mod = []  # macierz sztywności z warunkami brzegowymi
        self.b = []  # pochodna tablicy self.n_loc_element
        self.bond_cond = []  # warunki brzegowe
        self.react = []  # reakcje
        self.forces = []  # siły czynne
        self.dof = None  # liczba stopni swobody

        # Solutions
        self.node_disp = []  # przemiaszczenia węzłów
        self.local_element_stress=[] # naprężenian w elemencie w ukłądzie lokalnym
        self.max_stress=[] #naprężenia główne

        #obsługa programu
        self.version = None  # wersja danych do programu

    def input_val(self, obiekt):
        self.dof = obiekt.dof()
        self.nodes = obiekt.nodes()
        self.initial_disp = obiekt.initial_disp()
        # self.initial_force = obiekt.initial_force()
        self.initial_deflection = obiekt.initial_deflection()  # istnieje tylko jak są jakieś utwierdzenia
        self.initial_moment = obiekt.initial_moment()  # istnieje tylko jak są jakieś utwierdzenia
        self.elements = obiekt.elements()
        self.materials = obiekt.materials()
        self.bond_cond = obiekt.bond_cond()
        self.forces = obiekt.forces()
        self.el_type = self.elements[0][-1]
