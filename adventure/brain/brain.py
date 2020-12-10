from adventure.lib.player import Player
from adventure.lib.room import Room

# testing
from adventure.lib.map import connect_rooms, dungeon_maker, show_map, randomly_place

# level imports
from adventure.items.key import Key
from adventure.items.door import Door
from adventure.monsters.rat import Rat
from adventure.monsters.guard import Guard


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
    # current_level = level1()

    current_level = dungeon_maker(25, 25, 1)
    connect_rooms(current_level)
    randomly_place(current_level, player)

    door = Door()
    randomly_place(current_level, door)

    guard = Guard()
    monsters.append(guard)
    randomly_place(current_level, guard)
    guard = Guard()
    monsters.append(guard)
    randomly_place(current_level, guard)
    guard = Guard()
    monsters.append(guard)
    randomly_place(current_level, guard)


    def game_loop():
        while True:
            show_map(current_level, player)
            
            action = input(f'Health {player.health}/{player.max_health} > ')

            action = action.strip().lower()

            verb = action.split(" ")[0:1][0]
            args = " ".join(action.split(" ")[1:])

            # actions are hanled in the player object
            action_resolved = player.action(verb, args)
            # stretch: allow more than True/False resolutions, so that we can
            # have varying levels of commands:
            # active commands, such as 'strike' or movement, that allow monsters to react
            # passive commands, such as 'look', that do not allow monsters to react
            if action_resolved:
                if action_resolved == "level_complete":
                    return True
                for monster in monsters:
                    if(player.environment == monster.environment):
                        monster.introduce(player)
                    monster.choose_action(player)

                    # player died due to some monsters action
                    if not player.is_alive:
                        return False

                # we didn't win or die, so lets prompt another action
                continue   
            else:
                print(f"You cannot {verb}.")

    win = game_loop()
    if win:
        print("You escaped the dungeon and won!!!")
    else:
        print("GAME OVER!")


GameLogic()
