from adventure.lib.item import Item

class Torch(Item):
    def __init__(self):
        super().__init__()
        self.name = "Torch"
        self.description = "This torch will help you see farther."
        self.actions = {"collect" : self.do_move_torch_to_inventory}
        self.my_map_string = " T "

    def do_move_torch_to_inventory(self, verb, args, player):
        if args != self.name.lower():
            return False
        self.move(player)
        print(f"You've collected the {self.name}.")
        return True

    def introduce(self, player):
        if not super().introduce(player):
            return
        self.print_torch()

    def print_torch(self):
        print(
        """
    You found a torch, perhaps you could 'collect' it!

            )            
        *7*
        (`)`)
        |||
        |||
        |_|
        """
        )