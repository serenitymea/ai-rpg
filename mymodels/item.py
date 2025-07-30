"""
item
"""
from myengine.myllmengine import LLMEngine

class Item:
    """ Класс для создания предметов в игре """
    def __init__(self, world):

        self.llm = LLMEngine()
        self.world = world
        self.itemname = None
        self.itemeffect = None
        self.create_item()


    def create_item(self) -> str:
        """Создание предмета с помощью LLM"""

        locname = self.world.locname

        itemname_prompt = (
            f"Придумаq короткое атмосферное название для предмета текстовой RPG игры"
            f"который находиться в локации '{locname} и выдай его в форме Вы получили предмет:'"
        )
        self.itemname = self.llm.get_response(itemname_prompt).strip()

        itemeffect_prompt = (
            f"Сгенерируй действие эффекта предмета для текстовой RPG игры"
            f"где у героя есть 100 хп и 10 дмг в локации '{locname}'"
        )
        self.itemeffect = self.llm.get_response(itemeffect_prompt).strip()

        print(f"{self.itemname}{self.itemeffect} итем итем итем")
