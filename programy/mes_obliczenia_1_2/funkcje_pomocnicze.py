import itertools
import numpy as np
from programy.mes_obliczenia_1_2.wyjatki_i_checki import full_check
import numbers


def agreg_dostosowania(loc, dim, *nodes):  # TODO ryzyko przepełnienia macierzy, kontroluj liczbę węzzłów
    """powiększa macierz loc o dowolnej liczbie węzłów, do wymiaru dim, wstawiając zera

    Parametry
    ----------
    loc : numpy.ndarray
        macierz węzłów w ukłądzie lokalnym
    dim : int
        oczekiwany wymiar macierzy wynikowej
    *nodes : int
        kolejne węzły numerowane globalnie
        UWAGA! węzły numerowane od 0


    Zwraca
    -------
    numpy.ndarray
        macierz o kwadratową o wymiarze dim i wartościach z macierzy loc
        rozstawionych w sposób odpowiadający węzłom. Pozostałe elementy przyjmują
        wartość 0
    """
    #todo array2D_2 = 4*np.ones([6,6])  a=agreg_dostosowania(array2D_2,12,0,1,2,4) print(a) niewykryty błąd

    if len(nodes) == 2:
        node1, node2 = nodes
        return lokalne_dostosowanie(loc, node1, node2, dim)
    elif len(nodes) > 2:
        glob = np.zeros((dim, dim))
        li, node_pos = explode(loc, nodes)
        for num, elem in enumerate(li):
            temp = lokalne_dostosowanie(elem, node_pos[num][0][0], node_pos[num][1][0], dim)
            glob = add_control(glob, temp)
        return glob
    else:
        raise ValueError('zbyt mało węzłów')


def add_control(a, b):
    """dodaje macierze pomijając elem. na przęk. głownej a, jeżeli elem. na przek. b są niezerowe

    Parametry
    ---------
    a,b : numpy.ndarray
        macierze do dodawania

    Zwraca
    -------
    numpy.ndarray
        zmodyfikowana suma macierzy

    Uwagi
    -------
        elementy na przekątnej głównej powtarzają się w kazdej macierzy
        składowej, więc trzeba kontrolować przekątną, żęby się nie multiplikowały
    """
    rows, cols = np.shape(a)
    for rw in range(rows):
        for cl in range(cols):
            if (a[rw][cl] != 0) and (b[rw][cl] != 0):
                b[rw][cl] = 0
    return a + b


def explode(mlocal, nodes):
    """rozbija macierz local, na listę macierzy

    Parametry
    ---------
    local : numpy.ndarray
        macierz węzłów w ukłądzie lokalnym dla dowolnej liczby węzłów
    nodes : list
        lista numerów węzłów

    Zwraca
    -------
    numpy.ndarray
        zmodyfikowana suma macierzy

    Uwagi
    o
    -------"""
    node_pos_li = n_pos(nodes)
    wym = np.shape(mlocal)[1] / len(nodes)
    li = []
    for comb in node_pos_li:
        loc_nod = []
        for a in range(int(wym)):
            loc_nod.append(int(comb[0][1]*wym + a))
            loc_nod.append(int(comb[1][1]*wym + a))
        loc_nod.sort()
        temp = mlocal[np.ix_(loc_nod, loc_nod)] # ciekawa linijka, np.ix_bierze n list jednowymiarowych i
        # zwraca n list n wymiarowych, gdzie wszystkie indeksy oprócz jednego przyjmują wartość 1.
        # ten wspomniany przyjmuje len(n-ta lista). Kazda lista ma wspomniany wymiar na innej pozycji.
        li.append(temp)
    return li, node_pos_li


def n_pos(nodes, b=2):
    """zwraca wszystkie b-elementowe kombinacje elementów nodes z pierwotnymi pozycjami

     Parametry
     -----------
     nodes : list
        lista elementów
    b : str
        ilosć elementów w kombinacji

    Zwraca
    --------
    list
        lista kombinacji - każdy element listy zawiera zbiór elementów tuple,
        które zawierają numer z nodes i jego oryginalną pozycję
    """

    a = [(node, num) for num, node in enumerate(nodes)]
    return list(itertools.combinations(a, b))


def lokalne_dostosowanie(loc, node1, node2, dim):
    """powiększa macierz loc o dwóch węzłąch, do wymiaru dim, wstawiając zera

    Parametry
    ----------
    loc : numpy.ndarray
        macierz węzłów w ukłądzie lokalnym
    node1, node2 : int
        numery węzłów odpowiadających w ukłądzie globalnym
    dim : int
        oczekiwany wymiar macierzy wynikowej

    Zwraca
    -------
    numpy.ndarray
        macierz o kwadratową o wymiarze dim i wartościach z macierzy loc
        rozstawionych w sposób odpowiadający węzłom. Pozostałe elementy przyjmują
        wartość 0
    """

    # full_check(loc, node1, node2, dim)# todo wyłączone, bo przy dużych wartosciach wchodzi błąd numeryczny
    dof = int(loc.shape[1] / 2)
    glob = np.zeros((dim, dim))
    nodes = (node1, node2)
    li = [(0, 0), (0, dof), (dof, 0), (dof, dof)]
    for n1 in nodes:
        for n2 in nodes:
            a, b = li.pop(0)
            glob[int(n1 * dof):int(n1 * dof + dof), int(n2 * dof):int(n2 * dof + dof)] = loc[a:a + dof, b:b + dof]
    return glob


def swich_num_to_coords(elem, nodes):
    """zamienia numery wezłów w elementach na ich współrzędne

    Params:
    ------
    nodes : array_like,
        tablica węzłów
    elem : numpy.ndarray
        macierz elementów

    Return
    -------
    list
        tablica współrzednych wezłów w ukłądzie globalnym
        lista trzypoziomowa [[(xn,yn,zn),(xm,ym,zm)...],
                            [(),()...],...]
    """
    mac_wsp = []
    for el in elem:
        mac_wsp.append([nodes[int(el[ind])] for ind in range(len(el)-2) ])
    return mac_wsp


def elem_len(nodes):
    len_li = []
    for e in nodes:
        r1 = e[0] - e[1]
        len_li.append(np.linalg.norm(r1))
    return len_li


def dodaj_zera(mat, add_dim):
    """ za każdym elementem mat dodaje dim kolumn i wierszy zerowych

    :param
    ------
    mat: array_like,shape(n,m)
        dowolna dwuwymiarowa macierz
    add_dim : int
        liczba dodatkowych kolumn i wierszy zerowych

    :return
    ------
    numpy.array, shape(n*add_dim, m*add_dim)
    """
    li = []
    for num, e in enumerate(mat):
        li.append([])
        for e1 in e:
            li[num].append(e1)
            for num1 in range(add_dim):
                li[num].append(0)
    li1 = []
    lng = len(li[0])
    for n in range(len(mat)):
        li1.append(li[n])
        for e1 in range(add_dim):
            li1.append([0 for e2 in range(lng)])
    return np.array(li1)


def dodaj_z(mat):
    li=list(range(2,len(mat)+2,2))
    li.pop()
    li.reverse()
    mat = np.c_[mat, np.zeros(len(mat))]
    mat = np.r_[mat, np.zeros((1, len(mat) + 1))]
    for el in li:
        mat=np.insert(mat,el,0,axis=1)
        mat=np.insert(mat,el,0,axis=0)


    return mat


def one_nodes_matr_part(derx,dery,derz):
    """
    pomooznicza do tworzenia macierzy b.
    tworzy część macierzy dla jednego węzła
    :param derx:
    :param dery:
    :param derz:
    :return:
    """
    return np.array([[derx,0,0],
                     [0,dery,0],
                     [0,0,derz],
                     [dery,derx,0]])

def macierz_przylegania(elem_li,dof):
    con=[]
    for elem in elem_li:
        tmp=np.zeros([(len(elem)-2)*dof,12])
        n = 0
        for num,nod in enumerate(elem[:-2]):
            i=0
            while n<=dof*(num+1)-1:
                tmp[n][nod*dof+i]=1
                n+=1
                i+=1
        con.append(tmp)
    return con


def swich_poly(elem):
    """
    swich poly with degree 0 to float
    :param elem:
    :return:
    """
    if isinstance(elem, numbers.Number):
        return elem
    else:
        try:
            if elem.degree() == 0:
                return (float(elem.coef))  # skoro jest stopnia 0, to jedyny wspołczynnik jest tez wartoscia
            else:
                raise TypeError("łoooo, panie, całka, to bedzie płatne ekstra")
        except IndexError:
            return 0