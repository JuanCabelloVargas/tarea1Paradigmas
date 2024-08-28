class Attack:
    def __init__(self, attack_name: str, attack_type: str, objective: str, damage: int, precision: int, recharge: int) -> None:
        self.attack_name = attack_name
        self.attack_type = attack_type
        self.objective = objective
        self.damage = damage
        self.precision = precision 
        self.recharge = recharge
        self.current_recharge = 0
        
    
    def get_damage(self) -> int:
        return self.damage
    
    def get_precision(self) -> int:
        return self.precision
    
    def get_recharge(self) -> int:
        return self.recharge
    
    def update_recharge(self) -> None:
        if self.recharge > 0:
            self.recharge -= 1

    def set_recharge(self) -> None:
        self.current_recharge = self.recharge

    def is_available(self) -> bool:
        return True if self.recharge == 0 else False
    
    def get_description(self):
        return self.attack_name
    
    def get_specs(self):
        return f"Attack name: {self.attack_name}\n\nType: {self.attack_type}\nObjective: {self.objective}\nDamage: {self.damage}\nPrecision: {self.precision}\nRecharge: {self.recharge}"

