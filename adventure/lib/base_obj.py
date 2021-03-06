class Base:

    def __init__(self):
        self.environment = None
        self.inventory = []
        self.description = None
        self.ids = []
        self.name = None
        self.hidden = False
        self.actions = {}
        self.my_map_string = "   "
        self.introduced = False

    def move(self, destination):
        """
        this method is for moving objects into other objects.
        """
        # remove self from environment inventory list
        if self.environment:
            self.environment.inventory.remove(self)

        # set environment as destination
        self.environment = destination

        # add self to new environment inventory
        self.environment.inventory.append(self)

    def __str__(self):
        """
        this method is for description of space
        """
        return self.name
    
    def map_string(self):
        return self.my_map_string

    def contains_id(self):
        """
        this method contains lists of ids for comparing the input:
        """
        pass
    
    def is_hidden(self):
        return self.hidden

    def introduce(self, player=None):
        if self.introduced or not self.environment == player.environment:
            return False
        
        self.introduced = True
        return True
        