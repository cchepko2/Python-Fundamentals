character = 'A'

new_char = chr(ord(character)+1)
# ord function return the unicode number for a character
print(f"{character=}")
print(f"{ord(character)=}")
print(f"{new_char=}")

# unicode character can be written as below. This example is the degrees symbol
degrees = '\u00b0'

print(f"{degrees=}")

# Checkmark symbol
print("Checkmark symbol:", u'\u2713')

# can write binary numbers using 0b to prefix the number
print(f"{0b1011=}")

# can write hexadecimal numbers using 0x to prefix the number
print(f"{0xa=}")

# can write hexadecimal numbers using 0x to prefix the number
print(f"{0o11=}")

number = 255
print(f"Binary of {number} = {bin(number)}")
print(f"Octal of {number} = {oct(number)}")
print(f"Hexadecimal of {number} = {hex(number)}")

# bitshifting is basically fast way to multiply and divide integers by 2
number = 3
# left shift multiplies by 2
print(f"{number=} shifted left twice {number<<2=}")

# right shift divides by 2
print(f"{number=} shifted right once {number>>1=}")