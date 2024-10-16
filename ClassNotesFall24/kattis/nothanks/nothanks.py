'''
Author: Corin Chepko and Class
Date: 10/16/24
Program info: kattis problem - No Thanks - https://open.kattis.com/problems/nothanks
Algoithm Steps:
    Collect all numbers into a list
    Set score = 0
    Set first_val = first number in list
    for every next number:
        if incremented by 1 from previous number:
            don't change first_val
        else:
            add first_val to score
            set new first val to current number
    Profit
'''

def main():
    num_cards = int(input())
    numbers = input().split()
    numbers = list( map(int, numbers) )

    print(numbers) # verify we got our numbers

    numbers.sort() # sort numbers list in ascending order
    #print(numbers)

    tot_score = 0
    first_score = numbers[0]
    previous = numbers[0]
    
    for i in range(1,num_cards):
        if(numbers[i] == previous+1):
            tot_score += first_score
        else: # incremented by more than 1
            #tot_score += first_score
            first_score = numbers[i]
            #print("Current score = ", tot_score)
            #print("new first_score = ", first_score)

            if i == num_cards-1: # this is the last card and its more than 1 increment from last card
                tot_score += numbers[i]
        
        previous = numbers[i]
    


    print(tot_score)

if __name__ == "__main__":
    main()