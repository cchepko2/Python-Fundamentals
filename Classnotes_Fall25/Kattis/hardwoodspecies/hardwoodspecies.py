'''
Programmer: CS110
Date: 11/3/25
Program: Kattis problem - https://open.kattis.com/problems/hardwoodspecies
Algorithm:
    input lines "trees" into a list
        use: for line in sys.stdin:
    alphabatize the list
    for each new tree in the list:
        add to a dictionary with a count of 1
    else (not a new tree):
        increment value of dictionary entry by 1
    
    for each tree in list:
        print the tree name followed by # of trees/total_count * 100
'''

import sys

#species = sys.stdin.readlines() # return a list of lines until EOF
#print(species)
#print(species[0].strip())

species = []
for line in sys.stdin:
    if line == '':
         break
    species.append(line.strip())

#species.sort()

dict_trees = {}
for tree in species:
    if tree in dict_trees:
          dict_trees[tree] += 1
    else:
         dict_trees[tree] = 1

for tree in sorted(dict_trees.keys()):
#for tree in dict_trees:
     print("{} {:.6f}".format(tree, dict_trees[tree]/len(species)*100))
     
# input collection

#while(True):
#        try:
#            line = input()
#            if(line == ''):
#                 break
            
            # I got a tree!
#            species.append(line)
#        except EOFError:
#            break

# solution

# might want to sort the list first

#trees_dict = {}
#for tree in species:
#        if tree in trees_dict:
#            trees_dict[tree] += 1 # tree already in dict, increment by 1
#        else:
#            trees_dict[tree] = 1 # create new key with value of 1

#for tree in trees_dict:
     # print the tree name and %'age