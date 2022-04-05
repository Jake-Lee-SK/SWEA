import sys
sys.stdin = open('dijkstra_input.txt')


INF = float('INF')


def get_shortest_node():
    minimum = INF
    idx = 0
    for i in range(1, V+1):
        if distances[i] < minimum and not visited[i]:
            minimum = distances[i]
            idx = i
    return idx


def dijkstra(start):
    global distances, visited
    # 초기화
    distances[start] = 0
    visited[start] = True

    for e, w in graph[start]:
        distances[e] = w

    for _ in range(V-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 visited 처리
        current = get_shortest_node()
        visited[current] = True

        for new_node, weight in graph[current]:
            cost = distances[current] + weight
            if cost < distances[new_node]:
                distances[new_node] = cost


V, E, end = map(int, input().split())

graph = [[] for _ in range(V+1)]

visited = [False for _ in range(V+1)]

distances = [INF for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))


dijkstra(0)

print(distances)