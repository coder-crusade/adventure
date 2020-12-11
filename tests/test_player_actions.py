from adventure.lib.player import Player
from adventure.lib.room import Room


def test_import():
    assert Player
    assert Room


def test_move():
    p = Player()
    r1 = Room()

    p.move(r1)

    assert p.environment == r1
    assert p in r1.inventory


def test_move_action_n():
    p = Player()
    r1 = Room()
    r2 = Room()

    r1.add_exit('north', r2)
    r2.add_exit('south', r2)

    p.move(r1)
    assert p.environment == r1

    p.action('north')
    assert p.environment == r2


# def test_move_action_north():


# def test_move_action_n_into_wall():
