import string
import matplotlib.pyplot as plt

empty_dict = {'stuff':42}

print(empty_dict)
empty_dict.clear()
print(f"now it's empty: {empty_dict}")

empty_dict['CO'] = "Denver"
empty_dict['WY'] = "Cheyenne"
empty_dict['UT'] = "SLC"
print(f'{empty_dict=}')

if "CO" in empty_dict.keys():
    print("'CO' is in the dictionary.")

print(f'{empty_dict.keys()=}')
print(f'{empty_dict.values()=}')
print(f'{empty_dict.items()=}')

empty_dict['VT'] = "Montpelier"

if 'VT' in empty_dict:
    print(f"Value at 'VT': {empty_dict['VT']}")
if 'VT' in empty_dict.keys():
    print(f"Value at 'VT': {empty_dict['VT']}")
print(f"Value at 'VT': {empty_dict.get('VT', 'no se')}")

print(empty_dict.pop('UT')) # remove specific key
print(f"{empty_dict=}")

print(empty_dict.popitem()) # remove last item in dictionary
print(f"{empty_dict=}")

def getHist(word):# = "Mississippi"
    h = {}
    for c in word:
        c = c.lower()
        if( c in string.ascii_lowercase):
            if c in h:
                h[c] += 1
            else:
                h[c] = 1
    return h

sentence = "ThiS is String with Upper and lower case Letters"
sentence = sentence.lower()
print(f"{sentence=}")
sentence = list(sentence)
sentence.sort()
print(f"{sentence=}")
str(sentence)



letter_frequency = getHist(sentence)

print(f"{letter_frequency=}")

# Create the bar graph
plt.bar(letter_frequency.keys(), letter_frequency.values(), color='skyblue')

# Add labels and title
plt.xlabel("Letters")
plt.ylabel("Number")
plt.title("Simple Bar Graph")

# Display the plot
plt.show()
