from adventure.lib.player import Player
from adventure.lib.map import show_map, connect_rooms, dungeon_maker
from adventure.lib.room import Room

def test_10_by_10():
    x = dungeon_maker(10,10)
    assert len(x) == 10
    assert len(x[0]) == 10

def test_print_map():
    map = dungeon_maker(10,10)
    tom = Player()
    tom.move(map[0][0])
    assert show_map(map, tom) == None