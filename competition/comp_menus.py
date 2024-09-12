from menus import Menu, UserInput
from abc import ABC, abstractmethod
#from competition.robot_obj import Robot
import copy


class CompetitionMenu(ABC):
    @abstractmethod
    def get_menu(self) -> str:
        ...

    def get_select(self):
        ...
    
    @classmethod
    @abstractmethod
    def get_description(cls) -> str:
        ...


class RobotSelectionIstantiable(CompetitionMenu):
    def __init__(self, r_dict:dict):
        self.r_dict = r_dict

    def get_menu(self):
        text = ""
        for i, o in enumerate(list(self.r_dict.keys())):
            text += f"{i+1}. {o}\n"
        return text
    
    def get_select(self):
        opt = UserInput.get_input()
        if opt.isnumeric():
            opt = int(opt) -1
            return self.r_dict[list(self.r_dict.keys())[opt]] if opt in list(range(len(self.r_dict.keys()))) else None
        else:
            return self.r_dict[opt] if opt in list(self.r_dict.keys()) else None
    
    
    @classmethod
    def get_description(cls) -> str:
        return "Seleccionar robot"
    


class TeamSelection(CompetitionMenu):
    def __init__(self, r_dict:dict, name) -> None:
        super().__init__()
        self.r_dict = r_dict
        self.team = {"name":name, 
                      "members":{}}
    
    def get_menu(self) -> str:
        text = f"No text here"
        return text
        
    def get_select(self) -> dict:
        #print("Agregue al menos un Robot")
        while True:
            if len(self.team['members']) == 0:
                print("\nDebe agruegar al menos un Robot")
                robot_menu = RobotSelectionIstantiable(self.r_dict)
                print(robot_menu.get_menu())
                robot = robot_menu.get_select()
                if robot != None:
                    self.team['members'][robot.get_name()] = copy.deepcopy(robot)
                else:
                    print("Error")
                ...
            
            if len(self.team['members']) != 0:
                print("Desea agregar otro miembro?\nEscriba si o no.\n")
                opt = UserInput.get_input()
                if opt.lower() in ['y', 'si', 'yes']:
                    robot_menu = RobotSelectionIstantiable(self.r_dict)
                    print(robot_menu.get_menu())
                    robot = robot_menu.get_select()
                    if robot != None:
                        if robot.get_name() in self.team['members'].keys():
                            name = robot.get_name()
                            i = 1
                            while True:
                                if f"{name}{i}" in self.team['members'].keys():
                                    i += 1
                                else:
                                    self.team['members'][f"{name}{i}"] = copy.deepcopy(robot)
                                    break
                            ...
                        else:
                            self.team['members'][robot.get_name()] = copy.deepcopy(robot)
                elif opt in ['n', 'no']:
                    print("Done")
                    break
                else:
                    print("Opcion no disponible")
                    UserInput.get_input()
        return self.team
    
    @classmethod
    def get_description(cls) -> str:
        return "Seleccion de equipo"
    ...

class TeamName(CompetitionMenu):
    def get_menu(self) -> str:
        text = "\nEscribe un nombre para tu equipo"
        return text
    def get_select(self) -> str:
        opt = UserInput.get_input()
        return opt if opt != "" else self.get_select()
    def run_menu(self) -> str:
        print(self.get_menu())
        return self.get_select()
    
    @classmethod
    def get_description(cls) -> str:
        return "Seleccion de nombre del equipo"


class GetTeamDescription:
    @classmethod
    def get_menu(cls, team:dict) -> str:
        text = "-" * 48
        text += f"\n{team['name']} members:\n"
        for i, t in enumerate(team['members'].items()):
            k, o = t
            text += f'''
{i+1}- {k}
Nombre original: {o.get_name()}
Ataques:
{o.get_attacks_list()}
'''
        text += "-" * 48
        return text
        ...
