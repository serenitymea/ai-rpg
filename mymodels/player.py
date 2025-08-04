"""
player
"""
from mymodels.npc import Character

class Player(Character):
    def __init__(self, name: str, hp: int, dmg: int):
        super().__init__(name, hp, dmg)
        self.inventory = []

    @staticmethod
    def create_player():
        #name = input("Введите имя персонажа: ")
        name = "serenity"
        return Player(name = name, hp=100, dmg=10)
