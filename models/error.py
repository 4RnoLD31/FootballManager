import utils.constants as const
from tkinter import messagebox


def error(errorcode):
    text = f"Ошибка {errorcode}: {const.errorcodes[errorcode]}"
    messagebox.showerror(title=f"Ошибка {errorcode}", message=text)
