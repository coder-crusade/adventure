from adventure.lib.base_obj import Base


class Room(Base):

    def __init__(self):
        super().__init__()
        self.exits = {}   
        #  self.exits = {
            # 'north' 
            # 'south '
            # 'east'
        # }
    
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
        if self.inventory ==[]:
            return 'The room if empty!'
        for obj in self.inventory :
            if obj.is_hidden() == False :
                visible_object_found += obj.name+'\n'
            return f"The room contain:\n {visible_object_found}."


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
    

    def __repr__(self):
        if len(self.inventory):
            return ' X '
        return ' . '

    def show_room(self, destinations, description):
        destinations = self.exits.keys()
        self.description = description
        directions =''
        for destination in destinations:
            directions += destination+'\n'
        return f"Room description:\n {description} \n direction avaible:\n  {directions}"
