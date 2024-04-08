'''
Corin Chepko
4/3/24
Kattis Problem: Grandpa Bernie: https://open.kattis.com/problems/grandpabernie
Algorithm steps:
    input number to trips
    for trips:
        input country and year
    input queries
    for queries:
        input country and trip_num
        output year of trip_num
'''
import sys

def test():
    trips = {'USA':[1999,999], 'Australia':[2005]}
    queries = [('USA','2'),('Australia', '1')]

    assert solution(trips, queries) == '1999\n2005'
    print("All asserts passed!", file=sys.stderr)

def solution(trips, queries_l):

    ans = []

    for trip in trips:
        trips[trip].sort()

    for q in queries_l:
        country, trip_num = q
        #print(trips[country][int(trip_num)-1])
        ans.append(f"{trips[country][int(trip_num)-1]}")
    return '\n'.join(ans)

def main():
    num_trips = int(input())
    trips = {} #empty dictionary of trips
    for i in range(num_trips):
        country, year = input().split()
        if country in trips:
            trips[country].append(int(year))
        else:
            trips[country] = [int(year)]

    queries = int(input())
    queries_l = []
    for i in range(queries):
        country, trip_num = input().split()
        queries_l.append((country, trip_num))
    
    ans = solution(trips, queries_l)

    print(ans)


if __name__ == '__main__':
    test()
    main()