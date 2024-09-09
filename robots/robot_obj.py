import random

# Our creations
from robots.robot_menus import AttackMenu, AbilitiesMenu
from robots.triggers import Trigger


'''
{
    "name": "cortina de agua",
    "trigger": "attack_team",
    "duration": 1,
    "objective": "team",
    "effect": "shifting",
    "effect_value": 20
}
'''

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



class Attack:
    def __init__(self, attack_name: str, attack_type: str, objective: str, damage: int, precision: int, recharge: int) -> None:
        self.attack_name = attack_name
        self.attack_type = attack_type
        self.objective = objective
        self.damage = damage
        self.precision = precision 
        self.recharge = recharge
        self.current_recharge = 0
        
    
    def get_damage(self) -> int:
        return self.damage
    
    def get_precision(self) -> int:
        return self.precision
    
    def get_recharge(self) -> int:
        return self.recharge
    
    def update_recharge(self) -> None:
        if self.current_recharge > 0:
            self.current_recharge -= 1

    def set_recharge(self) -> None:
        self.current_recharge = self.recharge

    def is_available(self) -> bool:
        return True if self.current_recharge == 0 else False
    
    def get_description(self):
        return self.attack_name
    
    def get_specs(self):
        return f"Attack name: {self.attack_name}\n\nType: {self.attack_type}\nObjective: {self.objective}\nDamage: {self.damage}\nPrecision: {self.precision}\nRecharge: {self.recharge}"



class Robot:
    def __init__(self, name: str, energy: int) -> None:
        self.name = name
        self.base_energy = energy
        self.current_energy = 0
        self.attacks = {}
        pass

    def add_attack(self, attack_name: str, attack_type: str, objective: str, damage: int, precision: int, recharge: int) -> None:
        self.attacks[attack_name] = Attack(attack_name, attack_type, objective, damage, precision, recharge)
    
    def get_name(self) -> str:
        return self.name
    
    def get_energy(self) -> int:
        return self.current_energy
    
    def reset_energy(self) -> None:
        self.current_energy = self.base_energy
    
    #Not used 
    def receive_damage(self, damage: int) -> None:
        self.current_energy -= damage
    
    def receive_attack(self, attack:Attack) -> int:
        self.current_energy -= attack.get_damage()
        return self.current_energy
        ...

    #Retorna un ataque al azar entre los disponibles
    def get_move(self) -> Attack:
        available_attack_keys = [aname for aname, attack in self.attacks.items()
                           if attack.is_available()]
        selection = random.choice(available_attack_keys)
        # agregar contador de ataque
        self.attacks[selection].set_recharge()
        return self.attacks[selection]
    
    def get_attack(self, name: str) -> Attack:
        return self.attacks[name]
    
    @property
    def is_alive(self) -> bool:
        return True if self.current_energy > 0 else False
    
    # For manual mode
    def select_attack(self, battle=True) -> Attack:
        text = ""
        while True:
            for i, at in enumerate(self.attacks.items()):
                #print(at)
                text += f"({i}) {at[1].get_description()}\n"
            opt = input(f"{self.name} attacks:\n\n{text}")
            if opt.isnumeric() and int(opt) in list(range(1, len(self.attacks.items()) + 1)):
                selected_attack = list(self.attacks.keys())[int(opt)]
                return self.get_attack(selected_attack)
            else:
                input("Seleccione una opcion valida.\nPresione 'enter' para continuar\n>")
            
    
    def get_attacks_list(self) -> str:
        text = ""
        for i, at in enumerate(self.attacks.items()):
            #print(at)
            text += f"({i}) {at[1].get_description()}\n"
        return f"{self.name} attacks:\n\n{text}"
    
    def update_attacks_recharge(self):
        for k, at in self.attacks.items():
            at.update_recharge()
        pass


    def attack_selection(self, battle=True) -> Attack:
        not_available = [aname for aname, attack in self.attacks.items() if not attack.is_available()]
        available_attack_keys = [aname for aname, attack in self.attacks.items() if attack.is_available()]
        AttackMenu().get_menu(self.name, available_attack_keys, not_available, battle)
        ...

    