import random
import time

trees_list = ["ash", "cottonnwood", "aspen"]*300_000
random.shuffle(trees_list)

t0 = time.time()
trees_list.sort()
t1 = time.time()

print(f"{t1-t0} seconds")

species = {}
for tree in trees_list:
    if tree in species:
        species[tree] += 1
    else:
        species[tree] = 1

t0 = time.time()
keys_list = sorted(trees_list)
t1 = time.time()
print(f"{t1-t0} seconds")