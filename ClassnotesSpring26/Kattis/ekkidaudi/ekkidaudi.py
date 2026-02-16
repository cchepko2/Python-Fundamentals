'''
Corin Chepko
2/16/25
Kattis Problem: Ekki Daudi: https://open.kattis.com/problems/ekkidaudi
Algorithm Steps:
    Collect first line of input
    Split line into 1ine1a and line2a
    Cllect 2nd line of input
    Split line into line 1b and 2b
    Combine lines 1a+2a and 1b+2b
    Print the answer
'''

def solution(line1, line2):
    line1a, line2a = line1.split('|')
    line1b, line2b = line2.split('|')
    answer = line1a + line1b + ' ' + line2a + line2b
    return answer

line1 = input()
line2 = input()

answer = solution(line1, line2)
print(answer)