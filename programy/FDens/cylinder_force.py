import math

import numpy as np

skrajne = [[0, 1, 2, 3, 4, 5, 6], [28, 29, 30, 31, 32, 33, 34, 35]]
warstwy = np.linspace(11, 45, 35).reshape(5, 7)
warstwy = warstwy.astype('int32')
sila_osiowa = 100
sila_n = 31.1
zakres_x = (100, 800)

miter = [121.48626110689581, 100.0, 139.07704740180986, 196.0163099428192, 100.00000000000009, 258.2649248018864,
         311.7394633193709, 100.0, 338.5638495507936, 450.0000000000002, 100.00000000000003, 366.8888495507935,
         588.2605366806296, 100.00000000000009, 338.56384955079363, 703.9836900571811, 100.00000000000006,
         258.2649248018864, 778.5137388931045, 100.00000000000001, 139.07704740180986, 121.48626110689575, 200.0,
         139.07704740180992, 196.01630994281925, 200.0, 258.2649248018864, 311.7394633193708, 200.0000000000001,
         338.56384955079363, 450.00000000000017, 200.00000000000006, 366.8888495507936, 588.2605366806296,
         200.0000000000001, 338.56384955079375, 703.9836900571812, 200.00000000000006, 258.2649248018865,
         778.5137388931045, 200.00000000000006, 139.0770474018099, 121.48626110689577, 300.0, 139.07704740180992,
         196.0163099428192, 300.0, 258.2649248018865, 311.7394633193708, 300.00000000000006, 338.5638495507937,
         450.0000000000002, 300.00000000000017, 366.8888495507936, 588.2605366806296, 300.00000000000006,
         338.5638495507937, 703.9836900571812, 300.00000000000006, 258.2649248018864, 778.5137388931043, 300.0,
         139.07704740180992, 121.48626110689581, 400.00000000000006, 139.07704740180992, 196.01630994281925,
         400.00000000000006, 258.2649248018865, 311.73946331937077, 400.0000000000001, 338.5638495507938,
         450.0000000000003, 400.00000000000017, 366.8888495507937, 588.2605366806296, 400.00000000000006,
         338.5638495507937, 703.9836900571811, 400.0000000000001, 258.2649248018865, 778.5137388931043, 400.0,
         139.07704740180995, 121.48626110689575, 500.00000000000006, 139.07704740180995, 196.01630994281928,
         500.0000000000001, 258.2649248018864, 311.7394633193709, 500.0000000000002, 338.5638495507938,
         450.0000000000003, 500.00000000000017, 366.88884955079374, 588.2605366806296, 500.0000000000001,
         338.56384955079375, 703.9836900571812, 500.0000000000001, 258.2649248018865, 778.5137388931043, 500.0,
         139.0770474018099]

miter = np.array(miter).reshape(5, 7, 3)


def normal_row(row_nod, strt, end):
    li = [[strt, 0, 0], *row_nod, [end, 0, 0]]
    li_vec = []
    for n in range(len(li) - 2):
        px1 = li[n + 1][0] - li[n][0]
        pz1 = li[n + 1][2] - li[n][2]
        vec1 = np.array([pz1, 0, -px1])
        vers1 = vec1 / np.linalg.norm(vec1)
        px2 = li[n + 2][0] - li[n + 1][0]
        pz2 = li[n + 2][2] - li[n + 1][2]
        vec1 = np.array([pz2, 0, -px2])
        vers2 = vec1 / np.linalg.norm(vec1)
        vec_n = vers2 + vers1
        vers_n = vec_n / np.linalg.norm(vec_n)
        li_vec.append(vers_n)
    return np.array(li_vec)


def f_n_od_x(x, zakres):
    """wersor normalny do połowy okręgu, średnica określona przez 'zakres'"""
    d = zakres[1] - zakres[0]
    r = d / 2
    a = x - zakres[0] - r
    b = math.sqrt(r ** 2 - a ** 2)
    vect = np.array([float(a), 0, float(b)])
    vers = vect / np.linalg.norm(vect)
    return vers * (-1)


def forces1(nodes, scope=zakres_x, fn=sila_n, fax=sila_osiowa, edge=skrajne):
    """

    :param nodes:
    :param fn: float
        normal force
    :param fax: float
        axis force
    :return:
    """
    tmp = np.zeros([nodes, 3])
    xx = np.array([126.6421636, 202.5126266, 316.0607987, 450, 583.9392013, 697.4873734, 773.3578364])

    for num, row in enumerate(tmp):
        idx = np.where(warstwy == num + 11)
        vers = f_n_od_x(xx[idx[1]], scope)
        vect = vers * fn
        row[0] = vect[0]
        row[1] = vect[1]
        row[2] = vect[2]
        if num in edge[0]:
            row[1] = fax
        if num in edge[1]:
            row[1] = -fax
    return tmp


def forces(nodes, scope=zakres_x, fn=sila_n, fax=sila_osiowa, edge=skrajne):
    tmp = normal_row(miter[0], scope[0], scope[1])
    tmp = np.vstack((tmp, tmp, tmp, tmp, tmp)) * fn
    for num, row in enumerate(tmp):
        if num in edge[0]:
            row[1] = fax
        if num in edge[1]:
            row[1] = -fax
    return tmp


if __name__ == '__main__':
    forces()
