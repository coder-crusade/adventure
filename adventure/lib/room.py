from adventure.lib.base_obj import Base


class Room(Base):

    def __init__(self):
        super().__init__()
        self.exits = {}
    
    def __str__(self):
        super.__str__()


    def add_exit(self, direction, room):
        '''
        method that add exits to any given  room
        '''
        self.exits[direction] = room
    
    def visible_look(self):
        '''
        method that return a string of all the object that
        are visible inside of a room.
        '''
        visible_object_found = ''
        for obj in self.inventory :
            if obj.is_hidden() == False :
                visible_object_found += obj.name+', '
        return f"{visible_object_found}are the visible items found in the room"

    def search(self):
        '''
        method that return a string of all the object that
        are hidden inside of a room.
        '''
        invisible_object_found = ''
        for obj in self.inventory:
            if obj.is_hidden() == True:
                invisible_object_found += obj.name+', '
                obj.hidden = False
        return f"{invisible_object_found}are the hidden items found in the room"
    