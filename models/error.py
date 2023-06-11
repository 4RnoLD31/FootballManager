from utils.constants import errorcodes, main_window, clear
from tkinter import messagebox


class Error:
    def __init__(self, errorcode):
        self.errorcode = errorcode
        clear()
        self.text = "Ошибка " + str(self.errorcode) + ": " + errorcodes[self.errorcode]
        self.error = messagebox.showerror(title="Ошибка " + str(self.errorcode), message=self.text)
