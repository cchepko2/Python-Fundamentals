import time

t0 = time.time()

ans = ""
for i in range(100000):
    ans += str(i) + ' '

t1 = time.time()
print(t1-t0)

t0 = time.time()
ans_list = []
for i in range(100000):
    ans_list.append(str(i))

#print(' '.join(ans_list))
t1 = time.time()
print(t1-t0)