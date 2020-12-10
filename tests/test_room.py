from adventure.lib.room import Room
from adventure.monsters.rat import Rat


def test_import():
    assert Room


def test_two_rooms():
    room1 = Room()
    room2 = Room()
    room1.add_exit('north', room2)
    room2.add_exit('south', room1)
    assert room2.exits['south'] == room1
    assert room1.exits['north'] == room2

def test_visible_look_with_obj(capsys):
    room = Room()
    rat = Rat()
    room.inventory = [rat]
    room.do_visible_look()  
    capture = capsys.readouterr() 
    assert capture.out == "The room contain:\n Rabies Rat\n.\n"

def test_visible_look_without_obj(capsys):
    room = Room()
    room.inventory = []
    room.do_visible_look() 
    capture = capsys.readouterr() 
    assert capture.out == "The room is empty!\n"