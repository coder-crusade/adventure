from adventure.lib.room import Room
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

    def crawl(row, col, distance):
        if not distance:
            return

        if not map[row][col]:
            map[row][col] = Room()
        
        possible_directions = []

        if row - 1 >= 0:
            possible_directions.append('north')
        if row + 1 < len(map):
            possible_directions.append('south')
        if col - 1 >= 0:
            possible_directions.append('west')
        if col + 1 < len(map[row]):
            possible_directions.append('east')

        random_direction = random.choice(possible_directions)

        if random_direction == 'north':
            col -= 1
        elif random_direction == 'south':
            col += 1
        elif random_direction == 'east':
            row += 1
        # random_direction == 'west':
        else:
            row -= 1
        crawl(row, col, distance -1)
    
    crawl(0,0,20)

    # for row in range(height):
    #     for col in range(width):
    #         room = Room()
    #         map[row][col] = room
    print(map)


def show_map2(map):
    for row in range(len(map)):
        output = ""
        for col in range(len(map[row])):
            output += repr(map[row][col])
        print(output)

