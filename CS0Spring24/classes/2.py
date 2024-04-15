class Champian:
    def __init__(self, name, health=5, damage=2):
        self.name = name
        self.health = health
        self.damage = damage
    
    def __str__(self):
        if(self.health <= 0):
            return f"{self.name} is dead."
        return f"{self.name} has {self.health} health and can inflict {self.damage} damage."

    def attack(self, else_person):
        else_person.health = else_person.health-self.damage
    
    def defend(self, else_person):
        self.health = self.health - else_person.damage
    


def main():
    print('\n\n')
    ralphie = Champian("Ralphie")
    xander = Champian("Xander", 7, 3)

    print(ralphie)
    print(xander)

    print(f"\n{ralphie.name} and {xander.name} get in an encounter!")

    while(xander.health >= 0 and ralphie.health >= 0):
        xander.defend(ralphie)
        print(ralphie)
        print(xander)

        xander.attack(ralphie)
        print(ralphie)
        print(xander)


if __name__ == '__main__':
    main()