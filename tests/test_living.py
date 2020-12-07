from adventure.lib.living import Living
from adventure.lib.base_obj import Base

def test_import():
  assert Living

def test_hit():
  obj = Living()
  obj.hit(6)
  assert obj.health == 4

def test_heal():
  obj = Living()
  obj.hit(5)
  obj.heal(100)
  assert obj.health == 10

def test_is_alive():
  obj = Living()
  obj.hit(13)
  assert obj.is_alive() == False


  