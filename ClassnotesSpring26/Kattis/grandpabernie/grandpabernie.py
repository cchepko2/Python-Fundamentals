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

    num_queries = int(input())
    

    
    print(trip_dict)


if __name__ == '__main__':
    main()