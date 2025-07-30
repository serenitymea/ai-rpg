"""
world
"""
from myengine.myllmengine import LLMEngine

class World:
    def __init__(self):

        self.llm = LLMEngine()
        self.locname = None
        self.locdescription = None
        self.add_location()
    
    def add_location(self):
        locname_prompt = "Придумай короткое атмосферное название для стартовой локации текстовой RPG игры."
        self.locname = self.llm.get_response(locname_prompt).strip()

        locdesc_prompt = f"Сгенерируй атмосферное описание стартовой локации для текстовой RPG игры с названием '{self.locname}'."
        self.locdescription = self.llm.get_response(locdesc_prompt).strip()
        print(f"{self.locname}{self.locdescription} мир мир мир мир")

        return self.locname, self.locdescription