list1 = [1,2,3,4]
list2 = [5,6,7,8]

alist = list('aaaaaaaaaaaaaaa')
print(alist)

lists = [list1, list2]

print(list1+list2)
print(list1*2)

scores = [1,2,11,12,68, 98, 79, 87, 42]
for score in scores:
    print(score, end=',')
print('\n\n')

print(scores)
scores.sort()
scores = list(map(str, scores))
print(scores)
print(','.join(scores))

del scores[2]
print(scores)

print(scores)

