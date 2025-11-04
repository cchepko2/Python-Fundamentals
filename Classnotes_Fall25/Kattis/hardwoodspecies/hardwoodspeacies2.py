"""
Programmer: Willon Rice
Instructor: Corin Chepko
Date: 11/3/2025
Description: A Kattis problem involving dictionaries to sort a list of hardwood trees and determine what percent of the list is taken up by each species
"""

import sys
import time

def gather_data():
    treesUnsorted = sys.stdin.readlines()
    return treesUnsorted

def tree_percents(species, length:int):
    for tree in species:
        percent = (species[tree]/length)*100
        percent = round(percent, 6)
        species[tree] = percent

def process_data(species, trees):
    #trees.sort()
    for tree in trees:
        tree = tree.strip()
        if tree in species:
            species[tree] += 1
        else:
            species[tree] = 1

def main():
    species = {}
    trees = gather_data()
    
    process_data(species, trees)
    
    length = len(trees)

    tree_percents(species, length)
    for tree in sorted(species):
        print(tree, species[tree])

if __name__ == "__main__":
    main()
