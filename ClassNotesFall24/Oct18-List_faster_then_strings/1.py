import random
# Import the time library
import time

# Calculate the start time
start = time.time()

# Code here
# add 1000 random numbers to a string
ans = "1"
iterations = 10000000

for i in range(1000):
    num = random.randint(1, iterations)
    ans += f", {num}"

print("Done first!")
# Calculate the end time and time taken
end = time.time()
length = end - start

# Show the results : this can be altered however you like
print("It took", length, "seconds!")


# Calculate the start time
start = time.time()
# much faster way using list
ans_l = ["1"]
for i in range(1000):
    num = random.randint(1, iterations)
    ans_l.append(str(num))

ans = ", ".join(ans_l)
print("Done second!")
# Calculate the end time and time taken
end = time.time()
length = end - start

# Show the results : this can be altered however you like
print("It took", length, "seconds!")

