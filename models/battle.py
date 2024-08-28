from abc import ABC, abstractmethod
from robot import Robot


class Battle(ABC):
    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def auto_mode(self):
        ...
    
    @abstractmethod
    def manual_mode(self):
        ...
    
    @abstractmethod
    def get_history(self):
        ...



