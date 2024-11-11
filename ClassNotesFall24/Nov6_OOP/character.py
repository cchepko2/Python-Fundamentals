import random

class Hero:
    '''
    Hero class: Hero(health, attack)
    '''
    def __init__(self, name="Jerry", health=10, attack=3, shield=0, magic=0):
        self.name = name
        self.health = health
        self.attack = attack
        self.shield = shield
        self.magic = magic

    
    def __str__(self):
        return f"{self.name}:\nHealth = {self.health}, Attack = {self.attack}"
    
    def fight(self, hero2):
        my_attack = random.randint(0, self.attack)
        his_attack = random.randint(0, hero2.attack)
        while(hero2.health > 0 and self.health > 0):
            hero2.health -= my_attack
            if(hero2.health <= 0):
                return "You win, the imposter hero is dead!"
            self.health -= his_attack
            if(self.health <= 0):
                return "You died!"
    
    def defend(self, hero2):
        my_attack = random.randint(0, self.attack)
        his_attack = random.randint(0, hero2.attack)
        while(hero2.health > 0 and self.health > 0):
            self.health -= his_attack-self.shield
            if(self.health <= 0):
                return "You died!"
            hero2.health -= my_attack
            if(hero2.health <= 0):
                return "You win, the imposter hero is dead!"

xander = Hero("Xander", 15, 4)
that_other_guy = Hero("Jerry", 10, 3, 3)

print(xander)
print(that_other_guy) 
print()

#print(xander.fight(that_other_guy))
print(that_other_guy.defend(xander))

print(xander)
print(that_other_guy)

    