import numpy as np

import biblioteki.area.trian
from programy.mes_obliczenia_1_2.wyjatki_i_checki import check_równości_pierdolonych_list as chck
import biblioteki.vectors.vect_math as mat
from programy.mes_obliczenia_1_2.procesor.shape_fun.elem1d.bar import shape_fun_1d as shape_bar
from programy.mes_obliczenia_1_2.procesor.shape_fun.elem2d.shield import shape_fun_2d as shape_shield
from programy.mes_obliczenia_1_2.funkcje_pomocnicze import dodaj_zera, dodaj_z
from programy.mes_obliczenia_1_2.szybkie_do_zmiany import deriv_shield


def cos_mat_set(*nodes):
    """

    :param nodes:
    :return:
    """
    node1=np.array(nodes[0])
    node2=np.array(nodes[1])
    vers1=(node2-node1)/np.linalg.norm(node2-node1)
    for nod in nodes[2:]:
        vers2=(nod-node1)/np.linalg.norm(nod-node1)
        if not chck(vers2,vers1):
            return mat.lin_base_2vec(vers1,vers2)
    return mat.lin_base(vers1)

def set_volume(type_elem, nodes, material):
    """
    counts volume depend of type element

    :param type_elem:
    :param nodes:
    :param material:
    :return:
    """
    if type_elem in ('bar', 'beam'):
        lenght=0
        v1=nodes[0]
        for nod in nodes[1:]:
            lenght+=np.linalg.norm(np.array(v1)-np.array(nod))
            v1=nod
        return  lenght*material[1]
    elif type_elem in ('shield','plate','slab','surface'):
        area = biblioteki.area.trian.sur_area_by_points(*nodes)
        return area*material[3]
    else:
        raise ValueError('złą wartość')

def set_area(el_type, **kwargs):
    if el_type in ('bar', 'beam'):
        return kwargs['material'][1]
    elif el_type in ('shield','plate','slab','surface'):
        area = biblioteki.area.trian.sur_area_by_points(*kwargs['elem_loc'])
        return area

def set_length(el_type, elem):
    if el_type in ('bar', 'beam'):
        return abs(elem[0][0]-elem[1][0])

def set_shape_fuu(el_type, nodes, values):
    """
    count shape function of elements

    :param el_type:
    :param nodes:
    :param values:
    :return:
    """
    if el_type == 'bar':
        return shape_bar(nodes,values)
    elif el_type== 'shield':
        return shape_shield(nodes,values)
    elif el_type== 'surface':
        return shape_shield(nodes,values)
    elif el_type == 'plain':
        pass
    else:
        raise ValueError('zła wartość')


def set_deriv_matr(el_type,n_matr):
    """

    :param el_type: str
    :param n_matr:
    :return:
    """
    li=[]
    if el_type=='bar':
        for pol in n_matr[0]:
            li.append(pol.deriv())
        return np.array(li).reshape(1,len(li))
    elif el_type== 'shield':
        return deriv_shield(n_matr)
    elif el_type== 'surface':
        return deriv_shield(n_matr)
    else:
        raise ValueError('złą wartość')

def stif(el_type,**kwargs):
    if el_type == 'bar':
        return kwargs['ea']*kwargs['l']*np.array([[1]])
    elif el_type == 'shield':
        return kwargs['d']*kwargs['v']
    elif el_type == 'plain':
        pass
    elif el_type == 'surface':
        return kwargs['d']*kwargs['v']

def extend_local_k(el_type, k_matr):
    """
    extend matrix from local style of notation into 3d with or without torque
    :param el_type:
    :param k_matr:
    :return:
    """
    if el_type in ('bar'):
        return dodaj_zera(k_matr,2)
    elif el_type == 'shield':
        # return k_matr
        return dodaj_z(k_matr)
    elif el_type == 'surface':
        return k_matr

def remove_prop_form_matr(el_type, matr, **kwargs):
    if el_type in ('bar'):
        return matr/kwargs('length')