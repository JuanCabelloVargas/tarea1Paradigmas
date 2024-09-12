import json
import random
import csv
from abc import ABC, abstractmethod
from robots import Robot, Attack
#from competition import League, SingleFastBattle
from competition import *
from menus import MainMenu, RobotSelection, FileSelection, UserInput
from robots.skills import Skill
from robots.trigger import *



class Menu:
    def __init__(self) -> None:
        self.robots = {}
        pass

    def load_robots(self, filename) -> None:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                # Ahora data es un diccionario
                for rb in data["robots"]:
                    self.robots[rb['name']] = Robot(rb['name'], rb['energy'])
                
                print("\nRobots cargados\nAñadiendo ataques...\n")
                
                for rb in data['robots']:
                    if 'attacks' in rb:
                        for at in rb['attacks']:
                            self.robots[rb['name']].add_attack(at['name'], at['type'], at['objective'], at['damage'], at['precision'], at['recharge'])
                        print("")
                    #print(f"Ataques para {rb['name']}:")
                    print(self.robots[rb['name']].get_attacks_list())
                
                # Habilidades
                for rb in data['robots']:
                    if 'skills' in rb:
                        for sk in rb['skills']:
                            trigger = None
                            if sk['trigger'] == 'energy':
                                trigger = EnergyTrigger(sk['trigger_value'])
                                print(f"Habilidad {sk['name']} tiene un trigger de tipo 'energy' con valor {sk['trigger_value']}")
                            elif sk['trigger'] == 'attack type':
                                trigger = AttackTypeTrigger(sk['trigger_value'])
                                print(f"Habilidad {sk['name']} tiene un trigger de tipo 'attack type' para ataques de tipo {sk['trigger_value']}")
                            elif sk['trigger'] == 'attack_team':
                                trigger = AttackTeamTrigger('team')
                                print(f"Habilidad {sk['name']} tiene un trigger de tipo 'team' activado cuando el ataque es para el equipo")
                            elif sk['trigger'] == 'turns':
                                trigger = TurnsTrigger(sk['trigger_value'])
                                print(f"Habilidad {sk['name']} tiene un trigger de tipo 'turns' con valor {sk['trigger_value']}")
                            

                            
                            if trigger is not None:
                                skill = Skill(sk['name'], trigger, sk['duration'], sk['effect'], sk['objective'], sk['effect_value'])
                                self.robots[rb['name']].add_skill(skill)
                print("\nAtaques y habilidades añadidos correctamente\n")
                #print("\nAttacks added\n")
                #print(self.robots)
        except Exception:
            input("Archivo incorrecto o no encontrado. \nPresione 'enter' para continuar.")



    def start(self):
        league = League(self.robots)
        league.play()
        self.show_results(league)
        pass

    def new_start(self):
        while True:
            opt = MainMenu.get_menu()
            if opt == 1:
                filename = FileSelection.get_menu()
                self.load_robots(filename)
            if opt == 2:
                self.gamemodes()
                ...
            if opt == 4 and len(self.robots.items()) != 0:
                r_opt = RobotSelection.get_menu(list(self.robots.keys()))
                if r_opt != None:
                    self.robots[r_opt].attack_selection(False)
                ...
            if opt == 6:
                break

            ...

    def gamemodes(self):
        text = "Seleccione modo de juego\n"
        self.available_modes = [cls_obj for cls_name, cls_obj in globals().items() 
                      if isinstance(cls_obj, type) and issubclass(cls_obj, Competition) and cls_obj is not Competition]
        for i, o in enumerate(self.available_modes):
            text += f"{i+1}- {o.get_description()}\n"
        print([o.get_description() for o in self.available_modes])
        
        print(text)
        opt = UserInput.get_input()
        if opt.isnumeric() and int(opt) in range(1, len(self.available_modes)+1):
            #print(opt)
            self.game_mode = self.available_modes[int(opt)-1](self.robots)
            self.game_mode.play()
        else:
            print("Opcion no valida. Presione 'enter' para continuar")
            UserInput.get_input()
        


        
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
#g1.load_robots("data.json")
#g1.start()
g1.new_start()
    

