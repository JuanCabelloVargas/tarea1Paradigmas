from competition.competition_main import Competition, Robot
from competition.comp_menus import *
from battle import *
from competition.team_selection import TeamCreationTool

class TeamsFastBattle(Competition):
    #This part is for selection and config 
    def __init__(self, robots: dict[str, Robot]):
        #super().__init__()
        self.robots = robots
        #super().__init__(robots)
        # super command returns a list for robost variable
    
    def play(self):
        self._config()
        while True:
            print('Menu batalla rapida por equipos:\n\n1. Ver equipos y miembros\n2. Comenzar batalla\n3. Volver al menu principal')
            opt = UserInput.get_input()
            if opt == '1':
                self.show_teams()
            elif opt == '3':
                break
            else:
                print("Opcion no valida. Presione 'enter' para continuar.")
                UserInput.get_input()
            


        #battle = SoloBattle(self.player, self.enemy)
        #battle.auto_mode()

        ...
    
    def _config(self):
        self.player_team = None
        self.enemy_team = None
        while True:
            if self.player_team == None:
                print("\nCree su equipo:\n")
                menu = TeamCreationTool(self.robots)
                self.player_team = menu.create()
            if self.enemy_team == None:
                print("\nCree su equipo enemigo:\n")
                menu = TeamCreationTool(self.robots)
                self.enemy_team = menu.create()
                
            if self.player_team != None and self.enemy_team != None:
                break
    
    def show_teams(self):
        if self.player_team != None and self.enemy_team != None:
            print(f"Seleccione un equipo para visualizar:\n1- {self.player_team['name']}\n2-{self.enemy_team['name']}")
            opt = UserInput.get_input()
            if opt == '1':
                print(GetTeamDescription.get_menu(self.player_team))
            elif opt == '2':
                print(GetTeamDescription.get_menu(self.enemy_team))
            else:
                print("Opcion no disponible.")
                UserInput.get_input()
        else:
            print("No hay equipos que mostrar.")
        
    @classmethod 
    def get_description(cls):
        return "Batalla Rapida por Equipos"
    ...