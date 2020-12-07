from adventure.lib.base_obj import Base


class Item(Base):
    pass

# Item will NOT need a __str__ method bc it inherits from Base



# I got ahead of myself with the Weapons class - Hexx :D
#
# class Weapons(Item):
#     def __init__(self, name, description, damage):
#         '''
#         Damage will refer to the amount of points that a weapon can take away from the user's health
#         '''
#         self.damage = 0 
#         super().__init__(name, description)
