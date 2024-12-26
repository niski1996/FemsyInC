"""
Zawiera klasy `MainWindowForce` i `FactorEntry`, ktore nadpisują
program `Pokazywacz` do kształtu odpowiadającego zastosowaniu metody
współczynnika gęstości sił
"""
from programy.Pokazywacz.main_menu_by_tkinter import *
from programy.Ruler.force_handler.prepare_data import Conector



class MainWindowForce(MainWindow):
    def button_bars(self):
        super().button_bars()
        self.add_factor()
        self.butt_dest()
        self.add_and_mod()


    def butt_dest(self):
        x = self.ctr_left.winfo_children()
        x[2].destroy()
        x[3].destroy()
        self.modyfikuj_container.destroy()
        self.test_container.destroy()

    def add_and_mod(self):
        self.z_button = Button(self.ctr_right, text=self.obiekt_canvas.z_coord, width=10,
                               command=lambda: FactorEntry(self.z_button, self.obiekt_canvas, 'z_coord',
                                                                  entry_width=6))
        self.z_button.grid(row=3, column=0, columnspan=2)
        self.przyciski_rysuj = smutne_funkcje.butt_grid_org('punkt', 'linia', 'właściwości_r',
                                                       'wymaż')
        self.factor_button = Button(self.ctr_right, text='wspólczynnik', width=10,
                                    command=lambda: butt_entry.Checker(self.factor_button, self.obiekt_canvas, 'factor',
                                                                       entry_width=6))
        self.factor_button.grid(row=4, column=0, columnspan=2)
    def add_factor(self,*args):
        self.obiekt_canvas.factor = 1 #defaultowo
        def nadpis(fun,menu):
            def clos(self):
                fun(self)
                menu.przestrzen.add_prop(self.nazwa,'factor', menu.obiekt_canvas.factor)
            return clos
        Line.dodawanie= nadpis(Line.dodawanie,self)
    def down(self):
        super().down()
        create = Button(self.btm_frame, text = 'policz', command = lambda: Conector(self.przestrzen.przestrzen_dict,root = self.window))
        create.grid(row=0, column = 3)



class FactorEntry(butt_entry.Checker):
    def approved(self,e,ok):
        try:
            super().approved(e,ok)
        except ValueError:
            if e.get() == 'None':
                self.button.config(text='None')
                e.destroy()
                ok.destroy()
                self.overrite(None)






if __name__ == '__main__':
    x=MainWindowForce()
    mainloop()


