squares = [x**2 for x in range(1, 6)]
print(squares)

squares.reverse()
print(squares)

squares = squares[::-1]
print(squares)

last = squares.pop()
print(squares)
print(last)

squares.extend(range(1,5))
print(squares)

squares.sort(reverse=True)
print(squares)

mixed_list = ["Cprin", "Xander", "Sally"]
mixed_list.sort()