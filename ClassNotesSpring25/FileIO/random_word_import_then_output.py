from pathlib import Path
import random

import pathlib
import os
# If you want to keep numbers.txt in the same location as this lab... 
#my_path = pathlib.Path(__file__).parent.resolve()
#with open(f'{my_path}/numbers.txt m', 'r') as my_file:

current_file_path = Path(__file__)
#convert current_file_path to a string and add a '\'
# If running Python in a Windows environment, use a '\\', if in a Linux environment (Codespace), 
# use '/' to divide file path from file name.


# For windows based python, add a backslash, using double \\ because backslash is an escape charater
# For Codespace or linux/Mac, use a forward slash
current_file_path = str(current_file_path.parent) + '/'

def input_word(filename: str) -> str:
    '''
    Inputs a filename including path. Output string containing
    random_word.
    '''
    with open(filename) as fin:
        words = fin.readlines()
        random_word = random.choice(words)
        random_word = random_word.strip().lower()
        #num_words_in_file = len(words)
        return random_word
    
def write_game_file(filename: str, stats: tuple):
    # Unpack stats tuple into it's values
    (num_games, num_wins) = stats

    if os.path.exists(filename):
        print(f"File '{filename}' exists.")
        with open(filename) as fin:
            data = fin.readline().split()
            file_games = int(data[2])
            file_wins = int(data[6])
            print(f"{file_games=}, {file_wins=}")
            num_games += file_games
            num_wins += file_wins

    else:
        print(f"File '{filename}' does not exist.")

    with open(filename, "w") as fout:
        fout.write(f"You played {num_games} time and won {num_wins}\n")
        fout.write(f"Your win ratio is {num_wins/num_games}\n")

def main():
    name = input("Who is playing?")
    stats = (num_games, num_wins) = (0,0)
    print(f"{stats=}")

    while(True):
        filename = current_file_path + "words.txt"
        word_of_the_game = input_word(filename)
        print(f"Random word of the game is {word_of_the_game}")

        num_wins += 1
        num_games += 1

        again = input("Play again? (y/n)")
        if( again.lower() == 'n'):
            break

    out_file = current_file_path + name + ".txt"
    stats = (num_games, num_wins)
    write_game_file(out_file, stats)

    print("Thanks for playing!")

if __name__ == "__main__":
    main()