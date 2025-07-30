"""
quest
"""
from myengine.myllmengine import LLMEngine

class Quest:
    def __init__(self, world, enemy, item):
        self.world = world
        self.enemy = enemy
        self.item = item
        self.llm = LLMEngine()
        self.quest = None
        self.questdesc = None
        self.add_quests()


    def add_quests(self):


        ename = self.enemy.ename
        itemname = self.item.itemname
        locname = self.world.locname
        locdescription = self.world.locdescription

        quest_prompt = f"Придумай квест для текстовой RPG игры в локации {locname, locdescription} где игрок получит предмет {itemname} и встретит врага {ename}."
        self.questn = self.llm.get_response(quest_prompt).strip()

        questdesc_prompt = f"Сгенерируй описание квеста с именем '{self.questn}' в локации {locname, locdescription} где игрок получит предмет {itemname} и встретит врага {ename}."
        self.questdesc = self.llm.get_response(questdesc_prompt).strip()
       
        print(f"{self.questn}{self.questdesc} квест кевст квест")
        return self.questn, self.questdesc