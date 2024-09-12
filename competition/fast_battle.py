from competition.competition_main import Competition, Robot
from competition.comp_menus import *
from battle import *

class SingleFastBattle(Competition):
    #This part is for selection and config 
    def __init__(self, robots: dict[str, Robot]):
        #super().__init__()
        self.robots = robots
        #super().__init__(robots)
        # super command returns a list for robost variable
    
    def play(self):
        self._config()
        battle = SoloBattle(self.player, self.enemy)
        battle.auto_mode()

        ...
    
    def _config(self):
        self.player = None
        self.enemy = None
        while True:
            if self.player == None:
                print("\nSeleccione un robot\n")
                menu = RobotSelectionIstantiable(self.robots)
                print(menu.get_menu())
                self.player = menu.get_select()
                print(f"{self.player.get_name()} ha sido seleccionas.\nPresiones 'enter' para continuar." if self.player != None else "Parametro no valido.\nPresione 'enter' para continuar.")
            if self.enemy == None:
                print("\nSeleccione su enemigo\n")
                menu = RobotSelectionIstantiable(self.robots)
                print(menu.get_menu())
                self.enemy = menu.get_select()
                print(f"{self.enemy.get_name()} ha sido seleccionas.\nPresiones 'enter' para continuar." if self.enemy != None else "Parametro no valido.\nPresione 'enter' para continuar.")
            if self.player != None and self.enemy != None:
                break
        
    @classmethod 
    def get_description(cls):
        return "Batalla Rapida (solo)"
    ...