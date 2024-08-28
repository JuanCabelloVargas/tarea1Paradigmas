from abc import abstractmethod
from battle import Battle
from attack import Attack
from robot import Robot

class SoloBattle(Battle):
    def __init__(self, robot1: Robot, robot2: Robot) -> None:
        self.robot1 = robot1
        self.robot2 = robot2
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
                if self.execute_turn(self.robot1, self.robot2):
                    self.turn = 2
                else:
                    break
            elif self.turn == 2:
                if self.execute_turn(self.robot2, self.robot1):
                    self.turn = 1
                else:
                    break
            else:
                break
        return
    
    def execute_turn(self, attacker: Robot, defender: Robot) -> bool:
        attack = attacker.get_random_attack()
        attack.set_recharge()
        print(f"\n{attacker.get_name()} realiza {attack.get_description()}\n")
        defender.receive_attack(attack)

        if defender.is_alive:
            print(f"{defender.get_name()} recibe {attack.get_descriptio()}. \nEnergia = {defender.get_energy()}")
            self.history.append({'execute': {'name': attacker.get_name(), 'attack': attack}, 
                             'receive': {'name': defender.get_name(), 'is_alive': defender.is_alive, 'energy': defender.get_energy()}})
            return True
        else:
            print(f"{defender.get_name()} recibe {attack.get_description()}.\nEnergia = {defender.get_energy()}\n\n{defender.get_name()} is dead.")
            input("Presione 'enter' para continuar\n>")
            self.history.append({'execute': {'name': attacker.get_name(), 'attack': attack}, 
                             'receive': {'name': defender.get_name(), 'is_alive': defender.is_alive, 'energy': defender.get_energy()}})
            return False
        