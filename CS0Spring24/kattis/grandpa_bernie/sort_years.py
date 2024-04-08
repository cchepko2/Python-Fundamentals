years = []

for i in range(1024):
    years.append(str(999+i))

print(years)

years2 = years.copy()

years2.sort()
print(years2)

print(years == years2)