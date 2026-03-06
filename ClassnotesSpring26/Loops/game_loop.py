def game(wins, num_played):
    while True:
        num_played += 1
        wins += 1

        print("You win! Want to play again? (Y/N)")
        again = input()
        if again.upper()[0] == 'Y':
            continue
        else:
            print("Exiting...")
            return wins, num_played

    

def main():
    wins = 0
    num_played = 0

    wins, num_played = game(wins, num_played)
    print(f"You played {num_played} times and won {wins} times!")

main()