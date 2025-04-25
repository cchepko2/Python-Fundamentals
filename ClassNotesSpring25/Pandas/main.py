import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

current_file_path = Path(__file__)
current_file_path = str(current_file_path.parent) + '\\'

'''df = pd.read_csv(current_file_path + 'weather.csv')
df.head()

print(df.count())
print(df.head())

plt.title('Line Plot')
plt.xlabel('Index')
plt.ylabel('Values')
plt.show()
'''

d = {'Column One': [1, 2, 3, 4, 5], 'Column Two': [10, 20, 30, 40, 50]}

df = pd.DataFrame(data=d)

plot = df.plot(kind='line')

plt.show()
