import sys

print("This goes to error output when file=sys.stderr", file=sys.stderr)

print("Enter two numbers separated by a space.", file=sys.stderr)
a, b = input().split()