class Vehicle:
    def move(self):
        print("Moving...")
    
class Car(Vehicle):
    pass

class Electric_Car(Car):
    def charge(self):
        print("Charging...")

tesla = Electric_Car()
tesla.move()
tesla.charge()