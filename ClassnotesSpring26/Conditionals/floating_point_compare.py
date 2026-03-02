import math

n1 = 0.1
n2 = 0.2
print(n1+n2 == 0.3)

error = 1e-6
print(abs(n1+n2 - 0.3) <= error)
print( math.isclose(n1+n2, 0.3))