from adventure.lib.item import Item
from adventure.items.key import Key

class Door(Item):
    def __init__(self):
        super().__init__()
        self.name = "door"
        self.description = "Unlock this door to leave the level."
        self.actions = { "unlock" : self.do_unlock_door }
        self.my_map_string = "-D-"

    def do_unlock_door(self, verb, args, player):
        #if a key exsits in the player's inventory, then unlock the door
        for obj in player.inventory:
            if isinstance(obj, Key):
                obj.environment.inventory.remove(obj)
                obj.environment = None
                print("You've opened the door! Get outta here!")
                return "level_complete"
        print("You must collect a key.")
        return True

    def introduce(self, player):
        if not super().introduce(player):
            return
        self.print_door()
        
    def print_door(self):
        print(
        """
           You've found a door!
        Perhapss you can 'unlock' it
         __________________
        |_________________|\\
         | _____ | _____ | |
         | |###| | |###| | |
         | |###| | |###| | |  
         | _____ | _____ | |  
         | || || | || || | |
         | ||_|| | ||_|| | |
         | _____O|O_____ | | 
         | || || | || || | | 
         | ||_|| | ||_|| | |
         | _____ | _____ | |
         | || || | || || | | 
         | ||_|| | ||_|| | |       
         |       |       | |       
         *****************`
        """
        )
