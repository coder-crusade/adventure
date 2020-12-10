from adventure.lib.base_obj import Base
from adventure.lib.room import Room
from adventure.items.key import Key
class Living(Base):

    def __init__(self):
        '''
        Class holding init status of monster and player (dead) 
        '''
        super().__init__()
        self.health = 10
        self.max_health = 10
        self.attack_value = 1
        
    def hit(self, attack_value):
        '''
        method reducing health points of objects 
        '''
        self.health = self.health - attack_value 
        #if our health is less than 1, then death
        if self.health <= 0:
            print(f'{self.name} has died!')
        return self.attack_value

    def heal(self, num):
        '''
        method add healing points to objects
        '''
        if self.health < self.max_health:
            if (self.health + num) > self.max_health:
                self.health = self.max_health
            else:
                self.health += num
    
    #the property decorator is making is_alive behave as if it were a property of the Living class - contributed by Skyler Burger
    @property 
    def is_alive(self):
        '''
        method that check if objects is alive
        returns True if it alive, False if not.
        '''
        if self.health <= 0:
            return False
        return True

    def corpse_message(self):
        print(f"Alright, that\'s enough! You already killed the {self.name}!")

    def respond_to_hit(self, player):
        pass
