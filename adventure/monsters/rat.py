from adventure.lib.monster import Monster

class Rat(Monster):
    def __init__(self):
        super().__init__()
        self.name = "Rabies Rat"
        self.description = "That rat looks like it might be sick. I should be careful not to get bit!"
        #Set the Rat's starting health to 2 so that the player only has to attack the Rat twice to kill it
        self.health = 2
        #Set the Rat's attack_value to 1 so that it takes the rat 10 strikes to kill the player
        self.attack_value = 1
