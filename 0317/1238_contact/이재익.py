import sys
sys.stdin = open('input.txt')
from collections import deque

# 생각해보니 가장 마지막에 연락을 '받은' 사람이다
# 즉 중간에 받았던 사람은 제외다
# 그러므로 노드의 거리 + 맨 처음에 연락을 못 받은 사람이 있다면 그것을 위한 예외 구성만 해주면 될 듯
T = 10
for tc in range(1, 11):
    V, S = map(int, input().split())
    tree = [[] for _ in range(101)]
    M = list(map(int, input().split()))
    for i in range(V//2):
        if M[2*i+1] not in tree[M[2*i]]:
            tree[M[2*i]].append(M[2*i+1])
    queue = deque(tree[S])
    visited = [0]*101
    visited[S] = 1
    while(queue):
        n = queue.popleft()
        if len(tree[n]) == 0 and max(visited) == 1:
            visited[n] = visited[S]+1
        else:
            for i in tree[n]:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = visited[n]+1
    cnt = 0
    for i in range(101):
        if visited[i] == max(visited):
            cnt = i
    print(f'#{tc} {cnt}')