message = "a longer message than before"

empty = ""

print(f"Number of 'a's: {message.lower().count('a')}")

first_a_index = message.lower().find('a')
print(f"First 'a' at {first_a_index}")
second_a_index = message.lower().find('a', first_a_index+1)
print(f"Second 'a' at {second_a_index}")

# Get the num characters in string
print(f"Message length = {len(message)}")

print(message.capitalize())
print(message.title())

tuple_of_messages = ("a", "oo", ".")
print(message.endswith('a'))
print(message.endswith(tuple_of_messages))

words = message.split()
print(words)
for each_word in words:
    print(each_word, end=' ')

print()
print(",".join(words))