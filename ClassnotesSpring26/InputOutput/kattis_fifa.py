'''
Corin Chepko
1/30/26
Kattis Problem - Fifa - https://open.kattis.com/problems/fifa
Algorithm Steps:
    input n, the number of improvements
    input k, the improvements per year
    n/k = years since 2022
    print(2022 + n/k)
'''

n = input()
k = input()

n = int(n)
k = int(k)

years = n/k
years_plus_2022 = years + 2022
years_plus_2022 = int(years_plus_2022)
print(years_plus_2022)
