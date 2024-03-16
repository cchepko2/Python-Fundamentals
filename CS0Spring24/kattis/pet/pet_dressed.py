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

def getData() ->list:
    judge_scores = input().split()
    judge_scores = list(map(int, judge_scores))
    return judge_scores

def listSum(integers: list) -> int: 
    return sum(integers) # add up the total score for the chef

def answer(scores: list) ->str:
    max_score = max(scores)
    index = scores.index(max_score)
    return f"{index+1} {max_score}"

def main():
    scores = []  # empty list for all the chefs total scores

    for _ in range(5): #for each line
        judge_scores = getData()

        sum_scores = listSum(judge_scores)

        scores.append(sum_scores)  # add to list of total scores

    ans = answer(scores)
    print(ans)

if __name__ == "__main__":
    main()
