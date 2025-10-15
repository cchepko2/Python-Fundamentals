price = 8.99
tax = 0.08375

# formatted string, begins with an f"<string>"
# anything in {} will be replaced with the value of the 
# varible or expression in {}
print(f"Price = {price}")
print(f"Tax = {tax}")

# Use format specifier :.<num_digits> for significant figures
txt = f"The price is {price + (price * tax):.2} dollars"
print(txt)

# Use format specifier :.<num_digits>f for significant decimals
txt = f"The price is {price + (price * tax):.2f} dollars"
print(txt)

name = "Sally"
height = 159.0
txt = f"{name} is {height} tall and {name} has blonde hair"
print(txt)

txt = "{0} is {1:.2f} tall and {0} has blonde hair".format(name, height)
print(txt)

txt = f"{'Apple':>>}\t{'Price':^}\t{'Weight':<<}"
print(txt)
