import random

# Our creations
from robots.robot_menus import AttackMenu, UserInput
from robots.skills import Skill
from robots.attack import Attack






class Robot:
    def __init__(self, name: str, energy: int, skills=None) -> None:
        self.name = name
        self.base_energy = energy
        self.current_energy = 0
        self.attacks = {}
        self.skills = skills if skills is not None else []
        self.turns_passed = 0 
        self.unique_name = None
        pass

    def add_attack(self, attack_name: str, attack_type: str, objective: str, damage: int, precision: int, recharge: int) -> None:
        self.attacks[attack_name] = Attack(attack_name, attack_type, objective, damage, precision, recharge)
    
    def add_skill(self, skill):
        self.skills.append(skill)

    def get_name(self) -> str:
        return self.name
    
    def get_energy(self) -> int:
        return self.current_energy
    
    def reset_energy(self) -> None:
        self.current_energy = self.base_energy
    
    #Not used 
    def receive_damage(self, damage: int) -> None:
        if damage is not None:
            self.current_energy -= damage
        else:
            print(f"ERROR: El valor del daño recibido es None en {self.name}")
    
    def receive_attack(self, attack:Attack) -> int:
        self.current_energy -= attack.get_damage()
        for skill in self.skills:
            skill.check_activate(self, attack)
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
    
    # For manual mode | Not used
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
        sel_at = AttackMenu.get_menu(self.name, available_attack_keys, not_available, battle)
        if sel_at in available_attack_keys and not battle:
            print(self.attacks[sel_at].get_specs())
            UserInput.get_input()
        elif battle:
            if sel_at in available_attack_keys:
                return self.attacks[sel_at]
            else:
                input("Ataque no esta disponible. Presione enter y seleccione denuevo.")
                return self.attack_selection()
    
    def set_unique_name(self, name:str):
        self.unique_name = name
    
    def get_unique_name(self):
        return self.unique_name



    def next_turn(self) -> None:
        self.turns_passed += 1
        for skill in self.skills:
            if skill.active_turns > 0:
                skill.active_turns -= 1 
    