from adventure.lib.monster import Monster
import random

class Guard(Monster):
    def __init__(self):
        super().__init__()
        self.name = "Guard"
        self.description = "A burly guard stands in your way!"
        self.health = 8
        self.attack_value = 2
        self.my_map_string = "|X|"

    def choose_action(self, player):
        super().choose_action(player)

        if self.environment == player.environment:
            if not len(self.angry):
                print("The guard strikes you hard!")
                player.hit(self.attack_value)
                self.angry.append(player)

        keys = self.environment.exits.keys()

        possibilities = [ key for key in keys ]
        random_direction = random.choice(possibilities)
        random_room = self.environment.exits[random_direction]
        self.move(random_room)
    
    def print_guard():
        print(
"""
there's a guard
                   {}
                  .--.
                 /.--.\
                 |====|
                 |`::`|  
             .-;`\..../`;_.-^-._
            /  |...::..|`   :   `|
           |   /'''::''|   .:.   |
           ;--'\   ::  |..:::::..|
           <__> >._::_.| ':::::' |
           |  |/   ^^  |   ':'   |
           \::/|       \    :    /
           |||\|        \   :   / 
           ''' |___/\___|`-.:.-`
                \_ || _/    `
                <_ >< _>
                |  ||  |
                |  ||  |
               _\.:||:./_
              /____/\____\
    """)