"""Wykonuje operacje na przyciskach które potrzebują dostać konkretną wartość liczbową"""
import tkinter as tk
from tkinter import messagebox


class Checker:
    def __init__(self, butt, mobject, mproperty, entry_width=3, mtyp=int):
        """
        :param butt: tkinter button
        :param mobject: object
            object containing mproperty
        :param mproperty: str
            name of changed property by string
        :param entry_width: int
            width of entry window
        :param mtyp: obj
            type type data that property reqired
        """
        self.mtype = mtyp
        self.button = butt
        self.frame = butt.master
        self.entry_width = entry_width
        self.property = mproperty
        self.object = mobject
        self.start()

    def start(self):
        """
        overrite button by entry window and approve button. Original button stil exist beneath
        """
        row, column = self.button.grid_info()['row'], self.button.grid_info()['column']
        e = tk.Entry(self.frame, width=self.entry_width)
        e.grid(row=row, column=column)
        ok = tk.Button(self.frame, text="Ok", command=lambda: self.approved(e, ok))
        ok.grid(row=row, column=column + 1)
        self.frame.bind('<Escape>', lambda event: self.abandon(e, ok))

    def abandon(self,e, ok):
        e.destroy()
        ok.destroy()

    def validate_val(self, val):
        pass

    def approved(self, e, ok):
        """read value from e, change text in self.button, and reveal self.button

        :param e: tkinter entry window
            object should have methods get() and destroy()
        :param ok: tkinter button
            object should have methods get() and destroy()
        """
        temporairy_conainer = e.get()
        if self.mtype is int:
            temporairy_conainer = int(temporairy_conainer)
        if self.mtype is float:
            temporairy_conainer = float(temporairy_conainer)
        self.button.config(text=temporairy_conainer)
        e.destroy()
        ok.destroy()
        self.overrite(temporairy_conainer)

    def overrite(self, val):
        """Overrite value val in field self.property in self.object

        :param val: any
        """
        if self.property in self.object.__dict__.keys():
            self.object.__dict__[self.property] = val
        else:  # backup method if property is @property.
            # In that case key contains class name, so first attempt fail
            prop = (self.property, None)
            work_str = 'self.object.' + prop[0] + '=val'
            exec(work_str)


class CoordsByHand(Checker):

    def validate_val(self, val):
        """Check if entry data are coords"""
        flag = 0
        explode = val.split(';')
        if len(explode) != 2:
            flag = 1
        elif not explode[0].isnumeric():
            flag = 1
        elif not explode[1].isnumeric():
            flag = 1
        if flag:
            messagebox.showerror("error",
                                    "wprowadzone współrzędne powinny być  w płaskim ukłądzie x,y oddzielone znakiem ;\n"
                                    "Przykład: 54;45")
            return False
        return True

    def overrite(self, val):
        class Event:
            def __init__(self, val):
                self.x = int(val[0])
                self.y = int(val[1])

        if self.validate_val(val):
            self.object.temp_method.press(Event(val.split(';')))


if __name__ == "__main__":
    pass
    # def write_slogan():
    #     print("Tkinter is easy to use!")
    #
    #
    # root = tk.Tk()
    # frame = tk.Frame(root)
    # frame.pack()
    # kutas = "dick"
    # button = tk.Button(frame,
    #                    text="QUIT",
    #                    fg="red",
    #                    command=quit)
    # button.grid(row=0, column=1, columnspan=2)
    # slogan = tk.Button(frame,
    #                    text=kutas,
    #                    command=lambda: Checker(slogan, kutas))
    # slogan.grid(row=1, column=1, columnspan=2)
    #
    # root.mainloop()
