from abc import ABC, abstractmethod
from robot import Robot
from report_generator import ReportGenerator

class Competition(ABC):
    def __init__(self,robots):
        self.robots = robots
        self.resultados = {robot.get_name(): {'victorias': 0, 'derrotas:':0} for robot in robots}
        self.history = []

    def register_results(self, winner, losser):
        self.resultados[winner.get_name()]['victorias']+=1
        self.resultados[losser.get_name()]['victorias']-=1

    @abstractmethod
    def play(self):
        ...
        
    def generate_reports(self):
        report_generator = ReportGenerator(self)

        report_generator.generate_victory_report('victories_report.csv')