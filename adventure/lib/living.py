from adventure.lib.base_obj import Base
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
            self.environment.inventory.remove(self)
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
    
    def is_alive(self):
        '''
        method that check if objects is alive
        returns True if it alive, False if not.
        '''
        if self.health <= 0:
            return False
        return True

