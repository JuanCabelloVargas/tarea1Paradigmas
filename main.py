import json
import random

'''
"name": "lanza de hielo",
"type": "sword",
"objective": "team",
"damage": 25,
"precision": 80,
"recharge": 2
'''

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
        if self.recharge > 0:
            self.recharge -= 1

    def set_recharge(self) -> None:
        self.current_recharge = self.recharge

    def is_available(self) -> bool:
        return True if self.recharge == 0 else False
    
    def get_description(self):
        return self.attack_name

    

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
    
    def receive_damage(self, damage: int) -> None:
        self.current_energy -= damage
    
    def get_move(self) -> Attack:
        available_attack_keys = [aname for aname, attack in self.attacks.items()
                           if attack.is_available()]
        selection = random.choice(available_attack_keys)
        return self.attacks[selection]
    
    def get_attacks_list(self):
        text = ""
        for i, at in enumerate(self.attacks.items()):
            #print(at)
            text += f"({i}) {at[1].get_description()}\n"
        return f"{self.name} attacks:\n\n{text}"


class RobotGame:
    def __init__(self) -> None:
        self.robots = {}
        pass

    def load_robots(self, filename) -> None:
        with open(filename, 'r') as f:
            data = json.load(f)
            #Now data is a dictionary
            for rb in data["robots"]:
                self.robots[rb['name']] = Robot(rb['name'], rb['energy'])
            
            print("\nRobotsloaded\nAdding attacks...\n")
            
            for rb in data['robots']:
                if 'attacks' in rb:
                    for at in rb['attacks']:
                        self.robots[rb['name']].add_attack(at['name'], at['type'], at['objective'], at['damage'], at['precision'], at['recharge'])
                    print("")
                print(self.robots[rb['name']].get_attacks_list())
            print("\nAttacks added\n")
            #print(self.robots)



    def start(self):
        
        pass


g1 = RobotGame()
g1.load_robots("robots01.json")
    

