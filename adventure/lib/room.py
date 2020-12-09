from adventure.lib.base_obj import Base


class Room(Base):

    def __init__(self):
        super().__init__()
        self.exits = {}

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def __repr__(self):
        if len(self.inventory):
            return ' X '
        return ' . '
