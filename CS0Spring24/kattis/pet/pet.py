'''
Corin Chepko
3/15/24
Kattis Problem: Pet https://open.kattis.com/problems/pet
Alogorithm Steps:
    for 5 chef scores:
        input line of numbers, convert them to ints
        Sum those ints for the chef score
        Add that score to a list of chef scores
    Pick the top score and line number from the list of scores
    print line number (starting from 1) and winning score
'''

scores = []  # empty list for all the chefs total scores

for _ in range(5): #for each line
    judge_scores = input().split()
    judge_scores = list(map(int, judge_scores))

    sum_scores = sum(judge_scores) # add up the total score for the chef
    scores.append(sum_scores)  # add to list of total scores

max_score = max(scores)
index = scores.index(max_score)
print(index+1, max_score)
