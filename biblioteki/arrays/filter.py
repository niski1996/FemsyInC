import math


def circle_meshgrid(rad, center, x, y):
    """

    :param rad:
    :param center:
    :param x:
    :param y:
    :return:
    """
    for rnum, row in enumerate(x):
        for cnum, col in enumerate(row):
            distance = math.sqrt((x[rnum][cnum] - center[0]) ** 2 + (y[rnum][cnum] - center[1]) ** 2)
            if distance > rad:
                x[rnum][cnum] = None
                y[rnum][cnum] = None