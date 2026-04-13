'''
Corin Chepko
Kattis problem - https://open.kattis.com/problems/grandpabernie
Algorithm:
    input number of trips
    for each trip:
        add year to country key
    input queries
    for queries:
        check year corrosponding to trip number
'''

import time

def solution(queries_list, trip_dict):
    for trip in trip_dict:
        trip_dict[trip].sort()

    ans = []
    for q in queries_list:
        country, trip_num = q
        ans.append(f"{trip_dict[country][trip_num-1]}")
    
    #print(ans)
    return '\n'.join(ans)

def main():
    num_trips = int(input())

    trip_dict = {}
    for i in range(num_trips):
        country, year = input().split()
        year = int(year)
        if country in trip_dict:
            trip_dict[country].append(year)
        else:
            trip_dict[country] = [year]

    #print(trip_dict)
    for trip in trip_dict:
        trip_dict[trip].sort()

    queries_list = []
    num_queries = int(input())
    for i in range(num_queries):
        country, trip_num = input().split()
        trip_num = int(trip_num)
        queries_list.append((country, trip_num))
        
        trip_num = int(trip_num)

    ans = solution(queries_list, trip_dict)
    print(ans)
    
    stop_time = time.time()
    print(stop_time-start_time)


if __name__ == '__main__':
    main()