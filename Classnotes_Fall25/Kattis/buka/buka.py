'''
Programmer: Corin Chepko
Date: 9/3/25
Program: Kattis problem - https://open.kattis.com/problems/buka
Alogorithm Steps:
    Input 1st number
    Input character
    Input 2nd number
    use 'eval' function to evaluate 1stnumber+character+2ndnumber
'''

number1 = input()
character = input()
number2 = input()

#print(f"{number1+character+number2=}")
answer = eval(number1+character+number2)
#print(f"{answer=}")

# Only print answer for Kattis
print(answer)