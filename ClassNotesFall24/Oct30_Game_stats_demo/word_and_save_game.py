import pathlib
import random
import os

my_path = pathlib.Path(__file__).parent.resolve()

def get_words(filename):
    # This line opens the file, and when the with scope is over, automatically
    # closes the file
    filename = f'{my_path}/{filename}'
    if os.path.exists(filename):
        with open(filename, 'r') as my_file:
            words = my_file.read().split('\n')

            return words
    else:
        print(f"Cannot find words file: {filename}")
        return []
    #print("Finished with file!")
    #print(words)

    #print(f"Random word of this program run is: {random.choice(words)}")

def get_user_stats(user):
    user = f"{my_path}/{user}"

    if os.path.exists(user):
        with open(user, 'r') as my_file:
            line = my_file.readline().split()
            played = int(line[1])
            line = my_file.readline().split()
            won = int(line[1])
            line = my_file.readline().split()
            tied = int(line[1])
            return (played, won, tied)
    else:
        # user does not exist
        return (0,0,0)

def write_user_stats(user, stats):
    user = f"{my_path}/{user}"

    with open(user, 'w') as my_file:
        my_file.write(f"Played: {stats[0]}\n")
        my_file.write(f"Won: {stats[1]}\n")
        my_file.write(f"Ties: {stats[2]}\n")