import sys
import heapq

sys.stdin = open('dijkstra_input.txt')

INF = float('INF')

V, E, end = map(int, input().split())

graph = [[] for _ in range(V+1)]

visited = [False for _ in range(V+1)]

distances = [INF for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))


def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distances[start] = 0

    while hq:
        distance, current = heapq.heappop(hq)
        if distances[current] < distance:
            continue
        for new_node, weight in graph[current]:
            cost = distance + weight
            if cost < distances[new_node]:
                distances[new_node] = cost
                heapq.heappush(hq, (cost, new_node))


dijkstra(0)

print(distances)

