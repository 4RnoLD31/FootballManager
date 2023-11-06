import utils.constants
from tkinter import *


class AllObjects:
    def __init__(self, type):
        self.type = type
        self.window = Toplevel()
        self.window.geometry("600x880")
        self.window.resizable(False, False)
        self.text = ""
        if self.type == "Footballers":
            for element in utils.constants.footballers:
                self.text += f"{utils.constants.footballers[element].name} - {utils.constants.footballers[element].power}\n"
            self.l_label = Label(self.window, text=self.text, font="MiSans 14")
        elif self.type == "Coaches":
            self.window.geometry("600x800")
            for element in utils.constants.coaches:
                self.text += f"{utils.constants.coaches[element].name} - {utils.constants.coaches[element].power}\n"
            self.l_label = Label(self.window, text=self.text, font="MiSans 26")
        elif self.type == "Managers":
            self.window.geometry("600x430")
            for element in utils.constants.managers:
                self.text += f"{utils.constants.managers[element].name} - {utils.constants.managers[element].type}\n"
            self.l_label = Label(self.window, text=self.text, font="MiSans 25")
        self.l_label.pack()


class ChangeBalance:
    def __init__(self):
        self.window = Toplevel()
        self.window.resizable(False, False)
        self.window.geometry("500x250")
        self.l_p1 = Label(self.window, text=f"{utils.constants.PL1.name} {utils.constants.PL1.balance}", font="MiSans 20")
        self.l_p1.place(x=0, y=20)
        self.l_p2 = Label(self.window, text=f"{utils.constants.PL2.name} {utils.constants.PL1.balance}", font="MiSans 20")
        self.l_p2.place(x=0, y=100)
        self.f_p1 = Entry(self.window, font="MiSans 20")
        self.f_p1.place(x=100, y=20, width=220)
        self.b_p1 = Button(self.window, text="Confirm", font="MiSans 20", command=self.__change_pl1__)
        self.b_p1.place(x=340, y=15, height=50)
        self.f_p2 = Entry(self.window, font="MiSans 20")
        self.f_p2.place(x=100, y=100, width=220)
        self.b_p2 = Button(self.window, text="Confirm", font="MiSans 20", command=self.__change_pl2__)
        self.b_p2.place(x=340, y=95, height=50)

    def __change_pl1__(self):
        self.balance_pl1 = int(self.f_p1.get())
        utils.constants.PL1.balance = self.balance_pl1

    def __change_pl2__(self):
        self.balance_pl2 = int(self.f_p2.get())
        utils.constants.PL2.balance = self.balance_pl2
