'''
Author: Corin Chepko
Date:9/18/24
Program Info: kattis problem - https://open.kattis.com/problems/spavanac
Algoithm Steps:
    input hours and minutes separated by a space
    convert to ints
    conver hours and minutes to total_minutes after midnight
    subtract 45 from total_minutes
    convert back to hours and minutes
    print(hours,minutes)
'''
def solution(hours, minutes):
    total_minutes = hours*60 + minutes

    total_minutes -= 45

    hours = ((total_minutes//60)+24)%24
    minutes = total_minutes%60

    # if hours less than zero, add 24 to convert to positive time the day before
    #if(hours < 0):
    #    hours += 24
    return hours, minutes

def main():
    hours, minutes = input().split()
    hours, minutes = map(int, (hours, minutes))

    hours, minutes = solution(hours, minutes)    

    print(hours, minutes)


if __name__ == "__main__":
    main()