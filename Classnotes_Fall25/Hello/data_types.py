price = '500.99'
#print("price=", price)
print(f"{price=}")
type(price)
price = float(price)
print(f"{price=}")

print("Hello\n\nWorld")

print("This solution is \r bonkered!")

total_price = price*(price+1)
print(f"{total_price=}")

not_rounded = 9.9999999999
print(f"{not_rounded=}")

# Convert not_rounded to an integer
#not_rounded = int(not_rounded)

# Round not_rounded first, then convert to int
not_rounded = round(not_rounded)
not_rounded = int(not_rounded)

# A clever rounding method...
not_rounded = int(not_rounded+0.5)
print(f"{not_rounded=}")

tot_seconds = 63
minutes = tot_seconds//60   # Does floor division, 
#                       only returns whole divider, not remainder
seconds = tot_seconds%60      # Returns the remainder of hours/60

print(tot_seconds, "seconds =", minutes, "minutes and", seconds, "seconds.")