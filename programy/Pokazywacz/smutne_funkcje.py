def motion(event, pos_label):#todo flag_motion motion powtórzony
    x, y = event.x, event.y
    pos_label.config(text='x={}; y={}'.format(x, y))
    return x, y


def check_str_or_int(fun):
    def inside_check(obj, arg, *tags):
        if type(arg) == int:
            fun(obj, arg, *tags)
        elif type(arg) == str:
            fun(obj, obj.get_num_by_name(arg), *tags)
        else:
            raise TypeError('must be str, or int')

    return inside_check


def przyciaganie(x, y, przestrzen, main_menu):  # użyj tutaj funkcji map()
    magn_list = przestrzen.list_of_magnet_val
    zakres = przestrzen.zakres
    flag = None
    temp = None
    if len(przestrzen.przestrzen_dict) != 0:
        for key in przestrzen.przestrzen_dict.keys():
            for elem in przestrzen.get_free_kwd(key, 'magnet_points').keys():
                if magn_list[elem][0] == 1:
                    for n in przestrzen.get_free_kwd(key, 'magnet_points')[elem]:
                        wspolrzedne = przyciaganie_podstawa(x, y, n[0], n[1], zakres)
                        if wspolrzedne[0] != x:
                            if flag is None:
                                flag = wspolrzedne[2]
                                temp = wspolrzedne
                                z=n[2]
                            else:
                                if flag > wspolrzedne[2]:
                                    flag = wspolrzedne[2]
                                    temp = wspolrzedne
                                    z=n[2]
        if flag is not None:
            main_menu.z_button.config(text=z)
            main_menu.obiekt_canvas.z_coord = z
            return temp[0], temp[1]
    return x, y


def przyciaganie_podstawa(x, y, x_przyciagajace, y_przyciagajace, zakres):
    bolx1 = bool(x + zakres > x_przyciagajace)
    bolx2 = bool(x - zakres < x_przyciagajace)
    if bolx1 and bolx2:
        boly1 = bool(y + zakres > y_przyciagajace)
        boly2 = bool(y - zakres < y_przyciagajace)
        if boly1 and boly2:
            suma_kwadratow = ((x - x_przyciagajace) * (x - x_przyciagajace) + (y - y_przyciagajace) * (
                    y - y_przyciagajace))
            return [x_przyciagajace, y_przyciagajace, suma_kwadratow]
        else:
            return x, y
    else:
        return x, y


def only_straight(x_pocz, y_pocz, x, y):
    if abs(x_pocz - x) >= abs(y_pocz - y):
        y = y_pocz
    else:
        x = x_pocz
    return [x, y]


def butt_grid_org(*names, vertical=True):
    """Organise button bars
    Return list of tuple, which contanins name of button, and position in grid,
    if vertical is True returns buttons in one column, else in one row
    :param
    names : str
        names of buttons
    vertical : bool
        direction of button bar
    :return
    two level list
        [[name1,row,column],...[name99, row, column]]"""
    tmp_bool = all(tuple(map(lambda x: True if type(x) is str else False, names)))  # validate if all names strings
    if tmp_bool is False:
        raise TypeError('wszystnkie nazwy przycisków muszą być typu str')
    else:
        tmp_tup = []
        n = 0
        for el in names:
            tmp_inner = [el, n, 0]
            if not vertical:
                tmp_inner[1], tmp_inner[2] = tmp_inner[2], tmp_inner[1]
            n += 1
            tmp_tup.append(tmp_inner)
    return tmp_tup
