from abc import ABC, abstractmethod


class Trigger(ABC):
    @abstractmethod
    def check_trigger(self, robot, attack=None):
        ...

class EnergyTrigger(Trigger):
    def __init__(self, threshold):
        self.threshold = threshold

    def check_trigger(self, robot, attack=None):
        return robot.current_energy < self.threshold

class AttackTypeTrigger(Trigger):
    def __init__(self, attack_type):
        self.attack_type = attack_type

    def check_trigger(self, robot, attack):
        return attack.attack_type == self.attack_type
    
class AttackTeamTrigger(Trigger):
    def __init__(self, attack_target):
        self.attack_target = attack_target

    def check_trigger(self, robot, attack):
        print(f"DEBUG: Verificando trigger de equipo: el objetivo del ataque es {attack.objective}, buscando {self.attack_target}")
        return attack.objective == self.attack_target


class TurnsTrigger(Trigger):
    def __init__(self, turns):
        self.turns = turns

    def check_trigger(self, robot, attack=None):      
        print(f"DEBUG: Verificando trigger de turnos: {robot.get_name()} ha pasado {robot.turns_passed} turnos, buscando {self.turns}")
        return robot.turns_passed >= self.turns
