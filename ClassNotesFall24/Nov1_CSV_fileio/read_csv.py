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
    
    time = time[::-1] # reverse the list because it's backwards in time
    temperature = temperature[::-1]

    avg = 0
    
    noontemps = []  # my list for temperatures at noon
    noontimes = []  # list of times (dates) at noon
    for i in range(144, len(temperature), 288): 
    # starting at index 144, incrementing by 24 hours of indexes
        noontemps.append(temperature[i])
        noontimes.append(time[i])
    
    for i in range(len(noontimes)):
        print(noontimes[i], noontemps[i])
        avg += temperature[i]
    
    plt.plot(noontemps)

    plt.show()

    avg = avg/len(temperature)

    with open(f'{my_path}/out.txt', 'w') as file:
        #file.write(f'Average temp = {avg}')
        file.write('Noon Date,Noon Temperature\n')
        for i in range(len(noontemps)):
            file.write(f'{noontimes[i]},{noontemps[i]}\n')
        

if __name__ == "__main__":
    main()