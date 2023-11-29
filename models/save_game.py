import os
import datetime
import pickle
import models.field as field
import utils.constants as const
import models.highlighting as hg
import models.error as error
from tkinter import filedialog as fd


def save_game(autosave=True):
    if const.PL1 is None or const.PL2 is None:
        print(hg.failed("Saving is impossible"))
        return
    if autosave:
        if not os.path.exists(f"{const.working_directory}\\saves\\autosave\\{datetime.date.today().strftime('%d.%m.%Y')}"):
            os.mkdir(f"{const.working_directory}\\saves\\autosave\\{datetime.date.today().strftime('%d.%m.%Y')}")
        index = 0
        while True:
            if os.path.exists(f"{const.working_directory}\\saves\\autosave\\{datetime.date.today().strftime('%d.%m.%Y')}\\save{index}.dat"):
                index += 1
            else:
                path = f"{const.working_directory}\\saves\\autosave\\{datetime.date.today().strftime('%d.%m.%Y')}\\save{index}.dat"
                break
    else:
        index = 0
        while True:
            if os.path.exists(f"{const.working_directory}\\saves\\manual\\manual_save{index}.dat"):
                index += 1
            else:
                name = f"manual_save{index}.dat"
                break
        path = fd.asksaveasfilename(defaultextension=".dat", filetypes=[("Сохранение", "*.dat")], initialdir=f"{const.working_directory}\\saves\\manual", initialfile=name, title="Сохранение игры")
        if path == "":
            error.error(10)
            del const.queue[0]
            return
        del const.queue[0]
    with open(path, "wb") as save_file:
        data = {}
        for element in const.clubs:
            data[element] = const.clubs[element]
        for element in const.footballers:
            data[element] = const.footballers[element]
        for element in const.managers:
            data[element] = const.managers[element]
        for element in const.coaches:
            data[element] = const.coaches[element]
        for element in const.TVs:
            data[element] = const.TVs[element]
        data["PL1"] = const.PL1
        data["PL2"] = const.PL2
        data["Queue"] = const.queue
        data["Next Player"] = const.next_player
        data["Number"] = const.number
        pickle.dump(data, save_file)
    print(hg.successful("Game saved"))
    if not autosave:
        field.Field.new_move()

