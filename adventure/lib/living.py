from adventure.lib.base_obj import Base
class Living(Base):

    def __init__(self):
        '''
        Class holding init status of monster and player (dead) 
        '''
        self.health = 10
        self.max_health = 10
        self.attack_value = 0
        
    def hit(self, attack_value):
        '''
        method reducing health points of objects 
        '''
        self.health = self.health - attack_value 
        return self.health

    def heal(self, num):
        '''
        method add healing points to objects
        '''
        if self.health < self.max_health:
            if (self.health + num) > self.max_health:
                self.health = self.max_health
            else:
                self.health += num
    
    def is_alive(self):
        '''
        method that check if objects is alive
        returns True if it alive, False if not.
        '''
        if self.health <= 0:
            return False
        return True

