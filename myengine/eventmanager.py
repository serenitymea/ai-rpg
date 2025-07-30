"""
интерпретация действий
"""
from game_state import GameState
from myengine.myllmengine import LLMEngine

class EventManager:
    def __init__(self):
        self.gamestate = GameState()
        self.llm = LLMEngine()
        self.player = self.gamestate.player
        self.inventory = self.gamestate.player.inventory
        self.quest = self.gamestate.quest
        self.world = self.gamestate.world
        self.enemy = self.gamestate.enemy
        self.item = self.gamestate.item
        self.eventresult = None
        self.res= None
        self.ress= None
        self.itemname = None
        self.uuu = None
        self.action = input("Что будете делать:")

    def item_pick(self) -> bool:
        prompt = (
            f"Игрок {self.player} находится в {self.world}."
            f"Он делает: '{self.action}' в квесте {self.quest}. он дереться с врагом {self.enemy}"
            f"и он может получить или не получить предмет в зависимости от {self.action}."
            f"Если он получит предмет то отправь 0 если не получит то 1 "
        )
        self.res = int(self.llm.get_response(prompt).strip())
        if self.res == 0:
            return True
        else:
            return False
    def taken_damage(self) -> int:
        prompt = (
            f"Игрок {self.player} находится в {self.world}."
            f"Он делает: '{self.action}' в квесте {self.quest}. он дереться с врагом {self.enemy}"
            f"и он может получить или не получить урон от врага в зависимости от {self.action}."
            f"Если он получит то отправь количество урона от 0 до 100 "
        )
        self.ress = int(self.llm.get_response(prompt).strip())

        print(f"{self.ress} ивент ивент ивент")
        return self.ress

    def add_item(self):
        self.uuu = EventManager.item_pick(self)
        self.itemname = self.gamestate.item
        if self.uuu is True:
            self.inventory.append(self.itemname)

