import numpy as np
import itertools
# from programy.FDens import surface_4_poitns


def n_point_surface_polinomial(nodes, usuwany=None):  # usuwany 0y niedozowoliny, tylko 0x
    # w przypadku usuwania należy sprawdzić całka potrójną , bo nwm ktory najlepszy
    matr = []
    z = []
    amount = len(nodes)
    empty_index = None  # potrzebny, ze wzgledu na wartosci zerowe w wierszach przy usuwaniu
    for nod in nodes:
        if amount % 2 == 1:
            power_x, power_y = fuu_x_y(nod[0], nod[1], amount)
        else:
            power_x, power_y = fuu_x_y(nod[0], nod[1], amount, usuwany)
        power_factors = list(
            itertools.chain.from_iterable(list(zip(power_x, power_y))))  # ustawia elementy dwóch list naprzemiennie
        power_factors.pop(-1)
        matr.append(power_factors)
        z.append([nod[2]])
    if amount % 2 == 0:
        ind = int(usuwany[1:])
        empty_index = amount - (ind * 2 - (lambda: 1 if usuwany[0] == 'y' else 0)())
        matr = [list(itertools.chain(rmatr[:empty_index], rmatr[empty_index + 1:])) for rmatr in matr]
    tmp = list(itertools.chain(list(np.linalg.solve(np.array(matr), np.array(z)))))
    tmp = list(itertools.chain.from_iterable(tmp))
    if empty_index is not None:
        tmp.insert(empty_index,
                   0)  # w ten sposób mam wszystkie współczynniki wielomianu, a nie dziure w niewiadomym punkcie
    wolny = tmp.pop(-1)
    return [*tmp[::2],wolny], [*tmp[1::2],wolny]


def fuu_x_y(x_val, y_val, rank, usuwany=None):
    """
    dla f(x,y) zwraca kolejne wartości potęg x i y

    :param x_val: float
        przyjeta wartosc x
    :param y_val:float
        przyjeta wartosc y
    :param rank: int
        ilość jednomianów w równaniu
    :param usuwany: str,
        usuwany[0] is 'x' or 'y', usuwany[1:] is int
        wskaźnik z którego zbioru usówam jaką liczbę, ważny w przypadku prarzystej liczby aproksymowanych punktów.
        Przykłądowo 'x4' znaczy,że x^4=0
    :return: list,list
        tablica wartości x i y od najwyższej potęgi, z wyrazem wolnm na koncu(x^0)
    """
    x_factor = []
    y_factor = []
    if rank % 2 == 0:
        if usuwany is None:
            raise ValueError('Wybierz jednomian do usunięcia')
        for power in range(rank // 2 + 1):
            power_usuw = int(usuwany[1:])
            if power_usuw > (rank // 2):
                raise ValueError('zbyt duża liczba, niema takiej potęgi.')
            if power == power_usuw:
                if usuwany[0] == 'x':
                    x_factor.append(0)
                    y_factor.append(y_val ** power)
                elif usuwany[0] == 'y':
                    y_factor.append(0)
                    x_factor.append(x_val ** power)
                else:
                    raise ValueError(
                        'zły typ usuwanego węzła, pierwsza litera powinna określać wspórzędną \'x\'lub \'y\'')
            else:
                x_factor.append(x_val ** power)
                y_factor.append(y_val ** power)
        return x_factor[::-1], y_factor[::-1]

    else:
        for power in range(rank // 2 + 1):
            x_factor.append(x_val ** power)
            y_factor.append(y_val ** power)
        return x_factor[::-1], y_factor[::-1]

def der_x_y(x_factors,y_factors):
    return np.polyder(x_factors),np.polyder(y_factors)


# if __name__ == '__main__':
#     nodes = np.random.rand(4, 3)
#
#     print(surface_4_poitns(nodes))
#     print(n:=n_point_surface_polinomial(nodes, 'x0'))
#     print(der_x_y(*n))
