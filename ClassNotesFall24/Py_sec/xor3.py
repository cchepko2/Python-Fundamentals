xor_str = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
#xor_str = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

key = 'myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymy'

key_bytes = [ord(c) for c in key]

xor_bytes = list(bytes.fromhex(xor_str))
print(len(key_bytes), len(xor_bytes))

print(xor_bytes)
print(key_bytes)

i=0
for byte in xor_bytes:
    if(i < len(key_bytes)):
        print(chr(byte^(key_bytes[i])), end='')
    i+=1
        #flag_byte += 1
print()
        