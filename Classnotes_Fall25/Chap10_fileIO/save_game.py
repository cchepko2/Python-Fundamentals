import random
import os

script_dir = os.path.dirname(__file__)

def main():
    numbers = [1, 2, 3]
    wins = 0
    games = 0

    while(True):
        games += 1
        random_number = random.choice(numbers)

        print("Guess the number (1-3): ")
        guess = int(input())

        if guess == random_number:
            print("You win!")
            wins += 1
        else:
            print("You lose.")
        
        again = input("Play again? (y/n): ")

        if( again[0].lower() != 'y' ):
            stats = (wins, games - wins, games)
            save_game(stats)
            break # game is over

def save_game(stats):
    filename = script_dir + '\\save.txt'
    with open(filename, 'w') as fout:
        fout.write(f"Wins: {stats[0]}\n")
        fout.write(f"Loses: {stats[1]}\n")
        fout.write(f"Games: {stats[2]}")

if __name__ == '__main__':
    main()