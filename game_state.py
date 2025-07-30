"""
логика запуска и цикла
"""
from mymodels import Player, World, Enemy, Item, Quest
from myengine.myllmengine import LLMEngine

class GameState:
    def __init__(self):
        self.llm = LLMEngine()
        self.world = World()
        self.item = Item(self.world)
        self.enemy = Enemy(self.world, self.item)
        self.quest = Quest(self.world, self.enemy, self.item)
        self.player = Player.create_player()

        self.locname = self.world.locname
        self.locdescription = self.world.locdescription

        self.loc = None
        self.player_pos = 0

        print("shluha sluha shluha")


    def move_player(self, player_poss: int) -> str:

        if player_poss == 0:
            self.locname, self.locdescription = self.world.add_location()
            self.loc = self.locname, self.locdescription
            print(f"Вы находитесь в локации: {self.loc}")

        else:
            self.locname, self.locdescription = self.world.add_location()
            self.loc = self.locname, self.locdescription
            print(f"Вы переместились в локацию: {self.loc}")

        return self.loc