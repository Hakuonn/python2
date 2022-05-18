import random


class Teacher:
    # constructor
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def eat(self):
        self.weight = self.weight+1

    def exercise(self):
        self.weight = self.weight-0.5
        self.height = self.height+0.1


hchung = Teacher("黃河銓", 70, 175)
print(hchung.name)
print(hchung.weight)
print(hchung.height)
hchung.eat()
hchung.exercise()

handsome = Teacher("黃天受", 88, 180)
print(handsome.name)
print(handsome.weight)
print(handsome.height)
for i in range(10):
    handsome.exercise()


class Student:
    def __init__(self, name, hp, ap):
        self.name = name
        self.hp = hp
        self.ap = ap

    def attack(self, uaker):
        uaker.hp = uaker.hp-self.ap

    def underattack(self, attacker):
        self.hp = self.hp-attacker.ap


aaa = Student("趙伯恩", 100, 100)
bbb = Student("陳亭蓁", 100, 100)

aaa.attack(bbb)
aaa.underattack(bbb)

print(aaa.hp)
print(bbb.hp)


class Hero:
    def __init__(self, name, hp, ap):
        self.name = name
        self.hp = hp
        self.ap = ap

    def attack(self, uaker):
        uaker.hp = uaker.hp-self.ap

    def underattack(self, attacker):
        self.hp = self.hp-attacker.ap


class Monster:
    def __init__(self, name, hp, ap):
        self.name = name
        self.hp = hp
        self.ap = ap

    def attack(self, uaker):
        uaker.hp = uaker.hp-self.ap

    def underattack(self, attacker):
        self.hp = self.hp-attacker.ap


hero = Hero("hero", 1000, 1000)
group = []
for i in range(10):
    group.append(Monster("monster"+str(i+1),
                 random.randint(80, 100), random.randint(10, 50)))
