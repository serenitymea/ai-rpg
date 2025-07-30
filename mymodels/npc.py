"""
npc
"""
class Character:
    def __init__(self, name: str, hp: int, dmg: int):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def is_alive(self) -> bool:
        return self.hp > 0
