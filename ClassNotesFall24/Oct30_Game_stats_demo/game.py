import word_and_save_game as read_words
import random

def run_game(words):
    word_of_day = random.choice(words)
    return random.choice(["You win", "You lose", "Tied!"])


def main():
    print("Welcome to my game!")
    user = input("Enter your username: ")
    stats = list(read_words.get_user_stats(user))
    print(f"User stats: {stats}")

    while(True):
        words = read_words.get_words("words.txt")
        stat = run_game(words)
        print(stat)

        if stat == "You win":
            stats[0] += 1 # increment game counter
            stats[1] += 1 # increment wins
        elif stat == "You lose":
            stats[0] += 1 # increment game counter
        else:
            # tied
            stats[0] += 1 # increment game counter
            stats[2] += 1 # increment ties


        print("Your latest stats: ")
        print(stats)

        again = input("Do you want to play again (y/n)?")
        if( again.upper() != 'Y'):
            break
    # End while(game) loop
    read_words.write_user_stats(user, stats)

if __name__ == "__main__":
    main()