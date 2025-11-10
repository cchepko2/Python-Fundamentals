import os
from matplotlib import pyplot as plt 

script_dir = os.path.dirname(__file__)
filename = script_dir + '\\weather.csv' # for windows
# filename = script_dir + '/weather.csv' # for codespace, mac, or linux
data = []

with open(filename) as fin:
    header_list = fin.readline().split(',')
    for line in fin:
        data.append(line.split(','))
    print(header_list[1])
    print(data[0][1])

    temps = []
    for item in data:
        temps.append(item[1])

plt.plot(temps)
plt.show()

