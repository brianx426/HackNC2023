class Move:
  name: str
  description: str
  damage: int
  cooldown: int
  is_aoe: bool


  def __init__(self, name: str, description: str, damage: int, cooldown: int,
               is_aoe: bool) -> None:
    self.name = name
    self.description = description
    self.damage = damage
    self.cooldown = cooldown
    self.is_aoe = is_aoe