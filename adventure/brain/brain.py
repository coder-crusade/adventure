from adventure.lib.player import Player
from adventure.lib.room import Room

# testing
from adventure.lib.map import connect_rooms, dungeon_maker, show_map

# level 1 imports
from adventure.monsters.rat import Rat
from adventure.items.key import Key

debug = {
    'action' : True,
    'combat' : True,
}


def GameLogic():

    player = Player()
    monsters = []

    def level1():
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

        # create a rat
        rat = Rat()
        monsters.append(rat)

        # move everything to the proper room
        player.move(room1)
        rat.move(room2)

        return [[room1, room2, room3]]

    # instantiate level1
    current_level = level1()

    # seths_map = dungeon_maker(12, 12)
    # connect_rooms(seths_map)
    # player.move(seths_map[0][0])

    while True:
        show_map(current_level, player)
        
        action = input(f'Health {player.health}/{player.max_health} > ')

        action = action.strip().lower()

        verb = action.split(" ")[0:1][0]
        args = " ".join(action.split(" ")[1:])

        if debug['action']:
            print('action:', action)
            print('verb:', verb)
            print('args:', args)

        # actions are hanled in the player object
        action_resolved = player.action(verb, args)
        # TODO: allow more than True/False resolutions, so that we can
        # have varying levels of commands:
        # active commands, such as 'strike' or movement, that allow monsters to react
        # passive commands, such as 'look', that do not allow monsters to react
        if(action_resolved):
            for monster in monsters:
                monster.choose_action()
            continue   
        else:
            print(f"You cannot {verb}. (yet)")

GameLogic()
