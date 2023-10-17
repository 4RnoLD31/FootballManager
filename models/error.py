from utils.constants import errorcodes, main_window, clear
from tkinter import messagebox


def error(errorcode):
        errorcode = errorcode
        clear()
        text = "Ошибка " + str(errorcode) + ": " + errorcodes[errorcode]
        error = messagebox.showerror(title="Ошибка " + str(errorcode), message=text)
