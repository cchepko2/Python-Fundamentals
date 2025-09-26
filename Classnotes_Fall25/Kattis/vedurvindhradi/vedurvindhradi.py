'''
Corin Chepko
9/26/25
Program - Kattis problem - https://open.kattis.com/problems/vedurvindhradi
Algorithm:
    input float number
    compare to table:
        if speed < 0.2:
            ans = "Logn"
        elif speed < 1.5:
            ans = "Andvari"
        elif speed < 3.3:
            ans = "Kul"
        elif speed < 5.4:
            ans = "Gola"
        elif speed < 7.9:
            ans = "Stinningsgola"
        elif speed < 10.7:
            ans = "Kaldi"
        elif speed < 13.8:
            ans = "Stinningskaldi"
        elif speed < 17.1:
            ans = "Allhvass vindur"
        elif speed < 20.7:
            ans = "Hvassvidri"
        elif speed < 24.4:
            ans = "Stormur"
        elif speed < 28.4:
            ans = "Rok"
        elif speed < 32.6:
            ans = "Ofsavedur"
        else:
            ans = "Farvidri"
'''

speed = float(input())

if speed <= 0.2:
    ans = "Logn"
elif speed <= 1.5:
    ans = "Andvari"
elif speed <= 3.3:
    ans = "Kul"
elif speed <= 5.4:
    ans = "Gola"
elif speed <= 7.9:
    ans = "Stinningsgola"
elif speed <= 10.7:
    ans = "Kaldi"
elif speed <= 13.8:
    ans = "Stinningskaldi"
elif speed <= 17.1:
    ans = "Allhvass vindur"
elif speed <= 20.7:
    ans = "Hvassvidri"
elif speed <= 24.4:
    ans = "Stormur"
elif speed <= 28.4:
    ans = "Rok"
elif speed <= 32.6:
    ans = "Ofsavedur"
else:
    ans = "Farvidri"

print(ans)