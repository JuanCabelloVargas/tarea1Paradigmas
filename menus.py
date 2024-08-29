# nada de esto esta implementado, ni siquiera esta terminado el "diseño"
# Python packages
from abc import ABC, abstractmethod

# Program specific packages
from battle import *



class Menu(ABC):
   @abstractmethod
   @classmethod
   def get_menu(cls) -> str:
       ... 

# Que va qui? no lo se 
class MainMenu(Menu):
    @abstractmethod
    @classmethod
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
    ...

