from competition.competition_main import Competition, Robot
from competition.comp_menus import *
from battle import *

class TeamCreationTool:
    def __init__(self, r_dict:dict) -> dict:
        self.robots = r_dict
        self.team = None
    def create(self):
        while True:
            if self.team == None:
                #print("\nSeleccione un robot\n")
                menu = TeamName()
                name = menu.run_menu()
                menu = TeamSelection(self.robots, name)
                self.team = menu.get_select()
                print(f"El equipo '{self.team['name']}' ha sido creado.\nPresiones 'enter' para continuar." if self.team != None else "Parametro no valido.\nPresione 'enter' para continuar.")
            else:
                break
        return self.team