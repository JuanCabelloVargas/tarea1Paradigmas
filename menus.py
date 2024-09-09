# nada de esto esta implementado, ni siquiera esta terminado el "diseño"
# Python packages
from abc import ABC, abstractmethod

# Program specific packages
#from battle import *
#from robots import Robot

class UserInput:
    @classmethod
    def get_input(cls):
        return input(">")
        ...

class Menu(ABC):
   @classmethod
   @abstractmethod
   def get_menu(cls):
       ... 

class MainMenu(Menu):
    @classmethod
    def get_menu(cls) -> int:
        text = '''
|------------------------------------------------|
| Super Robot Game (no se me ocurre otro nombre) |
|------------------------------------------------|
| 1. Cargar robots                               |
| 2. Nuevo juego                                 |
| 3. Cargar juego                                |
| 4. Ver robots                                  |
|                                                |
| 5. Salir                                       |
|------------------------------------------------|
'''
        print(text)
        selection = UserInput.get_input()
        return int(selection) if selection.isnumeric() and int(selection) > 0 and int(selection) <= 5 else None


# Que va qui? no lo se 
class MainMenu2(Menu):
    @classmethod
    @abstractmethod
    
    def get_menu(cls) -> str:
        return super().get_menu()

# Seleccion participativo/automatico
class GameModes:
    @classmethod
    def get_menu(cls):
        text = f'''
Participativo
Automatico
'''
        return


# Para modo de juego participativo
class TeamSelection(Menu):
    ...

class RobotSelection(Menu):
    @classmethod
    def get_menu(cls, robots:list[str]) -> str:
        text = "Available Robots\n"
        for i, o in enumerate(robots):
            text += f"{i+1}- {o}\n"
        text += f"\n{len(robots)+1}- Atras\n"
        print(text)
        
        selection = UserInput.get_input()
        return robots[int(selection)-1] if selection.isnumeric() and int(selection)-1 in list(range(len(robots))) else "back" if selection == len(robots) else None
    ...

class RobotAttacks(Menu):
    @classmethod
    def get_menu(cls, robot) -> str:
        text = 'Available attacks:'

        return super().get_menu()
    
    ...

class FileSelection(Menu):
    @classmethod
    def get_menu(cls):
        text = "Enter path/relative path"
        print(text)
        return UserInput.get_input()