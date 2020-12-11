from adventure.lib.room import Room
from adventure.monsters.rat import Rat
from adventure.lib.player import Player


def test_import():
    assert Room


def test_two_rooms():
    room1 = Room()
    room2 = Room()
    room1.add_exit('north', room2)
    room2.add_exit('south', room1)
    assert room2.exits['south'] == room1
    assert room1.exits['north'] == room2

def test_show_room_with_obj(capsys):
    room = Room()
    room_west = Room()
    room_east = Room()
    room.add_exit('east', room_east)
    room.add_exit('west', room_west)
    player = Player()
    player.move(room)
    rat = Rat()
    rat.move(room)
    room.do_show_room()  
    capture = capsys.readouterr() 
    assert capture.out == "A sparse room with a cold stone floor.\n Directions available: east, west.\nThe room contains:\n  Rat\n\n"


def test_visible_look_without_obj(capsys):
    room = Room()
    room_west = Room()
    room_east = Room()
    room.add_exit('east', room_east)
    room.add_exit('west', room_west)
    room.inventory = []
    room.do_show_room() 
    capture = capsys.readouterr() 
    assert capture.out == "A sparse room with a cold stone floor.\n Directions available: east, west.\nThe room contains:\n \n"