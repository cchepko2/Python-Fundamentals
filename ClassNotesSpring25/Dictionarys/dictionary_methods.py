english_to_spanish = {}

print(f"{english_to_spanish=}")

english_to_spanish["One"] = "Uno"
print(f"{english_to_spanish=}")

some_keys = ["Two", "Three", "Four"]
new_dict = english_to_spanish.fromkeys(some_keys, "Dos")
print(f"{new_dict=}")

print(f"{english_to_spanish.get("Two")=}")

# The following line causes a crash because the key does not exist
# print(f"{english_to_spanish["Two"]=}")
english_to_spanish["two"] = "dos"
english_to_spanish["three"] = "tres"

print(f"{english_to_spanish.keys()=}")

# .keys() returns a list of keys
print( "one" in english_to_spanish.keys())

# .items() returns a list of tuples (key, value)
print(f"{english_to_spanish.items()=}")

print(f"{english_to_spanish=}")
english_to_spanish.popitem()
print(f"{english_to_spanish=}")

print(f"{english_to_spanish.values()=}")