from adventure.monsters.guard import Guard
from adventure.lib.room import Room
from adventure.lib.player import Player

def test_import():
    assert Guard
    assert Room

def test_guard_moves():
    room1 = Room()
    room2= Room()
    room1.add_exit('west', room2)
    room2.add_exit('east', room1)

    player = Player()
    
    guard = Guard()
    guard.move(room1)
    guard.choose_action(player)

    actual = guard.environment
    expect = room2
    assert actual == expect
