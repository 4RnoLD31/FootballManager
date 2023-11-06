from utils.constants import errorcodes
from tkinter import messagebox


def error(errorcode):
    text = f"Ошибка {errorcode}: {errorcodes[errorcode]}"
    messagebox.showerror(title=f"Ошибка {errorcode}", message=text)
