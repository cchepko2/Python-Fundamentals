number = 1000000
f_number = f"{number:,}"
print(f_number)

name = "Corin"

# left alignment in 10 spaces
print(f"{name:<10}")
# right alignment in 10 spaces
print(f"{name:>10}")
# center alignment in 10 spaces
print(f"{name:^10}")

price = 9.9999
print(f"{price:.2f}")

fruit = 'Peach'
price = 0.99

list_price = f"{fruit:<20}{price:>.2f}"
print(list_price)