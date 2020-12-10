from adventure.lib.living import Living


class Player(Living):
    def __init__(self):
        super().__init__()
        self.name = "you"
        self.my_map_string = "You"
        self.actions = {
            # cardinal directions are always an available action,
            # so if the room does not have those exits, lets handle them
            'north'  : self.do_not_move_player,
            'south'  : self.do_not_move_player,
            'east'   : self.do_not_move_player,
            'west'   : self.do_not_move_player,

            # strike
            'strike' : self.do_strike,
        }


    def action(self, verb, args=None):
        """
        action handler for the player object

        return values:
        False - repesents an action that was not resolved
        True  - represets an action that was resolved
        """


        # cardinal directions are special commands, and are allowed to be shortcutted:
        # expand short directions into longer directions
        if verb == 'n':
            verb = 'north'
        elif verb == 's':
            verb = 'south'
        elif verb == 'e':
            verb = 'east'
        elif verb == 'w':
            verb = 'west'

        # is the action part of the environments exit list?
        if verb in self.environment.exits.keys():
            return self.do_move_player(verb, args, self)

        # is the action is in the players action list?
        if verb in self.actions:
            return self.actions[verb](verb, args, self) 

        # is the action in some obejct in the inventory of the player?
        for obj in self.inventory:
            if verb in obj.actions:
                resolved = obj.actions[verb](verb, args, self)
                if not resolved: 
                    continue
                else:
                    return True

        #is the action in some object in the enviroment of the player?
        for obj in self.environment.inventory:
            if verb in obj.actions:
                resolved = obj.actions[verb](verb, args, self) 
                if not resolved:
                    continue
                else:
                    return True

        #is the action in the enviroment's list of actions?
        if verb in self.environment.actions:
            return self.environment.actions[verb](verb, args, self) 



    def do_move_player(self, verb, args, player):
        """
        action to move a player in a cardinal direction
        """

        print(f'You walk {verb}')
        self.move(self.environment.exits[verb])
        return True


    def do_not_move_player(self, verb, arg, player):
        print(f'You bump into a wall as you try to walk {verb}.')
        return True


    def do_strike(self, verb, args, player):
        for thing in self.environment.inventory:

            if thing.name.lower() != args:
                continue 

            if not isinstance(thing, Living):
                print(f'You cannot strike ')
                return True

            if not thing.is_alive:
                thing.corpse_message()
                return True

            print(f"You hit the {thing.name} for {self.attack_value} damage!")
            damage = thing.hit(self.attack_value)
            if not self in thing.angry:
                print(f'{thing.name} snarls at you!')
                thing.angry.append(self) 

            thing.respond_to_hit(self)
        
            return True

        print("Strike what?")
        return True





    
