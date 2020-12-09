from adventure.lib.player import Player
from adventure.lib.room import Room

# testing
from adventure.lib.map import connect_rooms, dungeon_maker, show_map2

# level 1 imports
from adventure.monsters.rat import Rat
from adventure.items.key import Key

debug = {
    'action' : True,
    'room-movement' : True,
    'combat' : True
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
    # level1(player)

    seths_map = dungeon_maker(12, 12)
    connect_rooms(seths_map)
    player.move(seths_map[0][0])

    # prompt_string = 
    while True:
        show_map2(seths_map)

        action = input(f'Health {player.health}/{player.max_health} > ')

        action = action.strip().lower()

        verb = action.split(" ")[0:1][0]
        noun = " ".join(action.split(" ")[1:])

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

        elif verb == "strike":
            for thing in player.environment.inventory:

                if thing.name.lower() != noun:
                    continue 

                if not thing.is_alive:
                    return thing.is_corpse()

                print(f"You hit the {thing.name} for {player.attack_value} damage!")
                damage = thing.hit(player.attack_value)

                if thing.health > 0:
                    damage = player.hit(thing.attack_value)
                    print(f"The {thing.name} hits you for {damage} damage!")
                    if thing.health > 0:
                        print(f"{thing.name} snarls at you!")
                        print("Hurry! Strike it again!")

                if debug['combat']:
                    print(f'Player Health: {player.health}/{player.max_health}')
                    print(f'Opponents Health: {thing.health}/{thing.max_health}')

                break 

        else:
            print(f"You cannot {verb}. (yet)")


GameLogic()
