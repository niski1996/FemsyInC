import numpy as np

def polyval(x,y, c,):
    """
    Evaluate a polynomial at points x,y.

    The parameters `x` and `y` are converted to an array only if they are
    a tuple or a list, otherwise they are treated as a scalar.
    In either case, either `x` and `y` or its elements must support
    multiplication and addition both with themselves and with the elements of `c`.

    `x` and `y` must have the same shape.

     `p(x,y)` will have the same shape as `x` and `y`.

    Trailing zeros in the coefficients will be used in the evaluation, so
    they should be avoided if efficiency is a concern.

    Parameters
    ----------
    x,y : array_like, compatible object
        If `x` and `y` are a list or tuple, they are converted to an ndarray, otherwise
        they are left unchanged and treated as a scalar. In either case, `x` and `y`
        or its elements must support addition and multiplication with
        with themselves and with the elements of `c`.
    c : array_like
        Array of coefficients ordered with PolyXY style.
        To see more check


    Returns
    -------
    values : ndarray, compatible object
        The shape of the returned array is described above.

    See Also
    --------
    polyval2d, polygrid2d, polyval3d, polygrid3d

    Notes
    -----
    The evaluation uses Horner's method.

    Examples
    --------
    >>> from numpy.polynomial.polynomial import polyval
    >>> polyval(1, [1,2,3])
    6.0
    >>> a = np.arange(4).reshape(2,2)
    >>> a
    array([[0, 1],
           [2, 3]])
    >>> polyval(a, [1,2,3])
    array([[ 1.,   6.],
           [17.,  34.]])
    >>> coef = np.arange(4).reshape(2,2) # multidimensional coefficients
    >>> coef
    array([[0, 1],
           [2, 3]])
    >>> polyval([1,2], coef, tensor=True)
    array([[2.,  4.],
           [4.,  7.]])
    >>> polyval([1,2], coef, tensor=False)
    array([2.,  7.])

    """