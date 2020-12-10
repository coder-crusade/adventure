from adventure.lib.base_obj import Base

class Room(Base):

    def __init__(self):
        super().__init__()

        self.exits = {}
        self.x = None
        self.y = None
        
        self.actions = {"look" : self.do_visible_look}
    
    def __str__(self):
        super.__str__()


    def add_exit(self, direction, room):
        '''
        method that add exits to any given  room
        '''
        self.exits[direction] = room


    def do_visible_look(self, verb=None, args=None, player=None):
        '''
        method that return a string of all the object that
        are visible inside of a room.
        '''
        visible_object_found = ''
        if self.inventory ==[]:
            print('The room is empty!')
            return
        for obj in self.inventory :
            if obj.is_hidden() == False :

                visible_object_found += obj.name+'\n'
            print(f"The room contain:\n {visible_object_found}.")



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

    def show_room(self):
        destinations = self.exits.keys()
        directions =''
        for destination in destinations:
            directions += destination+'\n'
        print(f"Room description:\n {self.description} \n directions available:\n  {directions}")
