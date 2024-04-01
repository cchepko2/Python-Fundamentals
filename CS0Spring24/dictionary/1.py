def something(alist):
    alist.append('Another Item')

eng2sp = {}

unos = ['uno']

eng2sp['One'] = unos
eng2sp['Two'] = 'dos'

print(eng2sp)

print(eng2sp.keys())

key = input("Enter a key: ")
#value = input("Enter a value")

if key in eng2sp.keys():
    print(eng2sp[key])
else:
    print("Key does not exist!")

if key in eng2sp:
    print(eng2sp[key])
else:
    print("Key really does not exist!")

if eng2sp.get(key) != None:
    print(eng2sp[key])

print(eng2sp.items())

for key,value in eng2sp.items():
    print(f"Value at key {key} = {value}")


stuff = ['a', 2, 5]
something(stuff)

print(stuff)


