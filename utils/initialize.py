import utils.constants
from models.club import Club
from models.footballer import Footballer
from models.tv_company import TVCompany
from models.coach import Coach
from models.manager import Manager
from utils.constants import *


def initialize():
    for element in range(len(utils.constants.names_clubs)):
        utils.constants.clubs[utils.constants.names_clubs[element]] = Club(utils.constants.names_clubs[element], utils.constants.prices_clubs[element],
                                                                           utils.constants.leagues_clubs[element], utils.constants.colors_clubs[element],
                                                                           utils.constants.codenames_clubs[element])

    for manager in utils.constants.nt_managers.keys():
        utils.constants.managers[manager] = Manager(manager, utils.constants.nt_managers[manager])

    for coach in utils.constants.name_coaches.keys():
        utils.constants.coaches[coach] = Coach(coach, utils.constants.name_coaches[coach],
                                               utils.constants.pp_coaches[utils.constants.name_coaches[coach]])

    for footballer in utils.constants.name_footballers.keys():
        utils.constants.footballers[footballer] = Footballer(footballer, utils.constants.name_footballers[footballer],
                                                             utils.constants.pp_footballers[
                                                                 utils.constants.name_footballers[footballer]])
    for TV in utils.constants.name_TV:
        utils.constants.TVs[TV] = TVCompany(TV)
