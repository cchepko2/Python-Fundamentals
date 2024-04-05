def guess_letter(letter_guessed):
    guess = input("Guess a letter: ")
    if guess in letter_guessed:
        letter_guessed[guess] += 1
    else:
        letter_guessed[guess] = 1

def guess_letter_copy(letter_guessed):
    new_guess = letter_guessed.copy()
    guess = input("Guess a letter: ")
    if guess in letter_guessed:
        new_guess[guess] += 1
    else:
        new_guess[guess] = 1

    return new_guess

def main():
    letters_guessed = {}

    for _ in range(6):
        #guess_letter(letters_guessed)
        letters_guessed = guess_letter_copy(letters_guessed)
    
    print(letters_guessed)

if __name__ == "__main__":
    main()