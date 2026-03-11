# Cannot change a piece of a string without 
# re-defining the whole string

message = "A piece"
message2 = " of a string."

#message[0] = 'a'
message = 'a' + message[1::]
print(message)

print(message+message2)

message = message + message2

list_in_brackets = [1, 2, 3, 4, 5]
tuple_in_parenthesis = (1, 2, 3, 4 ,5)