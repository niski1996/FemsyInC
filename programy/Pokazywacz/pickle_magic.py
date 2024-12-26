import pickle
from tkinter import filedialog
import sys
sys.path.append('C:\\Users\\Karol\\PycharmProjects\\projekt_ostateczny\\programy\\Pokazywacz') #dodaje sciezke dla starych danych




path = None


def save(main_menu):
    """zapisuje przestrzen obiektow do pliku .pickle"""
    przestrzen = main_menu.przestrzen.przestrzen_dict
    for keys in przestrzen:
        przestrzen[keys][0] = None
    file = filedialog.asksaveasfile(mode='wb', filetypes=(("pickle files", "*.pickle"), ("all files", "*.*")),
                                    defaultextension='.pickle')
    if not file:
        return
    else:
        pickle.dump(przestrzen, file)
    file.close()


def open_fil(main_menu):
    file = filedialog.askopenfile(mode='rb', filetypes=(("pickle files", "*.pickle"), ("all files", "*.*")),
                                  defaultextension='.pickle')
    przestrzen = pickle.load(file, encoding="UFT-8")
    file.close()
    main_menu.obiekt_canvas.clear_canvas()
    my_canvas = main_menu.canvas
    for keys in przestrzen:
        tmp = przestrzen[keys][1]
        if 'linia' in tmp['tagi']:
            main_menu.generator.add_val('linia',keys)
            my_canvas.create_line(tmp['magnet_points']['konce'][0][0],
                               tmp['magnet_points']['konce'][0][1],
                               tmp['magnet_points']['konce'][1][0],
                               tmp['magnet_points']['konce'][1][1],
                               dash=tmp['property']['przerywana'],
                               fill=tmp['property']['kolor'],
                               width=tmp['property']['grubosc'],
                               tags=tmp['tagi']
                               )
        elif 'punkt' in tmp['tagi']:
            main_menu.generator.add_val('punkt', keys)
            grubosc = tmp['property']['grubosc']
            x,y = tmp['magnet_points']['konce'][0][0],tmp['magnet_points']['konce'][0][1]

            my_canvas.create_oval((x - grubosc, y - grubosc,
                                     x + grubosc, y + grubosc),
                                    fill=tmp['property']['kolor'], tags=tmp['tagi'])

    main_menu.przestrzen.podmien(przestrzen)

