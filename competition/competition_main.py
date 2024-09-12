import random
from abc import ABC, abstractmethod

#Only used for reference, 'Robot' objects aren't created here
from robots.robot_obj import Robot 


class Competition(ABC):
    def __init__(self, robots):
        #iterate robot objects
        self.robots = list(robots.values())
        self.results = {robot.get_name(): {'victorias': 0, 'derrotas': 0} for robot in self.robots}

    def register_results(self, winner, loser):
        self.results[winner.get_name()]['victorias'] += 1
        self.results[loser.get_name()]['derrotas'] += 1
    @abstractmethod
    def play(self):
        ...
    @classmethod 
    @abstractmethod
    def get_description(cls) -> str:
        return
    
    def ask_battle_mode(self):
        """Pregunta al jugador si desea jugar en modo manual o automático"""
        while True:
            mode = input("¿Deseas jugar en modo manual o automático? (Escribe 'manual' o 'auto'): ").strip().lower()
            if mode in ["manual", "auto"]:
                return mode
            else:
                print("Entrada inválida. Por favor, escribe 'manual' o 'auto'.")

