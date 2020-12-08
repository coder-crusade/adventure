from adventure.lib.room import Room


def test_import():
    assert Room


def test_two_rooms():
    room1 = Room()
    room2 = Room()
    room1.add_exit('north', room2)
    room2.add_exit('south', room1)
    assert room2.exits['south'] == room1
    assert room1.exits['north'] == room2
