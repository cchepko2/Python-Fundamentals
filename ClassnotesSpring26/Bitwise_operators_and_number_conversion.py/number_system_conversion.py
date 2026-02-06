'''
Conversion from binary to decimal:
    0b1001 = 1*2**3 + 0*2**2 + 0*2**1 + 1*2**0
    = 8 + 1 = 9
    0b1101 = 1*2**3 + 1*2**2 + 0*2**1 + 1*2**0
    = 8 + 4 + 1 = 13

    0b1011 = 1*2**3 + 0*2**2 + 1*2**1 + 1*2**0
    = 8 + 2 + 1 = 11


Conversion from decimal to binary (base 2):
    18 / base => 9 R0
    9/base => 4 R1
    4/2 => 2 R0
    2/2 => 1 R0
    1/2 => 0 R1
    Put together the remainders backwards:
    18 = 0b10010

    11 / base => 5 R1
    5/2 => 2 R1
    2/2 = 1 R0
    1/2 = 0 R1
    Put remainders together backwards: 0b1011

Count to 15 in Hex: 0123456789ABCDEF
0x18 = 1*16**1 + 8*16**0 = 16 + 8 = 24
0xFF = 15*16**1 + 15*16**0 = 15*16 + 15 = 255

Decimal to Hex: Same as base 2, but the base is 16:
    24 / 16 => 1 R8
    1/16 => 0 R1

    Remainders backward: 0x18

    255 to Hex (base 16):
    255 / base => 15 R15 = F RF
    15/16 => 0 R15 = 0 RF

    Remainders backward: 0xFF

    134 to Hex:
    134 / 16 => 8 R6
    8/16 => 0 R8
    Remainders backward: 0x86
'''



number = 18
print(bin(number))
print(hex(number))

number = 11
print(bin(number))
print(hex(number))

number = 0x86
print(number)

