import csv
import matplotlib as plt
from competition import Competition

class ReportGenerator:
    def __init__(self, competition: Competition):
        self.competition = competition

    def generate_victory_report(self, filename: str) ->None:
        with open(filename, 'w', newline='')as f:
            fieldnames = ['Robot/equipo', 'Victorias', 'Derrotas', 'Turnos Totales']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            for robot, results in self.competition.results.items():
                writer.writerow({
                    'Robot/equipo': robot,
                    'Victorias': results['victorias'],
                    'Derrotas': results['derrotas'],
                    'Turnos Totales': results.get('turnos_totales',0)
                })
    
### add the rest of the csv files generators in this file