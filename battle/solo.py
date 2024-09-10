from battle.battle_main import Battle
import random
import matplotlib.pyplot as plt

#Only for references
from robots import Robot, Attack
from robots.skills import Skill


class SoloBattle(Battle):
    def __init__(self, robot1: Robot, robot2: Robot) -> None:
        self.robot_1 = robot1
        self.robot_2 = robot2
        self.r1_name = robot1.get_name()
        self.r2_name = robot2.get_name()
        self.stats = {'turns':0, 
                      self.r1_name:{'attacks':[], 'energy':0, 'winner':False}, 
                      self.r2_name:{'attacks':[], 'energy':0, 'winner':False}}
        self.robot_1.reset_energy()
        self.robot_2.reset_energy()
    
    def start(self, auto: bool) -> str:
        self.auto_mode = auto
        if self.auto_mode:
            return self.auto_mode()
        ...

    def auto_mode(self) -> tuple[Robot, Robot]:
        self.move_counter = 0
        while self.robot_1.get_energy() > 0 and self.robot_2.get_energy() > 0:            
            attack_1 = self.robot_1.get_move()
            if random.randint(1, 100) <= attack_1.get_precision():          
                for skill in self.robot_2.skills:
                    skill.check_and_activate(self.robot_2, attack_1)

                modified_damage = attack_1.get_damage()
                for skill in self.robot_2.skills:
                    modified_damage = skill.apply_effect(self.robot_2, attack_1)

             
                self.robot_2.receive_damage(modified_damage)
                self.stats['turns'] += 1
                self.stats[self.r1_name]['attacks'].append(attack_1.get_description())
                print(f"\n{self.robot_1.get_name()} realiza {attack_1.get_description()} causando {modified_damage} de daño a {self.robot_2.get_name()}")
                print(f"{self.robot_2.get_name()} ahora tiene {self.robot_2.get_energy()} de energía")

            if self.robot_2.get_energy() <= 0:
                print(f"\n{self.r1_name} ha ganado.")
                self.stats[self.r1_name]['winner'] = True
                self.stats[self.r1_name]['energy'] = self.robot_1.get_energy()
                self.generate_attack_usage_graph()
                return self.robot_1, self.robot_2

          
            attack_2 = self.robot_2.get_move()
            if random.randint(1, 100) <= attack_2.get_precision():
                for skill in self.robot_1.skills:
                    skill.check_and_activate(self.robot_1, attack_2)

              
                modified_damage = attack_2.get_damage()
                for skill in self.robot_1.skills:
                    modified_damage = skill.apply_effect(self.robot_1, attack_2)

           
                self.robot_1.receive_damage(modified_damage)
                self.stats['turns'] += 1
                self.stats[self.r2_name]['attacks'].append(attack_2.get_description())
                print(f"\n{self.robot_2.get_name()} realiza {attack_2.get_description()} causando {modified_damage} de daño a {self.robot_1.get_name()}")
                print(f"{self.robot_1.get_name()} ahora tiene {self.robot_1.get_energy()} de energía")

            if self.robot_1.get_energy() <= 0:
                print(f"\n{self.r2_name} ha ganado.")
                self.stats[self.r2_name]['winner'] = True
                self.stats[self.r2_name]['energy'] = self.robot_2.get_energy()
                self.generate_attack_usage_graph()
                return self.robot_2, self.robot_1

            

    
    def manual_mode(self):
        return super().manual_mode()
    
    def get_stats(self) -> dict:
        return self.stats
        
    def generate_attack_usage_graph(self):
        for robot_name in [self.r1_name, self.r2_name]:
            attacks = self.stats[robot_name]['attacks']
            attack_counts = {attack: attacks.count(attack) for attack in set(attacks)}

            plt.figure(figsize=(10,6))
            plt.bar(attack_counts.keys(), attack_counts.values())
            plt.title(f'Cantidad de ataques de {robot_name}')
            plt.xlabel('Nombre del ataque')
            plt.ylabel('Cantidad de usos')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(f'{robot_name}_attack_usage.png')
            plt.close()

    

# return {'turns' : int, 
#         'winner' : {'name' : str, attacks : list, 'energy' : int}, 
#         'looser' : {'name' : str, attacks : list, 'energy' : int}}
# o 
# return {'turns' : int, 
#         'name' : {attacks : list, 'energy' : int, 'winner' : bool}, 
#         'name' : {attacks : list, 'energy' : int, 'winner' : bool}}
# equipos:
# return {'turns' : int, 
#         'Team1' : [{'name' : str, 'attacks' : list, 'energy' : int}, ...], 
#         'Team2' : [{'name' : str, 'attacks' : list, 'energy' : int}, ...]}