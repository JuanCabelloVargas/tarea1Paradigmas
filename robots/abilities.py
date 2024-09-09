from robots.triggers import Trigger

class Ability:
    def __init__(self, name:str, trigger:Trigger, duration:int, objective:str, effect:str, effect_value, trigger_value:int =None) -> None:
        self.ability_name = name
        self.trigger = trigger
        self.duration = duration
        self.objective = objective
        self.effect = effect
        #self.effect_value = effect_value if type(effect_value) == int else None
        #Will this works? It should hahaha
        #self.effect_type, self.effect_value = (None, effect_value) if type(effect_value) == int else effect_value.split(':')
        self.current_duration = 0
        self.active = False
        self.trigger_value = trigger_value
        if type(effect_value) == int:
            self.effect_extent, self.effect_value = None, effect_value
        else:
            self.effect_extent, self.effect_value = effect_value.split(':')
    
    def check_trigger(self, robot, event_type:str, trigger_value:int=None) -> None:
        if self.trigger.check(robot, trigger_value):
            ...
    
    def activate(self):
        self.current_duration = self.duration
        self.active = True
        ...
    
    def deactive(self):
        self.active = False
    
    def get_specs(self) -> str:
        return f"Ability name: {self.ability_name}\n\nTrigger: {self.trigger}\nTrigger value: {self.trigger_value}\nObjective: {self.objective}\nDuration: {self.duration}\nEffect: {self.effect}\nEffect value: {self.effect_value}\nEffect extension: {self.effect_extent}"
    
    def get_description(self) -> str:
        return self.ability_name
    ...
    def update_duration(self) -> None:
        if self.current_duration > 0:
            self.current_duration -= 1
            if self.current_duration == 0:
                self.deactive()
    
    def apply(self, robot):
        if self.active:
            if self.effect == "regenerate":
                robot.current_energy += self.effect_value
        ...

    def is_active(self) -> bool:
        return self.active
