from adventure.lib.player import Player
from adventure.lib.room import Room

# level 1 imports
from adventure.monsters.rat import Rat
from adventure.items.key import Key

def GameLogic():

    # probably should move this into the player object
    def move_player(direction):
        destination = player.environment.exits[direction]
        if destination:
            print(f'You walk {direction}')
            player.move(destination)
        else
            print("You hit wall")

    player = Player()

    def level1(player):
        room1 = Room()
        room2 = Room()
        room3 = Room()

        #map looks llike this:
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

    level1(player)


    prompt_string = '> '
    while True:
        action = input(prompt_string)

        action = action.strip().lower()

        verb = action.split(" ")[0:1]
        noun = action.split(" ")[1:]

        # handle movement
        if verb in ["north", 'n']:
            move_player(player.environment.exits['north'])
            
        elif verb in ['south', 's']:
            move_player(player.environment.exits['south'])

        elif verb in ['east', 'e']:
            move_player(player.environment.exits['east'])

        elif verb in ['west', 'w']:
            move_player(player.environment.exits['west'])

    