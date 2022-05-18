class hero:
    def __init__(self,name,hp,ap):
        self.name=name
        self.hp=hp
        self.ap=ap

    def plus(self):
        self.hp+=500
        self.ap+=200

    def attack(self,uaker):
        uaker.hp-=self.ap

    def underattack(self,attacker):
        self.hp-=attacker.ap

class monster:
    def __init__(self,name,hp,ap):
        self.name=name
        self.hp=hp
        self.ap=ap

    def attack(self,uaker):
        uaker.hp-=self.ap

    def underattack(self,attacker):
        self.hp-=attacker.ap

    def plus(self):
        self.hp+=500
        self.ap+=200

hakuonn=hero('Hakuonn',5000,2000)
gojira=[]
for i in range(1,5+1):
    gojira.append(monster('gojira'+str(i) , 500 , 600))


hakuonn.attack(gojira[0])
hakuonn.attack(gojira[1])
hakuonn.attack(gojira[1])


for i in range(5):
    gojira[i].plus()

print(hakuonn.name,hakuonn.hp,hakuonn.ap)
for i in range(5):
    print(gojira[i].name,gojira[i].hp)