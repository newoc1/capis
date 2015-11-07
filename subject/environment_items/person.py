class Person:

    def __init__(self, health):
        self.health = health

    def damage(self, damage):
        print("I've been hit!")
        self.health = self.health - damage