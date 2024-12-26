import numpy as np


def matr_to_diag2(mat, i=2):
    """tworzy macierz i razy więksą niż mat, gdzie powielone mat leży na przekątnej


    :param
    mat_cos : numpy.array, shape(n,m)
        macierz transformacji

    :return
    numpy.array, sahpe(2*n,2*m)
        [[mat_cos, zeros],[zeros,mat_cos]]
    """
    n, m = np.shape(mat)
    r,v=n,m
    m_c_2_nodes = np.zeros([i * n, i * m])
    a = 0
    b = 0
    for num in range(i):
        m_c_2_nodes[a:r, b:v] = mat
        a+=n
        b+=m
        r+=n
        v+=m
    return m_c_2_nodes

def matr_to_diag(mat, i=2):

    """
    NOWE

    tworzy macierz i razy więksą niż mat, gdzie powielone mat leży na przekątnej


    :param
    mat_cos : numpy.array, shape(n,m)
        macierz transformacji

    :return
    numpy.array, sahpe(2*n,2*m)
        [[mat_cos, zeros],[zeros,mat_cos]]
    """
    n, m = np.shape(mat)
    r,v=n,m
    m_c_2_nodes = np.zeros([i * n, i * m])
    a = 0
    b = 0
    for num in range(i):
        m_c_2_nodes[a:r, b:v] = mat
        a+=n
        b+=m
        r+=n
        v+=m
    # m_c_2_nodes=np.delete(m_c_2_nodes,(2,5,8),axis=0)
    return m_c_2_nodes


def reduce_matrix(matrix, num=3):
    """ usuwa co n-ty wiersz i kolumnę z macierzy

    :param
    matrix : array_like
        macierz na której pracujemy. Dowolny listowy typ danych
    num : int
        defaultowo usuwa wymiar z

    :return
    list
    """
    temp = []
    for n, e in enumerate(matrix):
        if ((n + 1) % num) != 0:
            temp.append([])
            for n1, e1 in enumerate(e):
                if (n1 + 1) % num != 0:
                    temp[-1].append(e1)
    return temp

def del_with_val(mat, val=0, ax=0):
    """
    Return a new array with sub-arrays with value along an axis deleted.

    :param mat:  array_like
        Input array.
    :param val: float
        value to find
    :param ax: int, optional
        The axis along which to delete the vaues defined by `obj`.
        0 for column, 1 for rows, other for multidimensional array(may not work)
    :return: ndarray
        A copy of `mat` with the elements containing only `val` removed.
    """
    idx = np.argwhere(np.all(mat[..., :] == 0, axis=ax))
    a2 = np.delete(mat, idx, axis=not ax)
    return a2


def del_last_with_val(mat, val=0, ax=0):
    """
    Return a new array with sub-arrays with value along an axis deleted,
    but only if behinde them there's no other subarrays

    :param mat:  array_like
        Input array.
    :param val: float
        value to find
    :param ax: int, optional
        The axis along which to delete the vaues defined by `obj`.
        0 for column, 1 for rows, other for multidimensional array(may not work)
    :return: ndarray
        A copy of `mat` with the elements containing only `val`, and are on the last positions removed.
    """
    idx = np.argwhere(np.all(mat[..., :] == 0, axis=ax))
    last_idx=len(mat)-1
    while last_idx>=0:
        if last_idx in idx:
            last_idx-=1
        else: break
    a2 = np.delete(mat, list(range(last_idx+1,len(mat))), axis=not ax)
    return a2


x=np.array([[1,2,3,0],
          [1,2,4,0]])
del_with_val(x)