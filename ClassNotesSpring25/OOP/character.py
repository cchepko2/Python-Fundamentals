import random

class Character:
    def __init__(self, name="Nobody", health=10, attack=5):
        self.name = name
        self.health = health
        self.attack = attack
    
    def __str__(self):
        return f"{self.name} has health of {self.health}"
    
    def fight(self, someone_else):
        while(self.health > 0 and someone_else.health > 0):
            someone_else.health -= random.randint(1, self.attack)
            if(someone_else.health > 0):
                self.health -= random.randint(1, someone_else.attack)
        if(self.health < 0):
            return "You died"
        else:
            return "Victory!"

hero = Character("Xandar", 15, 7)
monster1 = Character("Smeagle")

print("Breathtaking story...")
print(hero.fight(monster1))
print(hero)
print(monster1)