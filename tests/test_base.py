from adventure.lib.base_obj import Base


def test_import():
    assert Base


def test_environment():
    obj = Base()
    target = Base()

    obj.move(target)

    assert obj.environment == target


def test_inventory():
    obj = Base()
    target = Base()

    obj.move(target)

    assert obj in target.inventory
