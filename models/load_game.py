import os
import pickle
import datetime
from tkinter import filedialog as fd
import utils.initialize as initialize
import utils.constants as const
import models.field as field
import models.highlighting as hg
import models.error as error


class NoSaves(Exception):
    pass


class LoadGame:
    def __init__(self, autosave: bool):
        self.autosave = autosave
        self.exceptions = []
        if const.PL1 is not None:
            print(hg.failed("Unable to load the game while playing"))
            error.error(7)
        else:
            self.__loading__()

    def __search_save__(self):
        self.folders = os.listdir(f"{const.working_directory}\\saves\\autosave")
        self.dates = []
        for element in self.folders:
            try:
                self.dates.append(datetime.datetime.strptime(element, "%d.%m.%Y").strftime('%d.%m.%Y'))
            except:
                pass
        while self.dates:
            self.latest_folder = max(self.dates)
            self.files = os.listdir(f"{const.working_directory}\\saves\\autosave\\{self.latest_folder}")
            while self.files:
                if f"{const.working_directory}\\saves\\autosave\\{self.latest_folder}\\{max(self.files)}" in self.exceptions:
                    self.files.remove(max(self.files))
                    continue
                return f"{const.working_directory}\\saves\\autosave\\{self.latest_folder}\\{max(self.files)}"
            else:
                self.dates.remove(self.latest_folder)
        else:
            return False

    def __loading__(self):
        try:
            if self.autosave:
                self.path = self.__search_save__()
                if not self.path:
                    raise NoSaves()
            else:
                self.path = fd.askopenfilename(initialdir=f"const.working_directory\\saves\\autosave", title="Выберите файл с сохранением", filetypes=[("Сохранение", "*.dat")])
            with open(self.path, "rb") as load_file:
                self.data = pickle.load(load_file)
            for element in const.clubs:
                const.clubs[element] = self.data[element]
            for element in const.footballers:
                const.footballers[element] = self.data[element]
            for element in const.managers:
                const.managers[element] = self.data[element]
            for element in const.coaches:
                const.coaches[element] = self.data[element]
            for element in const.TVs:
                const.TVs[element] = self.data[element]
            const.PL1 = self.data["PL1"]
            const.PL2 = self.data["PL2"]
            const.queue = self.data["Queue"]
            const.next_player = self.data["Next Player"]
            const.working_directory = self.data["Working Directory"]
            const.number = self.data["Number"]
            const.game_loaded = True
            const.after_saving = True
            print(hg.info(f'Save file "{self.path}"'))
            print(hg.successful("Game loaded"))
            field.Field.new_move()
        except NoSaves:
            print(hg.failed("No save files found"))
            initialize.initialize()
            error.error(9)
        except:
            if self.autosave:
                self.__research__()
            else:
                print(hg.failed("The game wasn't loaded! Broken save"))
                initialize.initialize()
                error.error(6)

    def __research__(self):
        self.exceptions.append(self.path)
        self.__loading__()