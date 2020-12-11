from adventure.lib.living import Living
import random


class Monster(Living):
    def __init__(self):
        super().__init__()
        self.angry = []

    def choose_action(self, player):
        if not self.is_alive:
            return
        if len(self.angry):
            choose_one_to_hit = []
            for obj in self.environment.inventory:
                if obj in self.angry:
                    choose_one_to_hit.append(obj)
            if len(choose_one_to_hit):
                #random imports the method choice that takes in a list and returns one item from that list at random
                random_choice = (random.choice(choose_one_to_hit))
                random_choice.hit(self.attack_value)
                print(f"The {self.name} hits {random_choice.name} for {self.attack_value} damage!")

    def random_move(self):
        keys = self.environment.exits.keys()

        possibilities = [ key for key in keys ]
        random_direction = random.choice(possibilities)
        random_room = self.environment.exits[random_direction]
        self.move(random_room)
