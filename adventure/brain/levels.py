from adventure.lib.room import Room

from adventure.lib.map import connect_rooms, dungeon_maker, show_map, randomly_place

from adventure.items.key import Key
from adventure.items.door import Door
from adventure.monsters.rat import Rat
from adventure.monsters.guard import Guard
from adventure.items.torch import Torch

def generate_level1(player):

    monsters = []
    current_map = dungeon_maker(5, 1)
    connect_rooms(current_map)

    room1 = current_map[0][0]
    room2 = current_map[0][2]
    room3 = current_map[0][4]

    # map looks like this:
    #
    #  [ room1 ] - [ room2 ] - [ room3 ]
    #     ^            ^          ^
    #   player     rat & key     door

    # create a rat
    rat = Rat()
    monsters.append(rat)
    rat.move(room2)

    #create a door
    door = Door()
    door.move(room3)

    # move everything to the proper room
    player.move(room1)


    return (monsters, current_map)


def generate_level2(player):

    monsters = []
    current_map = dungeon_maker(5, 5)
    connect_rooms(current_map)

    # create a rat, and randomly place
    rat = Rat()
    monsters.append(rat)
    randomly_place(current_map, rat)

    # create a door, and randomly place
    door = Door()
    randomly_place(current_map, door)

    # randomly place a player
    randomly_place(current_map, player)


    return (monsters, current_map)


def generate_level3(player):
    monsters = []
    current_map = dungeon_maker(20, 20, 1)
    connect_rooms(current_map)

    # create a rat, and randomly place
    rat = Rat()
    monsters.append(rat)
    randomly_place(current_map, rat)

    # create a few guards, and randomly place
    guard1 = Guard()
    guard2 = Guard()
    guard3 = Guard()

    monsters.append(guard1)
    monsters.append(guard2)
    monsters.append(guard3)

    randomly_place(current_map, guard1)
    randomly_place(current_map, guard2)
    randomly_place(current_map, guard3)

    # create and randomly place a torch
    torch = Torch()
    randomly_place(current_map, torch)

    # create a door, and randomly place
    door = Door()
    randomly_place(current_map, door)

    # randomly place a player
    randomly_place(current_map, player)


    return (monsters, current_map)
