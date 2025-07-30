"""
Построение промптов для LLM
"""
from game_state import GameState
from myengine.myllmengine import LLMEngine
from myengine.eventmanager import EventManager

class PromptBuilder:
    def __init__(self):
        self.action = EventManager()
        self.gamestate = GameState()
        self.llm = LLMEngine() 
        self.world = self.gamestate.world
        self.locname = self.gamestate.locname
        self.locdescription = self.gamestate.locdescription
        self.player = self.gamestate.player
        self.item = self.gamestate.item
        self.quest = self.gamestate.quest
        self.answer = None

    def build_prompt(self) -> str:

        inventory = ", ".join(self.item.itemname for self.item in self.player.inventory) or "нет предметов"
        quest = self.gamestate.quest

        prompt = f"""
Ты — ведущий текстовой ролевой игры. Игрок совершает действия, а ты описываешь, что происходит.

Игрок находится в локации: {self.locname}
Описание: {self.locdescription}

Инвентарь: {inventory}
Квест: {quest}
Характеристики: HP={self.player.hp}, Сила={self.player.dmg}

Игрок хочет: {self.action}

"""
        self.answer = self.llm.get_response(prompt).strip()

        print(f"{self.answer} промтптбббб промптбббб промптббб")

        return self.answer
