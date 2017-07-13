class Animal(object):
    def __init__(self, texture, predator, legs, prey, breath, name):
        self.texture = texture
        self.predator = predator
        self.legs = legs
        self.prey = prey
        self.breath = breath
        self.name = name
    def iAm(self):
        print("i am a " + self.name)
    def iFeel(self):
        print("my texture is " + self.texture)
    def hunt(self):
        print("i eat " + self.prey)
    def drink(self):
        print("i drink " + self.prey + "'s juices.(insert evil laugh here)")
    def die(self):
        print("death by: " + self.predator)
    def iBreath(self):
        print("do i breathe? answer: " + self.breath)
    def leggy(self):
        print("i have " + self.legs + " legs")
roc = Animal(raw_input("texture\n"), raw_input("the predator\n"), raw_input("how many legs\n"), raw_input("what is it's prey\n"), raw_input("do i breathe?\n"), raw_input("what is my name\n"))
roc.iAm()
roc.iFeel()
roc.hunt()
roc.drink()
roc.die()
roc.iBreath()
roc.leggy()
class Unicorn(Animal):
    def __init__(self, texture, predator, legs, prey, breath, name, ability):
        self.texture = texture
        self.predator = predator
        self.legs = legs
        self.prey = prey
        self.breath = breath
        self.name = name
        self.ability = ability
    def iStillAm(self):
        print("i am a " + self.name)
    def iFelt(self):
        print("my texture is " + self.texture)
    def hunting(self):
        print("i eat " + self.prey)
    def drinker(self):
        print("i drink " + self.prey + "'s juices.(insert evil laugh here)")
    def died(self):
        print("death by: " + self.predator)
    def iBreathe(self):
        print("do i breathe? answer: " + self.breath)
    def leggyy(self):
        print("i have " + self.legs + " legs")
    def myAbility(self):
        print("something only i can do is i can " + self.ability)
uni = Unicorn(raw_input("texture\n"), raw_input("the predator\n"), raw_input("how many legs\n"), raw_input("what is it's prey\n"), raw_input("do i breathe?\n"), "i am a unicorn.", raw_input("what is my ability\n"))
uni.iStillAm()
uni.iFelt()
uni.hunting()
uni.drinker()
uni.died()
uni.iBreathe()
uni.leggyy()
uni.myAbility()

