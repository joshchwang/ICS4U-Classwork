class Person:
    """
    Attrs:
        name (str): First and Last
        height (int): in cm
        strength (int): How strong the person is
        health_points (int): Out of 100 (everyone starts at 100)
    """
    def __init__(self, name, height, strength):
        self.name = name
        self.height = height
        self.strength = strength
        self.health_points = 100

    def __str__(self):
        return f"{self.name}, hp: {self.health_points}"

    def introduce(self):
        print(f"Hello, my name  is {self.name}.")

    def punch(self, person):
        damage = self.strength / person.strength * 10
        print(f"{self.name} punches {person.name}")
        if self == person:
            self.health_points -= 5 + self.strength
        else:
            person.health_points -= damage
    def eat(self):
        self.health_points = 100


jeff = Person("Jeff Blah", 170, 1)
david = Person("David Greenchair", 200, 1)

print(jeff)
print(david)

jeff.introduce()
david.introduce()

david.punch(jeff)
david.punch(david)

print(jeff)
print(david)