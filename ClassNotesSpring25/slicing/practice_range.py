# Investigate the slicing further

giftList = ["partridge in a pear tree","turtle doves","french hens","calling birds","gold rings","geese a laying","swans a swimming","maids a milking","ladies dancing","lords of leaping","pipers piping","drummers drumming"]
phrase = "partridge in a pear tree"
word = "word"

# Cannot go out of bounds of the length of the string, len(word) = 4,
# so, positive index cannot exceed 3 and negative cannot exceed -4
#print(word[-5])
#print(word[4])


# Refer to elements by index
print(phrase)
print(f"First char = {phrase[0]}")
print(f"Second char = {phrase[1]}")
print(f"Last char = {phrase[-1]}, or {phrase[len(phrase)-1]}")
print(f"Second to last char = {phrase[-2]}, or {phrase[len(phrase)-2]}")

# slicing, use [start : stop(not included) : step], if one is not provided, defaults
# are applied, start=0 : stop=end : step=1
print(phrase[::]) # assume start is 0, end is len-1, step is 1
print(phrase[0:len(phrase):1]) # assume start is 0, end is len-1, step is 1

# get the "partiridge" for the phrase
print(phrase[0:10:1])
print(phrase[0:10:2])

# print the whole phrase backward, start=0:end=end:step=-1
print(phrase[::-1])

# take partridge and print backward
partridge = phrase[0:9]
partridge_backward = partridge[::-1]
print(partridge, partridge_backward)

day = 5
print(list(range(day-1,-1,-1)))

print(phrase[:-1])
