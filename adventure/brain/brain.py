from adventure.lib.player import Player
from adventure.lib.room import Room

# level 1 imports
from adventure.monsters.rat import Rat
from adventure.items.key import Key

debug = {
    'action' : True,
    'room-movement' : True,
}

def GameLogic():

    # probably should move this into the player object
    def move_player(destination):
        player.move(destination)

    player = Player()

    def level1(player):
        room1 = Room()
        room2 = Room()
        room3 = Room()

        # map looks like this:
        #
        #  [ room1 ] - [ room2 ] - [ room3 ]
        #     ^            ^
        #   player     rat & key

        # link room1 <-> room2
        room1.add_exit('east', room2)
        room2.add_exit('west', room1)

        # link room2 <-> room3
        room2.add_exit('east', room3)
        room3.add_exit('west', room2)

        # create a rat and a key
        rat = Rat()
        key = Key()

        # move everything to the proper room
        player.move(room1)
        rat.move(room2)
        key.move(room2)

    # instantiate level1
    level1(player)

    prompt_string = '> '
    while True:
        action = input(prompt_string)

        action = action.strip().lower()

        verb = action.split(" ")[0:1][0]
        noun = action.split(" ")[1:]

        if debug['action']:
            print('action:', action)
            print('verb:', verb)
            print('noun:', noun)

        # handle movement

        # expand short directions into longer directions
        if verb == 'n':
            verb = 'north'
        elif verb == 's':
            verb = 'south'
        elif verb == 'e':
            verb = 'east'
        elif verb == 'w':
            verb = 'west'

        if verb in ['north', 'south', 'east', 'west']:
            if verb in player.environment.exits:
                print(f'You walk {verb}')
                move_player(player.environment.exits[verb])
            else:
                print("You hit wall")
        else:
            print(f"You cannot {verb}. (yet)")


GameLogic()