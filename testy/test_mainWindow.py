"""gówno, ale tylko taki pomysł miałem"""""
#dla linii
def main(main_menu,tag):
    """Sprawdza czy ilość linii na planszy jest równa ilości linii
    w przestrzeni obiektów, i czy współrzędne się zgadzają"""
    list_of_us_coor=[]
    canvas=main_menu.canvas
    x=canvas.find_withtag(tag)
    li=map(canvas.coords, x)
    for object in main_menu.przestrzen.przestrzen_obiektow:
        if tag in object[2]['tagi']:
            coord=[float(coo) for tup in object[2]['magnet_points']['konce'] for coo in tup ]
            list_of_us_coor.append(coord)
    # if len(list_of_us_coor) != len(list(li)):
    #     raise AssertionError
    #powoduje wyczyszczenie obiektu map
    for a in li:
        if a in list_of_us_coor:
            list_of_us_coor.remove(a)
    assert len(list_of_us_coor)==0
    print('Wykonano Test Zgodności Linii')





