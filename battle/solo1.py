# This code is unused 
from robots.robot_obj import Robot
from battle.battle_main import Battle

class SoloBattle_old(Battle):
    def __init__(self, robot_1: Robot, robot_2: Robot) -> None:
        self.robot1 = robot_1
        self.robot2 = robot_2
        self.history = []
        self.robot1.reset_energy()
        self.robot2.reset_energy()
    
    def start(self, auto: bool) -> str:
        self.auto_mode = auto
        if self.auto_mode:
            return self.auto_mode()
        ...
    
    def auto_mode(self) -> str:
        self.turn = 1
        self.move_counter = 0
        while True:
            if self.turn == 1:
                attack = self.robot1.get_move()
                print(f"\n{self.robot1.get_name()} realiza {attack.get_description()}\n")
                energy = self.robot2.receive_attack(attack)
                if self.robot2.is_alive:
                    print(f"{self.robot2.get_name()} recibe {attack.get_description()}.\nEnergia = {self.robot2.get_energy()}")
                    self.turn = 2
                    self.history.append({'execute' : {'name':self.robot1.get_name(), 'attack':attack}, 'receive' : {'name':self.robot2.get_name(), 'is_alive':self.robot2.is_alive, 'energy':self.robot2.get_energy()}})

                else:
                    print(f"{self.robot2.get_name()} recibe {attack.get_description()}.\nEnergia = {self.robot2.get_energy()}\n\n{self.robot2.get_name()} is dead.")
                    input("Presione 'enter' para continuar\n>")
                    self.history.append({'execute' : {'name':self.robot1.get_name(), 'attack':attack}, 'receive' : {'name':self.robot2.get_name(), 'is_alive':self.robot2.is_alive, 'energy':self.robot2.get_energy()}})
                    self.turn = 0
                ...
            
            elif self.turn == 2:
                attack = self.robot2.get_move()
                print(f"\n{self.robot2.get_name()} realiza {attack.get_description()}\n")
                energy = self.robot1.receive_attack(attack)
                if self.robot1.is_alive:
                    print(f"{self.robot1.get_name()} recibe {attack.get_description()}.\nEnergia = {self.robot1.get_energy()}")
                    self.turn = 2
                    self.history.append({'execute' : {'name':self.robot2.get_name(), 'attack':attack}, 'receive' : {'name':self.robot1.get_name(), 'is_alive':self.robot1.is_alive, 'energy':self.robot1.get_energy()}})

                else:
                    print(f"{self.robot2.get_name()} recibe {attack.get_description()}.\nEnergia = {self.robot2.get_energy()}\n\n{self.robot2.get_name()} is dead.")
                    input("Presione 'enter' para continuar\n>")
                    self.history.append({'execute' : {'name':self.robot2.get_name(), 'attack':attack}, 'receive' : {'name':self.robot1.get_name(), 'is_alive':self.robot1.is_alive, 'energy':self.robot1.get_energy()}})
                    self.turn = 0
                ...
            else:
                break
        return   