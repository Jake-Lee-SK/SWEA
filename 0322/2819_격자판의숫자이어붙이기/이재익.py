import sys
sys.stdin = open('input.txt')
def DFS(cnt, y, x, number):
    global lists
    global seven_list
    global graph
    number = number*10 + M[y][x]

    if cnt == 6:
        lists.append(number)
        return
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0<=new_y<4 and 0<=new_x<4:
            DFS(cnt+1, new_y, new_x, number)

T = int(input())
for tc in range(1, T+1):
    M = [list(map(int, input().split())) for _ in range(4)]
    dx = [1, -1, 0, 0]
    dy = [0,0,1,-1]
    seven_list = []
    lists = []
    for i in range(4):
        for j in range(4):
            DFS(0, i, j, 0)
    results = set(lists)
    print(f'#{tc} {len(results)}')