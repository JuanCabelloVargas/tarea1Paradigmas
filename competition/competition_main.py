import random

#Only used for reference, 'Robot' objects aren't created here
from robots.robot_obj import Robot 


class Competition:
    def __init__(self, robots):
        #iterate robot objects
        self.robots = list(robots.values())
        self.results = {robot.get_name(): {'victorias': 0, 'derrotas': 0} for robot in self.robots}

    def register_results(self, winner, loser):
        self.results[winner.get_name()]['victorias'] += 1
        self.results[loser.get_name()]['derrotas'] += 1

