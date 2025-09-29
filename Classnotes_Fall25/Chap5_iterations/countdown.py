# while loop - countdown
import time
import os

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

i = 10
while i >= 1:
    print(i)
    time.sleep(1) # sleep for 1 second
    clearScreen()
    i -= 1
    
time.sleep(0.3)
print('Hapy new year!')