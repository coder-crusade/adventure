from adventure.lib.base_obj import Base

class Room(Base):

    def __init__(self):
        super().__init__()

        self.exits = {}
        self.x = None
        self.y = None
        self.description = "A sparse room with a cold stone floor."
        
        self.actions = {"look" : self.do_show_room}
    
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
        if len(self.inventory) == 1:
            print('The room is empty!')
            return True
        for obj in self.inventory :
            if obj.is_hidden() == False and not obj.name == 'you':
                visible_object_found += " "+obj.name+'\n'
        print(f"The room contains:\n {visible_object_found}")
        return True



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
        print(f"Whoa! You found a {invisible_object_found}! I wonder if this is useful?")


    def __repr__(self):
        if len(self.inventory):
            return self.inventory[0].map_string()
        
        return ' . '


    def do_show_room(self, verb=None, args=None, player=None):
        destinations = []
        for key in self.exits.keys():
            destinations.append(key)
        directions = ''
        for i in range(len(destinations)-1):
            directions += destinations[i] + ", "
        directions += destinations[len(destinations)-1]+"."
        print(f"{self.description}\n Directions available: {directions}")
        self.visible_look()
        return True
