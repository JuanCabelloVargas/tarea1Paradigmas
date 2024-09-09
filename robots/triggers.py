from abc import ABC, abstractmethod


class Trigger(ABC):
    @abstractmethod
    def check(self, robot, eventvalue):
        ...


class EnergyTrigger(Trigger):
    def __init__(self, event_value) -> None:
        self.event_value = event_value
        super().__init__()
    
    def check(self, robot):
        if robot.get_energy() <= self.event_value:
            return True
        return False
    ...

    def apply_effect(self):
        ...
