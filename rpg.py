class Personaje:

    def __init__(self):
        self.hp = 1000
        self.level = 1
        self.is_alive = True

    def attack (self, objetivo, damage):

        if self.is_alive == False:
            return

        objetivo.hp -= damage

        if objetivo.hp < 0:
            objetivo.hp = 0
            objetivo.is_alive = False
        return objetivo.hp


    def heal (self, objetivo, cured_quantity):

        if self.is_alive == False:
            return 

        objetivo.hp += cured_quantity

        if objetivo.hp > 1000:
            objetivo.hp = 1000

        return objetivo.hp