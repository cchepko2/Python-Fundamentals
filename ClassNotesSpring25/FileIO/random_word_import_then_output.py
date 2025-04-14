from pathlib import Path
import random

current_file_path = Path(__file__)
#convert current_file_path to a string and add a '\'
# If running Python in a Windows environment, use a '\\', if in a Linux environment (Codespace), 
# use '/' to divide file path from file name.


# For windows based python, add a backslash, using double \\ because backslash is an escape charater
# For Codespace or linux/Mac, use a forward slash
current_file_path = str(current_file_path.parent) + '\\'

def input_word(filename):
    with open(current_file_path + filename) as fin:
        words = fin.readlines()
        choice = random.choice(words)
        choice = choice.strip().lower()
        num_words_in_file = len(words)
        return (choice, num_words_in_file)

def main():
    name = input("Who is playing?")
    stats = (num_games, num_wins) = (0,0)
    print(f"{stats=}")

    while(True):
        filename = "words.txt"
        word_of_the_game, num_words = input_word(filename)
        print(f"The number of words in {filename} is {num_words}")
        print(f"Random word of the game is {word_of_the_game}")

        num_wins += 1
        num_games += 1

        again = input("Play again? (y/n)")
        if( again.lower() == 'n'):
            break

    out_file = current_file_path + name + ".txt"
    with open(out_file, "w") as fout:
        fout.write(f"{name}\n")
        fout.write(f"You played {num_games} time and won {num_wins}\n")
        fout.write(f"Your win ratio is {num_wins/num_games}\n")
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()