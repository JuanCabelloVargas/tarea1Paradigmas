from battle.solo import SoloBattle
from robots.robot_obj import Robot
from competition_main import Competition
from playoff import Playoff
import random


class Tournament(Competition):
    def __init__(self, robots: dict[str, Robot], group_size = 4):
        super().__init__(robots)
        self.group_size = group_size
        self.groups =  self.create_groups()

    @classmethod
    def get_description(cls)->str:
        return "Modo Tournament"
    
    def create_groups(self):
        random.shuffle(self.robots)
        groups = [self.robots[i:i + self.group_size] for i in range (0, len(self.robots), self.group_size)] 

    def play_auto(self):
        print("Comienza el torneo...")
        playoff_robots = [] # List of robots that goes to knockout phase

        for group in self.groups:
            print(f"\nGrupo {self.groups.index(group) + 1}")

            group_results =  {robot: 0 for robot in group}
            for i in range(len(group)):
                for j in range(i+1, len(group)):
                    robot_1 = group[i]
                    robot_2 = group[j]
                    print(f"\nBatalla entre {robot_1.get_name()} y {robot_2.get_name()}")
                    mode = self.ask_battle_mode()
                    bat = SoloBattle(robot_1, robot_2)
                    if mode == 'manual':
                        winner, loser = bat.manual_mode()
                    else:                
                        winner, loser = bat.auto_mode()
                    print(f"Ganador: {winner.get_name()}, Perdedor: {loser.get_name()}")
                    self.register_results(winner, loser)
                    group_results[winner] += 1
            
            sorted_group = sorted(group_results, key=group_results.get, reverse = True) # Sort the robort sacoording to the number of wins of each one
            playoff_robots.extend(sorted_group[:2])

        print("fase de playoff entre los clasificados")
        playoff = Playoff({robot.get_name(): robot for robot in playoff_robots}) #Create the playoff using the robots that advanced to the knockout phase
        playoff.play()
