import random

jerry_art = r'''
       !
      .-.
    __|=|__
   (_/`-`\_)
   //\___/\\
   <>/   \<>
    \|_._|/
     <_I_>
      |||
jgs  /_|_\
'''

xander_art = r'''
  / \
  | |
  |.|
  |.|
  |:|      __
,_|:|_,   /  )
  (Oo    / _I_
   +\ \  || __|
      \ \||___|
        \ /.:.\-\
         |.:. /-----\
         |___|::oOo::|
         /   |:<_T_>:|
        |_____\ ::: /
         | |  \ \:/
         | |   | |
         \ /   | \___
         / |   \_____\
         `-'
'''

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
        self.art = ''''''

    
    def __str__(self):
        return f"{self.name}:\nHealth = {self.health}, Attack = {self.attack}\n{self.art}"
    
    def heal(self):
        self.health += self.magic
        self.magic = 0

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
        
        while(hero2.health > 0 and self.health > 0):
            my_attack = random.randint(0, self.attack)
            his_attack = random.randint(0, hero2.attack)
            
            choice = input(f"It's your next turn, what should you do? (Attack, Heal)")
            if(choice == 'A'):
                if(his_attack > self.shield):
                    self.health -= his_attack-self.shield
            elif(choice == 'H'):
                self.heal()
            else:
                # our hero decides to take a break
                pass
            
            if(self.health <= 0):
                return f"{self.name} died!"
            hero2.health -= my_attack
            if(hero2.health <= 0):
                return f"{self.name} wins, the imposter hero is dead!"

xander = Hero("Xander", 15, 4)
xander.art = xander_art
that_other_guy = Hero("Jerry", 3, 3, 3)
that_other_guy.art = jerry_art


story = f'''{that_other_guy.name} was walking in the woods, minding his own buisness...
when an ugly SOB named {xander.name} tries to mug him! {that_other_guy.name} has no choice but to defend himslef.'''

print(story)
print(f'{xander.name} strikes the first blow!')

print(that_other_guy.defend(xander))
print(xander)
print(that_other_guy)



    