import json
import random
import csv
from abc import ABC, abstractmethod
from robots import Robot, Attack
from competition import League


class Menu:
    def __init__(self) -> None:
        self.robots = {}
        pass

    def load_robots(self, filename) -> None:
        with open(filename, 'r') as f:
            data = json.load(f)
            #Now data is a dictionary
            for rb in data["robots"]:
                self.robots[rb['name']] = Robot(rb['name'], rb['energy'])
            
            print("\nRobotsloaded\nAdding attacks...\n")
            
            for rb in data['robots']:
                if 'attacks' in rb:
                    for at in rb['attacks']:
                        self.robots[rb['name']].add_attack(at['name'], at['type'], at['objective'], at['damage'], at['precision'], at['recharge'])
                    print("")
                print(self.robots[rb['name']].get_attacks_list())
            print("\nAttacks added\n")
            #print(self.robots)



    def start(self):
        league = League(self.robots)
        league.play()
        self.show_results(league)
        pass

    def show_results(self, competicion):
        print("\nResultados de la Liga:")
        for robot, results in competicion.results.items():
            print(f"{robot}: {results['victorias']} victorias, {results['derrotas']} derrotas")

        with open('results.csv', mode='w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Robot','Victorias', 'Derrotas', 'Turnos'])
            for robot, results in competicion.results.items():
                writer.writerow([robot,results['victorias'], results['derrotas'],results.get('turnos',0)])

        pass


g1 = Menu()
g1.load_robots("data.json")
g1.start()
    

