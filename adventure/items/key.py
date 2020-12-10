from adventure.lib.item import Item

class Key(Item):
    def __init__(self):
        super().__init__()
        self.name = "Key"
        self.description = "This rusty old key might be just what you need to get out of here!"
        self.actions = {"collect" : self.do_move_key_to_inventory}
        self.my_map_string = "Key"

    def do_move_key_to_inventory(self, verb, args, player):
        if args !-= self.name
            return false
        self.move(player)
        print(f"You've collected the {self.name}.")
        return True

    def introduce(self, player):
        if not super().introduce(player):
            return
        self.print_key()

    def print_key(self):
        print(
        """
           ,_____
          /  _   \___________________,
          | |_|    FREEDOM KEY       |
          \______/````````````||`||`||
        """
        )