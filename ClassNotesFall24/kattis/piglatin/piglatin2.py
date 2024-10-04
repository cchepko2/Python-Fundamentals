'''
Author: Corin Chepko
Date: 10/2/24
Program Info: kattis problem - https://open.kattis.com/problems/piglatin
Algorithm Steps:
    while(input a phrase):
        for each word in phrase:
            if word begins with consonent take all letters
            before first vowel and move to end of word. Add "ay" to end

            if word begins with vowel (aeiouy) add "yay" to end of word

'''
import sys

def translate(phrase):
    pig_latin = ""
    vowels = "aeiouy"

    words = phrase.split() # words is a list of the words in the phrase
    #print(words)

    for word in words:
        if word[0] in "aeiouy":  # if it begins with a vowel
        # both if statements are equivalent
        #if word.startswith(("a","e","i","o","u","y")):
            new_word = word+"yay"
        else:
            #new_word = word
            index = 0
            for char in word:
                index += 1
                if char in vowels: # found first vowel
                    new_word = word[index-1::] + word[0:index-1] + "ay"
                    break
        pig_latin += new_word + ' '

    return pig_latin

def main():

    #while(True):
    #    sys.stdin()
    #    try:
    #        phrase = input()
    #    except EOFError:
    #        break
        #phrase = input()
    for phrase in sys.stdin:    
        # for user testing, if last line is blank end program
       # if(phrase == ""):
       #     break

        pig_latin = translate(phrase)

        print(pig_latin)



if __name__ == "__main__":
    main()