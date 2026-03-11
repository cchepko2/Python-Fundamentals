message = "a longer message than before"

for i in range(len(message)):
    print(message[i], end= ' ')

print()

# First character
print( message[0] )
# Last character
print( message[len(message)-1])

# Print last character
print( message[-1] )
for i in range(0, -1*len(message), -1):
    print( message[i], i)

print()


for i in range(0, len(message)-1, 1):
    print( message[i], i)