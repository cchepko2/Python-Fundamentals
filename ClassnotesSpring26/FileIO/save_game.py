'''
Save Game
'''

import os

# Strip the filename and return the path
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

# For windows based system
filename = script_dir + "\\save.txt"


def open_game(filename):
    stats = (1, 4)
    return (stats)



def main():
    
