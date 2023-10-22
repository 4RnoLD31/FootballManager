import os
from datetime import date
import utils.constants
import pickle
from configparser import ConfigParser
from utils.constants import path_to_settings
def save_game(autosave=True):
    if autosave:
        type = "autosave"
    else:
        type = "manual"
    try:
        os.mkdir("saves")
    except:
        pass
    try:
        os.mkdir("saves/" + type)
    except:
        pass
    try:
        os.mkdir("saves/" + type + "/" + date.today().strftime("%d.%m.%Y"))
    except:
        pass
    index = 0
    while True:
        if os.path.exists("saves/" + type + "/" + date.today().strftime("%d.%m.%Y") + "/save" + str(index) + ".dat"):
            index += 1
        else:
            path = "saves/" + type + "/" + date.today().strftime("%d.%m.%Y") + "/save" + str(index) + ".dat"
            break
    with open(path, "wb") as save_file:
        data = {}
        for element in utils.constants.clubs:
            data[element] = utils.constants.clubs[element]
        for element in utils.constants.footballers:
            data[element] = utils.constants.footballers[element]
        for element in utils.constants.managers:
            data[element] = utils.constants.managers[element]
        for element in utils.constants.coaches:
            data[element] = utils.constants.coaches[element]
        for element in utils.constants.TVs:
            data[element] = utils.constants.TVs[element]
        data["PL1"] = utils.constants.PL1
        data["PL2"] = utils.constants.PL2
        data["Next Player"] = utils.constants.next_player
        data["Working Directory"] = utils.constants.working_directory
        data["Game Loaded"] = True
        pickle.dump(data, save_file)
        d_path = {"latest_autosave": path}
        settings_file = ConfigParser()
        settings_file["Settings"] = d_path
        with open(path_to_settings, "w") as file:
            settings_file.write(file)
        print("saved")