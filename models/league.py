from competition import Competition
import random
from attack import Attack
from solo_battle import SoloBattle

class League(Competition):
    def __init__(self,robots):
        super().__init__(robots)

    def play(self):
        for i in range(len(self.robots)):
            for j in range(i + 1, len(self.robots)):
                robot_1 = self.robots[i]
                robot_2 = self.robots[j]
                print(f"\nComienza la batalla entre {robot_1.get_name()} y {robot_2.get_name()}!")
                
                battle = SoloBattle(robot_1, robot_2)
                winner, loser = battle.start(auto=True)
                
                print(f"Ganador: {winner.get_name()}, Perdedor: {loser.get_name()}")
                self.register_results(winner, loser)
        
        self.generate_reports()
    
    # def simulate_battle(self, robot_1, robot_2):
    #     robot_1.reset_energy()
    #     robot_2.reset_energy() 

    #     while robot_1.get_energy() > 0 and robot_2.get_energy() > 0: 
    #         #turnos impares, crea un ataque y luego le asigna el danio de este al otro robot, luego revisa si la vida del contrincante a disminuido a 0
    #         attack_1 = robot_1.get_move()
    #         attack_1.set_recharge()
    #         if random.randint(1,100) <= attack_1.get_precision():
    #             robot_2.receive_damage(attack_1.get_damage())
            
    #         if robot_2.get_energy() <= 0:
    #             return robot_1, robot_2
            
    #         #turnos pares
    #         attack_2 = robot_2.get_move()
    #         attack_2.set_recharge()
    #         if random.randint(1,100) <= attack_2.get_precision():
    #             robot_1.receive_damage(attack_2.get_damage())

    #         if robot_1.get_energy() <= 0:
    #             return robot_2, robot_1