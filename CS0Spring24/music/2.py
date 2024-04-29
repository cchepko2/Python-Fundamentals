import time
import random
from pygame import mixer

class goblin:
    def __init__(self, hitpoints=10, attack_pow=5):
        self.hitpoints = hitpoints
        self.attack_pow = attack_pow

    def attack(self):
        return random.randint(1,self.attack_pow)
    
    def defend(self, damage):
        self.hitpoints -= damage
    
    def battle_music_start(self):
        music = "TubePocket.mp3"
        mixer.init()
        mixer.music.load(music)
        mixer.music.play(-1)
    
    def end_battle_music(self, fadeout_ms):
        mixer.music.fadeout(fadeout_ms)
        time.sleep(fadeout_ms/1000)


goblin1 = goblin(11,5)
my_hitpoints = 10

print(goblin1.hitpoints,goblin1.attack_pow)

y = input("Ready for battle?")
if( y == 'y' or y == 'Y'):
    goblin1.battle_music_start()
    while(True):
        input("Press enter to attack")
        attack = random.randint(1,5)
        goblin1.defend(attack)
        print("The goblin has {} left.".format(goblin1.hitpoints))
        
        if(goblin1.hitpoints > 0):
            input("Press enter to defend.")
            my_hitpoints -= goblin1.attack()
            print("The goblin attacked. You have {} left.".format(my_hitpoints))
        else:
            print("You win!")
            goblin1.end_battle_music(2000)
            break
        if(my_hitpoints <= 0):
            print("You have been defeated!")
            goblin1.end_battle_music(2000)
            break



