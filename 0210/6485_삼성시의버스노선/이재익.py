import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    routes = []
    for route in range(1, N+ 1):
        route = list(map(int, input().split()))
        whole_route = list(range(route[0], route[1]+1))
        routes.append(whole_route)
    P = int(input())

    stops = []
    for i in range(1, P+1):
        stops.append(int(input()))

    set_stops = set(stops)
    stops2 = list(set_stops)
    stop_count = [0]*5000

    for j in stops2:
        for i in routes:
            if j in i:
                stop_count[j-1] += 1
    stop_list = []
    for j in stops:
        stop_list.append(stop_count[j-1])

    print(f'#{tc}', end=' ')
    for stops in stop_list:
        print(stops, end=' ')
    print()