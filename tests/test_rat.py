from adventure.monsters.rat import Rat
from adventure.lib.player import Player
from adventure.lib.room import Room

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

# capsys contributed by Skyler Burger
def test_respond_to_hit(capsys):
    rat = Rat()
    player = Player()
    rat.respond_to_hit(player)
    captured = capsys.readouterr()
    actual = captured.out
    expected = "- - - Keep striking it! - - -\n"
    assert expected == actual

def test_do_search_corpse(capsys):
    rat = Rat()
    room = Room()
    player = Player()
    rat.move(room)
    player.move(room)
    actual = rat.do_search_corpse('search', 'rat', player)
    expected = True
    assert expected == actual
    

def test_hit(capsys):
    rat = Rat()
    rat.hit(1)
    rat.hit(1)
    captured = capsys.readouterr()
    actual = captured.out
    expected = "Rat has died!\nPerhaps you can 'Search Rat'\n"
    assert expected == actual
