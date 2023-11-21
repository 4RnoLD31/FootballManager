import tkinter as tk
import utils.constants as const


class AllObjects:
    def __init__(self, type):
        self.type = type
        self.window = tk.Toplevel()
        self.window.geometry("600x880")
        self.window.resizable(False, False)
        self.text = ""
        if self.type == "Footballers":
            for element in const.footballers:
                self.text += f"{const.footballers[element].name} - {const.footballers[element].power}\n"
            self.l_label = tk.Label(self.window, text=self.text, font="MiSans 14", wraplength=600)
        elif self.type == "Coaches":
            self.window.geometry("600x800")
            for element in const.coaches:
                self.text += f"{const.coaches[element].name} - {const.coaches[element].power}\n"
            self.l_label = tk.Label(self.window, text=self.text, font="MiSans 26", wraplength=600)
        elif self.type == "Managers":
            self.window.geometry("600x430")
            for element in const.managers:
                self.text += f"{const.managers[element].name} - {const.managers[element].type}\n"
            self.l_label = tk.Label(self.window, text=self.text, font="MiSans 25", wraplength=600)
        self.l_label.pack()


class ChangeBalance:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.resizable(False, False)
        self.window.geometry("500x250")
        self.l_p1 = tk.Label(self.window, text=f"{const.PL1.name} {const.PL1.balance}", font="MiSans 20")
        self.l_p1.place(x=0, y=20)
        self.l_p2 = tk.Label(self.window, text=f"{const.PL2.name} {const.PL1.balance}", font="MiSans 20")
        self.l_p2.place(x=0, y=100)
        self.f_p1 = tk.Entry(self.window, font="MiSans 20")
        self.f_p1.place(x=100, y=20, width=220)
        self.b_p1 = tk.Button(self.window, text="Confirm", font="MiSans 20", command=self.__change_pl1__)
        self.b_p1.place(x=340, y=15, height=50)
        self.f_p2 = tk.Entry(self.window, font="MiSans 20")
        self.f_p2.place(x=100, y=100, width=220)
        self.b_p2 = tk.Button(self.window, text="Confirm", font="MiSans 20", command=self.__change_pl2__)
        self.b_p2.place(x=340, y=95, height=50)

    def __change_pl1__(self):
        self.balance_pl1 = int(self.f_p1.get())
        const.PL1.balance = self.balance_pl1

    def __change_pl2__(self):
        self.balance_pl2 = int(self.f_p2.get())
        const.PL2.balance = self.balance_pl2
