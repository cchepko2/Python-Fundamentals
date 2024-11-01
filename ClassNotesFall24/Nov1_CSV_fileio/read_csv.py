import os
import pathlib
import matplotlib.pyplot as plt

# find local path of program
my_path = pathlib.Path(__file__).parent.resolve()

def main():
    time = []
    temperature = []
    header = []
    filename = f'{my_path}/weather.csv'

    if os.path.exists(filename):
        with open(filename, 'r') as my_file:
            header = my_file.readline().split(',')
            '''while(True):
                data = my_file.readline()
                if data == "":
                    break'''
            data = my_file.read().split('\n')
            data.pop(-1) # remove the last value which is an empty line

    for line in data:       
        line = line.split(',')
        time.append(line[0])
        temperature.append(float(line[1]))
    
    time = time[::-1]
    temperature = temperature[::-1]

    avg = 0

    for i in range(len(time)):
        print(time[i], temperature[i])
        avg += temperature[i]
    
    plt.plot(temperature)

    plt.show()

    avg = avg/len(temperature)

    with open(f'{my_path}/out.txt', 'w') as file:
        file.write(f'Average temp = {avg}')


if __name__ == "__main__":
    main()