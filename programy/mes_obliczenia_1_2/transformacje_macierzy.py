import numpy as np

from biblioteki.vectors.vect_math import lin_base, lin_base_2vec


def transform(type_elem, nodes):
    """wybiera metodę transformacji do lokalnego ukłądu współrzednyvh dal jednego elementu

    Params
    --------
    type : str
        typ elementu skończonego. Może być 'bar'
    *nodes : array_like, shape (n,3)
        współrzędne węzłów w układzie globalnym (x, y, z)

    Return
    ------
    tuple, shape (n,3)
        współrzedne w nowym układzie
    numpy.ndarray, shape(3,3)
        macierz cosinusów kierunkowych przejscia
    """

    if type_elem == 'bar':
        return transformacja_bar(nodes)
    elif type_elem == 'shield':
        return transformacja_shield(nodes)


def transformacja_bar(nodes):
    """transformuje wezły do układu lokalnego

    taransformuje węzły do ukłądu w którym oś x jest wyznaczona
    przez wektor łączący dwa pierwsze węzły z nodes. Pozostałe
    osie pryjmują dowolne ułożenie. Ukłąd prawoskrętny

    Params
    --------
    *nodes : array_like, shape (n,3)
        współrzędne węzłów w układzie globalnym (x, y, z)

    Return
    ------
    list, shape (n,3)
        współrzedne w nowym układzie
    numpy.ndarray, shape(3,3)
        macierz cosinusów kierunkowych przejscia   """
    vect = np.array(nodes[1]) - np.array(nodes[0])
    a_cos = lin_base(vect)
    nodes = list(nodes)
    for num in range(len(nodes)):
        nodes[num] = np.matmul(a_cos, nodes[num])
    return nodes, a_cos


def transformacja_shield(nodes):
    """transformuje wezły do układu lokalnego w trzywęzłowej tarczy

    taransformuje węzły do ukłądu w którym oś x jest wyznaczona
    przez wektor łączący dwa pierwsze węzły z nodes.
    Wektor y przez pierwszy i trzeci węzeł

    Params
    --------
    *nodes : array_like, shape (3,3)
        współrzędne węzłów w układzie globalnym (x, y, z)

    Return
    ------
    list, shape (3,3)
        współrzedne w nowym układzie
    numpy.ndarray, shape(3,3)
        macierz cosinusów kierunkowych przejscia   """
    if len(nodes) != 3:
        raise TypeError('obsługuje tylko elementy trójkątne')
    vect_x = np.array(nodes[1]) - np.array(nodes[0])
    vect_y = np.array(nodes[2]) - np.array(nodes[0])
    a_cos = lin_base_2vec(vect_x, vect_y)
    nodes = list(nodes)
    for num in range(len(nodes)):
        nodes[num] = np.matmul(a_cos, nodes[num])
    return nodes, a_cos


