'''
Floor division and modulus
'''

time = 131

hours = 131/60
print(f"{time= }")
#print(int(hours))

hours = time//60 # use floor division to cut off decimal
print(f"{time//60=}")

minutes = time%60
print(f"{time%60=}")