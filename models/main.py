import json
import random
from menu import RobotGame

'''
"name": "lanza de hielo",
"type": "sword",
"objective": "team",
"damage": 25,
"precision": 80,
"recharge": 2
'''



    
if __name__ == "__main__":
    game = RobotGame()
    game.load_robots("data.json")
    game.start()
    

