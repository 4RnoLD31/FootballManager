import pickle
import utils.constants
import os
from datetime import date
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
        pickle.dump(data, save_file)
        print("saved")


def load_game():
    with open("save.dat", "rb") as load_file:
        data = pickle.load(load_file)
        print("loaded")
    for element in utils.constants.clubs:
        utils.constants.clubs[element] = data[element]
    for element in utils.constants.footballers:
        utils.constants.footballers[element] = data[element]
    for element in utils.constants.managers:
        utils.constants.managers[element] = data[element]
    for element in utils.constants.coaches:
        utils.constants.coaches[element] = data[element]
    for element in utils.constants.TVs:
        utils.constants.TVs[element] = data[element]
    utils.constants.PL1 = data["PL1"]
    utils.constants.PL2 = data["PL2"]
    utils.constants.next_player = data["Next Player"]
    utils.constants.working_directory = data["Working Directory"]