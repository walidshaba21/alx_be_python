class Flyer:
    def fly(self):
        print("Flying...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Duck(Swimmer, Flyer):
    pass


duck = Duck()

duck.fly()
duck.swim()
        