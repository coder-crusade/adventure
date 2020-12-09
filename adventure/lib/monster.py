from adventure.lib.living import Living
import random


class Monster(Living):
    def __init__(self):
        super().__init__()
        self.angry = []

    def choose_action():
        if len(self.angry):
            choose_one_to_hit = []
            for obj in self.environment.inventory:
                if obj in self.angry:
                    choose_one_to_hit.append(obj)
            if len(choose_one_to_hit):
                (random.choice(choose_one_to_hit)).hit(self.attack_value)

        
            
