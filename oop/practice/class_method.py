class Person:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod 
    def display_count(cls):
        print(f"Total person created: {cls.count}")

person1 = Person("Alice")
person2 = Person("Bob")

Person.display_count()