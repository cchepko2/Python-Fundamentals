class Character():
    def __init__(self, name="Hero", health=100, attack=6, defence=1):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
    
    def __del__(self):
        pass

    def __str__(self):
        return f"{self.name} has {self.health} health" #, and can attack with {self.attack} and a defence of {self.defence}"
    
    def fight(self, the_other_guy):
        while(self.health > 0 and the_other_guy.health > 0):
            the_other_guy.health -= self.attack-the_other_guy.defence
            if(the_other_guy.health > 0):
                self.health -= the_other_guy.attack-self.defence

hero = Character()
print(hero)

villain = Character("Villain", 110, 4, 1)
print(villain)

villain.fight(hero)

print(hero)
print(villain)

