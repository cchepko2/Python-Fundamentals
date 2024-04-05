years = []
for i in range(1024):
    years.append(str(999+i))

years2 = years.copy()

print(years)

print()
years2.sort()
print(years2)

print(years2 is years)
print(years2 == years)