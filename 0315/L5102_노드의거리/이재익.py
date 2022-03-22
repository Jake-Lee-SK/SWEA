# BFS를 이용

import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    M = [[] for _ in range(V+1)]
    for i in range(E):
        A, B = map(int, input().split())
        M[A].append(B)
        M[B].append(A)
    S, G = map(int, input().split())

    queue = deque([S]) # 시작점을 넣은 deque를 생성
    visited = [0]*(V+1) # 방문여부 점검할 list
    visited[S] = 1 # 시작점을 방문했다고 함(첫번째이므로 거리는 1)
    while(queue):
        print(queue, visited)
        n = queue.popleft() # 맨 왼쪽을 빼냄, 만약 빼낸 숫자에서 더 이상 방문할 곳이 없다면 그대로 while문 종료.
        for i in M[n]: # 시작점에서 방문할 곳(연결된 노드)을 점검
            if visited[i] == 0: # 만약 방문한 곳이 아니라면
                queue.append(i) # deque의 맨 오른쪽에 i를 추가함
                visited[i] = visited[n]+1 # visited의 i번째에는 방문한 곳과 1만큼 떨어져있는 것임
    if visited[G] != 0:
        print(f'#{tc} {visited[G]-1}')
    else:
        print(f'#{tc} 0')