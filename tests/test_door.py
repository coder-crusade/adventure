from adventure.items.door import Door
from adventure.lib.player import Player

#=====TEST CONNECTION======
def test_import_Door():
    assert Door

def test_door_name():
  door = Door()
  assert door.name

def test_door_actions():
  door = Door()
  actual = list(door.actions.keys())
  expected = ['unlock']
  assert actual == expected

def test_do_unlock_door(capsys):
  door = Door()
  player = Player()
  actual_1 = door.do_unlock_door('unlock', door, player)
  expected_1 = True
  captured = capsys.readouterr()
  actual_2 = captured.out
  expected_2 = 'You must collect a key.\n'
  assert expected_1 == actual_1
  assert expected_2 == actual_2
