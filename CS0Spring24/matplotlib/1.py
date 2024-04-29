# Python program to show plot function

import matplotlib.pyplot as plt
import numpy as np
import math

y = [1, 4, 9, 16]
y_array = np.array(y)

x_vals = np.linspace(0, 2*math.pi, 100)
y_vals = np.sin(x_vals)
print(x_vals)

plt.plot(x_vals, y_vals)
#plt.plot([1, 2, 3, 4], 2*y_array)

plt.axis([0, 6, -1, 1])
plt.show()
