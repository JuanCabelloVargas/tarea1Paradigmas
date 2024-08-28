from abc import ABC, abstractmethod

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
    def get_stats(self):
        ...
