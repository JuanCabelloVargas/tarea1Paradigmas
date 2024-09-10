

class Skill:
    def __init__(self, name , trigger , duration , effect, objective, effect_value):
        self.name = name
        self.trigger = trigger
        self.duration = duration
        self.effect = effect
        self.objective = objective
        self.effect_value = effect_value
        self.active_turns = 0

        self.effect_functions = {
            'shield': self._apply_shield,
            'steroids': self._apply_steroids,
            'hawk': self._apply_hawk,
            'shifting': self._apply_shifting,
            'fast recharge': self._apply_fast_recharge,
            'magic': self._apply_magic
        }

    def activate(self,robot):
        self.active_turns = self.duration

    def check_and_activate(self, robot, attack=None):
        if self.trigger.check_trigger(robot, attack):
            print(f"DEBUG: Trigger de {self.name} activado en {robot.get_name()}")
            self.activate(robot)
        else:
            print(f"DEBUG: Trigger de {self.name} NO activado en {robot.get_name()}")

    def apply_effect(self, robot, attack=None):
        if self.active_turns > 0:
            if self.effect in self.effect_functions:
                print(f"DEBUG: Aplicando el efecto {self.effect} en {robot.get_name()} con valor {self.effect_value}.")
                return self.effect_functions[self.effect](robot,attack)
        return attack.get_damage()    
            
    def _apply_shield(self, robot, attack): 
        print("-----------------ejecutando trigger shield==============================")       
        return attack.get_damage() * (1 - self.effect_value / 100)

    def _apply_steroids(self, robot, attack):
        print("-----------------ejecutando trigger steroids==============================")       
        return attack.get_damage() * (1 + self.effect_value / 100)

    def _apply_hawk(self, robot, attack):
        print("-----------------ejecutando trigger hawk==============================")
        return attack.get_precision() * (1 + self.effect_value / 100)

    def _apply_shifting(self, robot, attack):
        print("-----------------ejecutando trigger shifting==============================")
        return attack.get_precision() * (1 - self.effect_value / 100)

    def _apply_fast_recharge(self, robot, attack):       
        attack.current_recharge = 0
        print("-----------------ejecutando trigger fast recharge==============================")
        return attack.get_damage()

    def _apply_magic(self, robot, attack=None):        
        robot.current_energy += self.effect_value
        robot.current_energy = min(robot.base_energy, robot.current_energy)
        print("-----------------ejecutando trigger magic==============================")
        return robot.current_energy
