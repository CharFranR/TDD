class Personaje:
    def __init__(self):
        self.hp = 1000
        self.nivel = 1
        self.esta_vivo = True

    def atacar(self, objetivo, dano):
        objetivo.hp -= dano
        if objetivo.hp <= 0:
            objetivo.hp = 0
            objetivo.esta_vivo = False


    def heal(self, objetivo, heal_q): 



        objetivo.hp += heal_q
        
        if objetivo.hp > 1000:
            objetivo.hp = 1000
