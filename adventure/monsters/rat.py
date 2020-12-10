from adventure.lib.monster import Monster
from adventure.items.key import Key

class Rat(Monster):
    def __init__(self):
        super().__init__()
        self.name = "Rabies Rat"
        self.description = "That rat looks like it might be sick. I should be careful not to get bit!"
        #Set the Rat's starting health to 2 so that the player only has to attack the Rat twice to kill it
        self.health = 2
        #Set the Rat's attack_value to 1 so that it takes the rat 10 strikes to kill the player
        self.attack_value = 1
        self.actions = {"search" : self.do_search_corpse}
        self.my_map_string = "Rat"

    def respond_to_hit(self, player):
        if self.health:
            print("- - - Keep striking it! - - -")

    def do_search_corpse(self, verb, args, player):
        key = Key()
        key.move(self.environment)
        print(f"As you search the {self.name} you hear a {key.name} hit the floor! You should 'Collect' it!")
        self.environment.inventory.remove(self)
        self.environment = None
        return True

    def hit(self, attack_value):
        super().hit(attack_value)
        if not self.is_alive:
            print(f"Perhaps you can 'Search {self.name}'")