class Traits:
    def __init__(self, strength=0, magic=0, street_smarts=0):
        self.strength = strength
        self.magic = magic
        self.street_smarts = street_smarts
    
    def __str__(self):
        return_str = "Here are your traits:\n"
        return_str += f"Strength = {self.strength}\n"
        return_str += f"Magic = {self.magic}\n"
        return_str += f"Street Smarts = {self.street_smarts}\n"
        return return_str


def question(player):
    print("What kind of Music do you like?")
    print("A: Angry and Unromantic")
    print("B: Something else")

    choice = input("Enter the letter for your selection: ")

    if(choice.upper() == 'A'):
        player.magic += 1
        player.strength -= 1

def main():
    player = Traits()
    print(player)

    question(player)

    print("Your new score is: ")
    print(player)


main()