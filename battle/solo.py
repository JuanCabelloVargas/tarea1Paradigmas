from battle.battle_main import Battle
import random

#Only for references
from robots import Robot, Attack


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
            #turnos impares, crea un ataque y luego le asigna el danio de este al otro robot, luego revisa si la vida del contrincante a disminuido a 0
            attack_1 = self.robot_1.get_move()
            if random.randint(1,100) <= attack_1.get_precision():
                self.robot_2.receive_damage(attack_1.get_damage())
                self.stats['turns'] += 1
                self.stats[self.r1_name]['attacks'].append(attack_1.get_description())
                #Logs
                print(f"\n{self.robot_1.get_name()} realiza {attack_1.get_description()}\n")
                print(f"{self.robot_2.get_name()} recibe el ataque; ahora su nergia es {self.robot_2.get_energy()}")
            
            if self.robot_2.get_energy() <= 0:
                input(f"\n{self.r1_name} ha ganado.\nPresione 'enter' para continuar.\n>")
                print('-' * 32)
                self.stats[self.r1_name]['winner'] = True
                self.stats[self.r1_name]['energy'] = self.robot_1.get_energy()
                return self.robot_1, self.robot_2
            
            #turnos pares
            attack_2 = self.robot_2.get_move()
            if random.randint(1,100) <= attack_2.get_precision():
                self.robot_1.receive_damage(attack_2.get_damage())
                self.stats['turns'] += 1
                self.stats[self.r2_name]['attacks'].append(attack_2.get_description())
                #Logs
                print(f"\n{self.robot_2.get_name()} realiza {attack_2.get_description()}\n")
                print(f"{self.robot_1.get_name()} recibe el ataque; ahora su nergia es {self.robot_1.get_energy()}")

            if self.robot_1.get_energy() <= 0:
                input(f"\n{self.r2_name} ha ganado.\nPresione 'enter' para continuar.\n>")
                print('-' * 32)
                self.stats[self.r2_name]['winner'] = True
                self.stats[self.r2_name]['energy'] = self.robot_2.get_energy()
                return self.robot_2, self.robot_1
    
    def manual_mode(self):
        return super().manual_mode()
    
    def get_stats(self) -> dict:
        return self.stats
        
    

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