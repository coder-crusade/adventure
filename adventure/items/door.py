from adventure.lib.item import Item
from adventure.items.key import Key

class Door(Item):
    def __init__(self):
        super().__init__()
        self.name = "door"
        self.description = "Use this door to leave the level"
        self.actions = {"unlock" : self.do_unlock_door}

    def do_unlock_door(self, verb, args, player):
      #if a key exsits in the player's inventory, then unlock the door
      for obj in player.inventory:
        if isinstance(obj) == Key
        print("You've opened the door! Get outta here!")
          return True
