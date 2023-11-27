import pickle
import configparser
import utils.initialize as initialize
import utils.constants as const
import models.field as field
import models.highlighting as hg
import models.error as error


def load_game(auto=True):
    if const.PL1 is not None:
        print(hg.failed("Unable to load the game while playing"))
        error.error(7)
        return 
    try:
        if auto:
            settings_file = configparser.ConfigParser()
            settings_file.read("settings.ini")
            with open(settings_file["Settings"]["latest_autosave"], "rb") as load_file:
                data = pickle.load(load_file)
        for element in const.clubs:
            const.clubs[element] = data[element]
        for element in const.footballers:
            const.footballers[element] = data[element]
        for element in const.managers:
            const.managers[element] = data[element]
        for element in const.coaches:
            const.coaches[element] = data[element]
        for element in const.TVs:
            const.TVs[element] = data[element]
        const.PL1 = data["PL1"]
        const.PL2 = data["PL2"]
        const.queue = data["Queue"]
        const.next_player = data["Next Player"]
        const.working_directory = data["Working Directory"]
        const.number = data["Number"]
        const.game_loaded = data["Game Loaded"]
        print(hg.successful("Game loaded"))
        field.Field.new_move()
    except:
        print(hg.failed("The game wasn't loaded! Broken save"))
        initialize.initialize()
        error.error(6)
