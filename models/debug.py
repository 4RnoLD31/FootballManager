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
                self.text += utils.constants.footballers[element].name + " - " + str(utils.constants.footballers[element].power) + "\n"
            self.l_label = Label(self.window, text=self.text, font="MiSans 14")
        elif self.type == "Coaches":
            self.window.geometry("600x800")
            for element in utils.constants.coaches:
                self.text += utils.constants.coaches[element].name + " - " + str(utils.constants.coaches[element].power) + "\n"
            self.l_label = Label(self.window, text=self.text, font="MiSans 26")
        elif self.type == "Managers":
            self.window.geometry("600x430")
            for element in utils.constants.managers:
                self.text += utils.constants.managers[element].name + " - " + str(utils.constants.managers[element].type) + "\n"
            self.l_label = Label(self.window, text=self.text, font="MiSans 25")
        self.l_label.pack()

