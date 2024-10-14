import copy

a = [1, [2, 3]]
b = a
c = a.copy()
d = a[:]
f = copy.deepcopy(a)

print(a,b,c,d,f)

a[1][1] = "Corin"

print(a,b,c,d,f)
# f is the only non-modifed one after modifying 'a'

a.pop(1)

print(a)