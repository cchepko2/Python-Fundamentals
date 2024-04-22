'''
Corin Chepko
4/22/24
Kattis problem: https://open.kattis.com/problems/hardwoodspecies
Algorithm Steps:
    Input lines of tree names:
        far each name, tree:
            if not in dictionary trees:
                create dictionary item with value 1
                trees[tree] = 1
            if in trees:
                trees[tree] = trees[tree] + 1
    
'''

import sys

def getTrees():
    trees = {}
    total = 0
    for tree in sys.stdin:
        if tree == "\n":
            break
        tree = tree.strip()
        if tree in trees:
            trees[tree] += 1
        else:
            trees[tree] = 1
        total += 1
    return trees, total

def solution(trees, total):
    answers = []
    for key in sorted(trees.keys()):
        percentage = trees[key]/total*100
        answers.append("{} {:2.8}".format(key, percentage))
    return answers

def test():
    total = 4
    trees = {"Ash":2, "Willow":1, "Elder":1}
    print(solution(trees, total))
    assert solution(trees, total) == ["Ash 50.0", "Elder 25.0", "Willow 25.0"]
    print("All tests passed!", file=sys.stderr)

def main():
    trees, total = getTrees()    
    answers = solution(trees, total)
    print('\n'.join(answers))
    

if __name__ == "__main__":
    test()
    main()