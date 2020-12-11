from adventure.items.torch import Torch
from adventure.lib.player import Player

def test_import():
    assert Torch

def test_torch_actions():
    torch = Torch()
    actual = list(torch.actions.keys())
    expected = ['collect']
    assert actual == expected

def test_move_torch_to_inventory(capsys):
    torch = Torch()
    player = Player()
    actual_1 = torch.do_move_torch_to_inventory('collect', 'torch', player)
    expected_1 = True
    captured = capsys.readouterr()
    actual_2 = captured.out
    expected_2 = "You've collected the Torch.\n"
    assert expected_1 == actual_1
    assert expected_2 == actual_2