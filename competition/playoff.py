from competition.competition_main import Competition
from battle.solo import SoloBattle
from robots.robot_obj import Robot
import random


class Playoff(Competition):
    def __init__(self, robots: dict[str, Robot]):
        super().__init__(robots)
        random.shuffle(self.robots)

    def play(self):
        print("Playoffs")
        while len(self.robots) > 1:
            next_round = []
            for i in range(0, len(self.robots),2):
                if i + 1 < len(self.robots):
                    robot_1 = self.robots[i]
                    robot_2 = self.robots[i + 1]
                    print("batalla....")
                    bat = SoloBattle(robot_1, robot_2)
                    winner , loser = bat.auto_mode()
                    print("ganador...Perdedor....")
                    self.register_results(winner,loser)
                    next_round.append(winner)
            self.robots = next_round
        print("campeon es...")
    
    @classmethod 
    def get_description(cls):
        return "PlayOff (Solo)"
    ...

