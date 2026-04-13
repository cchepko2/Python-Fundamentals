class Character:
    def __init__(self, name="Default", health=10, attack=3, defence=1):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
    
    def __del__(self):
        pass

    def __str__(self):
        return f'{self.name} has {self.health} health.'
    
    def fight(self, other_guy):
        while(other_guy.health > 0 and self.health > 0):
            other_guy.health -= self.attack-other_guy.defence
            if(other_guy.health > 0):
                self.health -= other_guy.attack-self.defence


def main():
    corin = Character("Corin", 99, 10, 5)
    monster = Character()

    print(corin)
    print(monster)

    corin.fight(monster)

    print(corin)
    print(monster)        

if __name__ == '__main__':
    main()