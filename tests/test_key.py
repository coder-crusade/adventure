from adventure.items.key import Key
from adventure.lib.player import Player
from adventure.lib.room import Room

#=====TEST CONNECTION======
def test_import_Key():
    assert Key

def test_key_name():
    key = Key()
    assert key.name

def test_key_actions():
    key = Key()
    actual = list(key.actions.keys())
    expected = ['collect']
    assert actual == expected

def test_move_key_to_inventory(capsys):
    key = Key()
    player = Player()
    actual_1 = key.do_move_key_to_inventory('collect', key, player)
    expected_1 = True
    captured = capsys.readouterr()
    actual_2 = captured.out
    expected_2 = "You've collected the Key.\n"
    assert expected_1 == actual_1
    assert expected_2 == actual_2
