import sys
sys.stdin = open('input.txt')

def DFS_AR(S):
    global where_go
    visited = []
    where_go.append(S)
    visited.append(S)
    for i in range(V+1):
        if L[S][i] == 1 and i not in visited:
            DFS_AR(i)

# 교수님이 알려준 방식

"""
def DFS(V, E, graph, S, G): # V는 node 수, E는 edge 수, graph는 node와 edge가 담겨있는 정보, S는 시작, G는 도착
    # 특정 node에 방문했는지 체크용
    visited = [False for _ in range(V+1)]
    # 앞으로 방문할 곳을 모아 놓은 stack
    to_visits = [S]
    while to_visits:
        current = to_visits.pop()
        if not visited[current]:
            visited[current] = True
            to_visits += graph(current)
"""
# 2. 2D Array 방식

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # V = 점 갯수, E = 간선 갯수
    # 이 경우에는 간선 갯수만큼 start,end가 존재.
    L = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        L[start][end] = 1
    S, G = map(int, input().split())
    # 스택을 쌓아서 DFS를 실행.
    where_go = []
    DFS_AR(S)
    if G not in where_go:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')