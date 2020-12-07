
class Base:

    def __init__(self):
        self.environment = None
        self.inventory = []
        self.description = None
        self.ids = []

    def move(self, other):
        """
        this method is for moving objects into other objects.
        """
        pass

    def __str__(self):
        """
        this method is for description of space
        """
        pass

    def contains_id(self):
        """
        this method contains lists of ids for comparing the input:
        """
        pass