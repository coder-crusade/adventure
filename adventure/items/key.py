from adventure.lib.item import Item

class Key(Item):
    def __init__(self):
        super().__init__()
        self.name = "Key"
        self.description = "This rusty old key might be just what you need to get out of here!"