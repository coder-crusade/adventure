from adventure.lib.room import Room
from adventure.monsters.rat import Rat
from adventure.lib.player import Player
import random

map2 = [
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]

# room1.add_exit('east', room2)
# room2.add_exit('west', room1)


def connect_rooms(map):
    """
    this method checks the boundaries of the map,
    if room is in boundaries look for connecting rooms
    if neighboring room exists
    link rooms together with exits
    """

    for row in range(len(map)):
        for col in range(len(map[row])):
            current = map[row][col]
            if not current:
                continue

            north = None
            south = None
            east = None
            west = None

            if row - 1 >= 0:
                north = map[row - 1][col]
            if row + 1 < len(map):
                south = map[row + 1][col]
            if col - 1 >= 0:
                west = map[row][col - 1]
            if col + 1 < len(map[row]):
                east = map[row][col + 1]

            if east:
                current.add_exit('east', east)
            if west:
                current.add_exit('west', west)
            if north:
                current.add_exit('north', north)
            if south:
                current.add_exit('south', south)


def dungeon_maker(width, height):
    map = [None] * height
    for row in range(height):
        map[row] = [None] * width

    def crawl(row, col, distance, north_weight, south_weight, east_weight, west_weight):

        if not map[row][col]:
            map[row][col] = Room()
            map[row][col].x = col
            map[row][col].y = row 

        if not distance:
            rat = Rat()
            rat.move(map[row][col])
            return
        possible_directions = []

        if row - 1 >= 0:
            if not map[row - 1][col]:
                possible_directions.extend(['north'] * north_weight)
            else:
                possible_directions.append('north')
        if row + 1 < len(map):
            if map[row + 1][col]:
                possible_directions.extend(['south'] * south_weight)
            else:
                possible_directions.append('south')
        if col - 1 >= 0:
            if not map[row][col - 1]:
                possible_directions.extend(['west'] * west_weight)
            else:
                possible_directions.append('west')
        if col + 1 < len(map[row]):
            if not map[row][col + 1]:
                possible_directions.extend(['east'] * east_weight)
            else:
                possible_directions.append('east')

        random_direction = random.choice(possible_directions)

        if random_direction == 'north':
            row -= 1
        elif random_direction == 'south':
            row += 1
        elif random_direction == 'east':
            col += 1
        # random_direction == 'west':
        else:
            col -= 1
        crawl(row, col, distance-1, north_weight, south_weight, east_weight, west_weight)
    
    crawl(19, 0, 40, 70, 10, 70, 10)
    crawl(19, 19, 40, 70, 10, 10, 70)
    crawl(0, 0, 40, 10, 70, 70, 10)
    crawl(0, 19, 40, 10, 70, 10, 70)

    # for row in range(height):
    #     for col in range(width):
    #         room = Room()
    #         map[row][col] = room
    return map


def show_map(map, player, radius=3):
    player_x = player.environment.x
    player_y = player.environment.y
    for row in range(len(map)):
        output = ""
        for col in range(len(map[row])):
            room = map[row][col]

            room_x = col 
            room_y = row
            if abs(room_x - player_x)**2 + abs(room_y - player_y)**2 <= radius**2:
                if room:
                    output += repr(room)
                else:
                    output += '[ ]'
            else:
                output += "   "
        print(output)

