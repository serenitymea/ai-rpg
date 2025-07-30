from myengine.myllmengine import LLMEngine
from mymodels.npc import Character

class Enemy(Character):
    def __init__(self, world, item):
                
        self.llm = LLMEngine()
        self.world = world
        self.item = item
        ename, ehp, edmg = self.create_enemy()

        super().__init__(name = ename, hp = ehp, dmg = edmg)

        self.ename = ename
        self.edmg = edmg
        self.ehp = ehp

    def create_enemy(self):

        locname = self.world.locname
        locdescription = self.world.locdescription
        itemname = self.item.itemname
        
        ename_prompt = (
            f"Придумай короткое атмосферное название для врага текстовой RPG игры в локации {locname,locdescription}."
            f"С которого падает предмет {itemname}"
                        )
        self.ename = self.llm.get_response(ename_prompt).strip()

        edmg_prompt = f"Придумай дамаг который может нанести враг {self.ename} и напиши только цифру от одного до 100."
        self.edmg = int(self.llm.get_response(edmg_prompt).strip())

        enemyhp_prompt = f"Придумай количество здоровья врага {self.ename} и напиши только цифру от 1 до 100."
        self.ehp = int(self.llm.get_response(enemyhp_prompt).strip())

        print(f"{self.ename}{self.ehp}{self.edmg} енеми енеми енеми")
        return self.ename, self.edmg, self.ehp