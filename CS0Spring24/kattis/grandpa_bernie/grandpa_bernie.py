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

def main():
    num_trips = int(input())
    trips = {} #empty dictionary of trips
    for i in range(num_trips):
        country, year = input().split()
        if country in trips:
            trips[country].append(int(year))
        else:
            trips[country] = [int(year)]

    for trip in trips:
        trips[trip].sort()

    queries = int(input())
    queries_l = []
    for i in range(queries):
        country, trip_num = input().split()
        queries_l.append((country, trip_num))
    
    for q in queries_l:
        country, trip_num = q
        print(trips[country][int(trip_num)-1])


if __name__ == '__main__':
    main()