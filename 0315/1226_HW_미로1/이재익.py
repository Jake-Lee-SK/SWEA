import sys
sys.stdin = open('input.txt')

# DFS 구현 문제

def find(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    global find2
    global CM

    # 찾으면 종료
    if M[x][y] == 3:
        find2 += 1
        return

    # 벽에 다다르면 종료.
    if M[x][y] == 1:
        return

    # 이미 갔던 곳이라면 종료.
    if CM[x][y] == False:
        CM[x][y] = True
    else:
        return

    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]
        find(new_x, new_y)

T = 10
for tc in range(1, 11):
    x = 0
    y = 0
    find2 = 0
    CM = [[False]*16 for _ in range(16)]
    N = int(input())
    M = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if M[i][j] == 2:
                x = i
                y = j
    find(x, y)
    print(f'#{tc} {find2}')