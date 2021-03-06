from adventure.lib.monster import Monster
from adventure.items.key import Key

class Rat(Monster):
    def __init__(self):
        super().__init__()
        self.name = "Rat"
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
        key.introduce(player)
        return True

    def hit(self, attack_value):
        super().hit(attack_value)
        if not self.is_alive:
            self.my_map_string = "XO-"
            print(f"Perhaps you can 'Search {self.name}'")

    def introduce(self, player):
        if not super().introduce(player):
            return
        self.print_rat()

    def print_rat(self):
        print(
        """
You stumble into a giant rat! Perhaps you could 'strike rat'?
             _     __,..---""-._                 ';-,
    ,    _/_),-"`             '-.                `\\\\
   \|.-"`    -_)                 '.                ||
   /`   a   ,                      \              .'/
   '.___,__/                 .-'    \_        _.-'.'
      |\  \      \         /`        _`""""""`_.-'
         _/;--._, >        |   --.__/ `""""""`
       (((-'  __//`'-......-;\      )
            (((-'       __//  '--. /
                      (((-'    __//
                             (((-'
        """)