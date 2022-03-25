import sys
sys.stdin = open('input.txt')

# BFS 문제의 전형이라고 생각함
# 최단거리 재는 문제는 무조건 BFS!
# 다만 조건을 조심할 것(이번 경우 길이가 같다면 방 크기가 '최소'였어야 함.)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(y, x):
    global max_cnt
    global room
    cnt = 0
    now_room = M[y][x]
    a = y
    b = x
    next = []
    next.append([y, x])
    while next:
        cnt += 1
        c = next.pop()

        for k in range(4):
            new_y = c[0] + dy[k]
            new_x = c[1] + dx[k]
            if 0<=new_y<N and 0<=new_x<N and M[new_y][new_x] == M[c[0]][c[1]] + 1:
                next.append([new_y, new_x])
                break
    if max_cnt < cnt:
        max_cnt = cnt
        room = now_room
    elif max_cnt == cnt:
        if room > now_room:
            room = now_room


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    room = N*N+1
    for i in range(N):
        for j in range(N):
            BFS(i, j)
    print(f'#{tc} {room} {max_cnt}')