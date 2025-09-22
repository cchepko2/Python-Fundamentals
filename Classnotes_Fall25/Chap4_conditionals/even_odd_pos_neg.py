# program that determines if a given number is even or odd, positive or negative 
num = int(input("Enter a number: "))

if num == 0:
    print(f'{num} is zero!')
elif num%2 == 0:
    if num > 0:
        print(f"{num} is even and positive")
    else:
        print(f'{num} is even and negative')
else:
    if num > 0:
        print(f"{num} is odd and positive")
    else:
        print(f'{num} is odd and negative')
        
print('done')

ans = ""
num = int(input("Enter a number: "))
if (num >= 0):
    ans = "positive"
    if( num % 2 == 0):
        ans += " even."
    else:
        ans += " odd."
else:
    ans = "negative"
    if( num % 2 == 0):
        ans += " even."
    else:
        ans += " odd."

print(f"{num} is {ans}")    
print('done')