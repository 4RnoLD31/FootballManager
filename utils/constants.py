import os
import re
import tkinter as tk
from tkinter import ttk


class Toplevel(tk.Toplevel):
    def __init__(self):
        super().__init__()

    def custom_geometry(self, string):
        numbers = re.findall(r"\d+", string)
        index = 0
        while index < len(numbers):
            if index == 0 or index == 2:
                numbers[index] = int(width(numbers[index]))
            else:
                numbers[index] = int(height(numbers[index]))
            index += 1
        if len(numbers) == 2:
            super().geometry(f"{numbers[0]}x{numbers[1]}")
        elif len(numbers) == 4:
            super().geometry(f"{numbers[0]}x{numbers[1]}+{numbers[2]}+{numbers[3]}")


class Tk(tk.Tk):
    def __init__(self):
        super().__init__()

    def custom_geometry(self, string):
        numbers = re.findall(r"\d+", string)
        index = 0
        while index < len(numbers):
            if index == 0 or index == 2:
                numbers[index] = int(width(numbers[index]))
            else:
                numbers[index] = int(height(numbers[index]))
            index += 1
        if len(numbers) == 2:
            super().geometry(f"{numbers[0]}x{numbers[1]}")
        elif len(numbers) == 4:
            super().geometry(f"{numbers[0]}x{numbers[1]}+{numbers[2]}+{numbers[3]}")


class Canvas(tk.Canvas):
    def __init__(self, window, **kwargs):
        kwargs["font"] = font(kwargs["font"])
        if "width" in kwargs:
            kwargs["width"] = width(kwargs["width"])
        if "height" in kwargs:
            kwargs["height"] = width(kwargs["height"])
        if "wraplength" in kwargs:
            kwargs["wraplength"] = width(kwargs["wraplength"])
        if "wrapheight" in kwargs:
            kwargs["wrapheight"] = height(kwargs["wrapheight"])
        super().__init__(window, kwargs)


class Checkbutton(tk.Checkbutton):
    def __init__(self, window, **kwargs):
        kwargs["font"] = font(kwargs["font"])
        if "wraplength" in kwargs:
            kwargs["wraplength"] = width(kwargs["wraplength"])
        if "wrapheight" in kwargs:
            kwargs["wrapheight"] = height(kwargs["wrapheight"])
        super().__init__(window, kwargs)

    def custom_place(self, **kwargs):
        if "x" in kwargs:
            kwargs["x"] = width(kwargs["x"])
        if "y" in kwargs:
            kwargs["y"] = height(kwargs["y"])
        if "width" in kwargs:
            kwargs["width"] = width(kwargs["width"])
        if "height" in kwargs:
            kwargs["height"] = width(kwargs["height"])
        super().place(kwargs)


class Combobox(ttk.Combobox):
    def __init__(self, window, **kwargs):
        kwargs["font"] = font(kwargs["font"])
        if "wraplength" in kwargs:
            kwargs["wraplength"] = width(kwargs["wraplength"])
        if "wrapheight" in kwargs:
            kwargs["wrapheight"] = height(kwargs["wrapheight"])
        super().__init__(window, kwargs)

    def custom_place(self, **kwargs):
        if "x" in kwargs:
            kwargs["x"] = width(kwargs["x"])
        if "y" in kwargs:
            kwargs["y"] = height(kwargs["y"])
        if "width" in kwargs:
            kwargs["width"] = width(kwargs["width"])
        if "height" in kwargs:
            kwargs["height"] = width(kwargs["height"])
        super().place(kwargs)


class Radiobutton(tk.Radiobutton):
    def __init__(self, window, **kwargs):
        kwargs["font"] = font(kwargs["font"])
        if "wraplength" in kwargs:
            kwargs["wraplength"] = width(kwargs["wraplength"])
        if "wrapheight" in kwargs:
            kwargs["wrapheight"] = height(kwargs["wrapheight"])
        super().__init__(window, kwargs)

    def custom_place(self, **kwargs):
        if "x" in kwargs:
            kwargs["x"] = width(kwargs["x"])
        if "y" in kwargs:
            kwargs["y"] = height(kwargs["y"])
        if "width" in kwargs:
            kwargs["width"] = width(kwargs["width"])
        if "height" in kwargs:
            kwargs["height"] = width(kwargs["height"])
        super().place(kwargs)


class Button(tk.Button):
    def __init__(self, window, **kwargs):
        kwargs["font"] = font(kwargs["font"])
        if "wraplength" in kwargs:
            kwargs["wraplength"] = width(kwargs["wraplength"])
        if "wrapheight" in kwargs:
            kwargs["wrapheight"] = height(kwargs["wrapheight"])
        super().__init__(window, kwargs)

    def custom_place(self, **kwargs):
        if "x" in kwargs:
            kwargs["x"] = width(kwargs["x"])
        if "y" in kwargs:
            kwargs["y"] = height(kwargs["y"])
        if "width" in kwargs:
            kwargs["width"] = width(kwargs["width"])
        if "height" in kwargs:
            kwargs["height"] = width(kwargs["height"])
        super().place(kwargs)


class Entry(tk.Entry):
    def __init__(self, window, **kwargs):
        kwargs["font"] = font(kwargs["font"])
        if "wraplength" in kwargs:
            kwargs["wraplength"] = width(kwargs["wraplength"])
        if "wrapheight" in kwargs:
            kwargs["wrapheight"] = height(kwargs["wrapheight"])
        super().__init__(window, kwargs)

    def custom_place(self, **kwargs):
        if "x" in kwargs:
            kwargs["x"] = width(kwargs["x"])
        if "y" in kwargs:
            kwargs["y"] = height(kwargs["y"])
        if "width" in kwargs:
            kwargs["width"] = width(kwargs["width"])
        if "height" in kwargs:
            kwargs["height"] = width(kwargs["height"])
        super().place(kwargs)


class Label(tk.Label):
    def __init__(self, window, **kwargs):
        kwargs["font"] = font(kwargs["font"])
        if "wraplength" in kwargs:
            kwargs["wraplength"] = width(kwargs["wraplength"])
            print(1)
        if "wrapheight" in kwargs:
            kwargs["wrapheight"] = height(kwargs["wrapheight"])
        super().__init__(window, kwargs)

    def custom_place(self, **kwargs):
        if "x" in kwargs:
            kwargs["x"] = width(kwargs["x"])
        if "y" in kwargs:
            kwargs["y"] = height(kwargs["y"])
        if "width" in kwargs:
            kwargs["width"] = width(kwargs["width"])
        if "height" in kwargs:
            kwargs["height"] = width(kwargs["height"])
        super().place(kwargs)


def resize():
    main_window.custom_geometry(f"{int(main_window.winfo_screenwidth() * 0.83)}x{int(main_window.winfo_screenheight() * 0.74)}+{int(main_window.winfo_screenwidth() * 0.083)}+{int(main_window.winfo_screenheight() * 0.1064)}")


def font(object):
    if type(object) == str:
        size = int(object.replace("MiSans ", ""))
        size = int(size * main_window.winfo_screenwidth() / 1920)
        return f"MiSans {size}"
    else:
        return (object[0], int(int(object[1]) * main_window.winfo_screenwidth() / 1920))


def width(size):
    return int(size) * main_window.winfo_screenwidth() / 1920


def height(size):
    return int(size) * main_window.winfo_screenheight() / 1080


def nothing():
    return None


def clear(list=None):
    for widget in main_window.winfo_children():
        try:
            if widget["text"] != "FOOTBALL MANAGER" or not isinstance(widget, tk.Menu):
                if list is None:
                    widget.destroy()
                elif widget not in list:
                    widget.destroy()
        except:
            pass


main_window = Tk()


def text_on_center(text, font, window=main_window):
    clear()
    label = Label(window, text=text, font=font, wraplength=1600)
    label.custom_place(relx=0.5, rely=0.5, anchor="center")
    return label


game_loaded = False
PL1 = None
PL2 = None
next_player = None
number = None
after_saving = False
working_directory = os.path.abspath(os.curdir).replace("utils", "")
used_in_video = {}
queue = []
version = "0.0.5 ALPHA"
date_of_build = "11/29/2023 9:22 PM"
sum = 0

errorcodes = {0: "Значение превышает 20 символов или равно 0",
              1: "В клубе есть футболист/тренер/менеджер",
              2: "Футболист/тренер мертв/болеет/забастовка",
              3: "Футболист болеет",
              4: "Недостаточно средств",
              5: "Нет доступных клубов",
              6: "Битое сохранение",
              7: "Невозможно загрузить сохранение во время игры",
              8: "Файл configs/database.cfg битый",
              9: "Нет файлов сохранения",
              10: "Неверный путь сохранения"}

gradual_income = [300000, 500000, 1000000, 2000000]

fines = {"Money": 9, "Dead": 2, "Strike": 2, "Coronavirus": 3}
bonuses = {"Money": 9, "Transfer Window": 2, "Vaccine": 2, "Revive": 1, "Charity Match": 1}

money_fines = {3000000: 2, 1500000: 3, 750000: 4}
money_bonuses = {1500000: 2, 1000000: 3, 500000: 4}

clubs = {}
TVs = {}
footballers = {}
coaches = {}
managers = {}

sheikh_level = {}
former_footballer_level = {}
economist_plus_level = {}
economist_minus_level = {}
