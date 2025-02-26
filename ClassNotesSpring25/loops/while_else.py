# While else example

play_again = 'y'
score = 0

while play_again.lower() == 'y':
    print("Playing the game...")

    won = input("Did you win?")
    if( won.lower() == 'y' ):
        print("Great job! Want to play again? (y/n)")
        #score += 1
        score = score + 1
        play_again = input()
    else:
        print("You lost. Ending Program.")
        break
else: # while loop did not break
    print("The while loop was not broken with a break statement, and you are the winner!")
    print(f"{score=}")
    