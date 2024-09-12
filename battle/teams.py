from battle.battle_main import Battle
#Only for references 
from robots import Robot, Attack




class TeamsBattle(Battle):
    def __init__(self, team1:dict, team2:dict) -> None:
        self.team1 = team1
        self.team2 = team2
        self.stats = {'turns' : 0, 
                      'Team1' : [], 
                      'Team2' : []}
                    # 'team' : [{'name' : str, 'attacks' : list, 'energy' : int}]
    
    def start(self):
        return super().start()
    
    def auto_mode(self):
        return super().auto_mode()
    
    def manual_mode(self):
        return super().manual_mode()
    
    def get_stats(self):
        return super().get_stats()

    ...