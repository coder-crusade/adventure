from adventure.monsters.rat import Rat
from adventure.lib.player import Player

#=====TEST CONNECTION======
def test_import_Rat():
    assert Rat

def test_rat_name():
    rat = Rat()
    assert rat.name

def test_rat_actions():
    rat = Rat()
    actual = list(rat.actions.keys())
    expected = ['search']
    assert actual == expected

def test_respond_to_hit(capsys):
    rat = Rat()
    player = Player()
    rat.respond_to_hit(player)
    captured = capsys.readouterr()
    actual = captured.out
    expected = "- - - Keep striking it! - - -\n"
    assert expected == actual

# def test_do_search_corpse(capsys):
#     rat = Rat()
#     player = Player()
#     rat.do_search_corpse('search', rat, player)
#     captured = capsys.readouterr()
#     actual = captured.out
#     expected = True
#     assert expected == actual
