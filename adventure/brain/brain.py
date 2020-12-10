from adventure.lib.player import Player
import pyfiglet


# level imports
from adventure.brain.levels import generate_level1
from adventure.brain.levels import generate_level2
from adventure.brain.levels import generate_level3

# for showing the map on each action
from adventure.lib.map import show_map
from adventure.items.torch import Torch


def ascii_text(words):
    return pyfiglet.figlet_format(words, font="big")


def GameLogic():

    player = Player()

    monsters = []

    level = 1

    def game_loop():
        nonlocal level
        # initial fog of war viewing radius
        radius = 4

        while True:
            for obj in player.inventory:
                if(isinstance(obj, Torch)):
                    radius = 7
            show_map(current_level, player, radius)
            
            
            
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
                    level += 1
                    return True
                    
                # after a player action, all the items in the player's environment get a chance to introduce themselves
                for obj in player.environment.inventory:
                    if obj != player:
                        obj.introduce(player)

                # after player action, monsters get an opportunity for their own action
                for monster in monsters:
                    monster.choose_action(player)

                # player died
                if not player.is_alive:
                    return False

                # we didn't win or die, so lets prompt another action
                continue   
            else:
                print(f"You cannot {verb}.")



    result = True
    while result:
        if(level <= 3):

            # set up whichever level we need to generate
            if(level == 1):
                generate = generate_level1
            if(level == 2):
                generate = generate_level2
            if(level == 3):
                generate = generate_level3
        
            monsters, current_level = generate(player)
            print(ascii_text(f"Level {level}"))
            result = game_loop()
        else:
            result = False
            print("You escaped the dungeon!!!\n")
            print(ascii_text("You did it!"))
            return
    
    print(ascii_text("GAME OVER!"))


GameLogic()
