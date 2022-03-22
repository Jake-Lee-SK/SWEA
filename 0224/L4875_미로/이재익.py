import sys
sys.stdin = open('input.txt')

def find_road(a, b):

    # 3(출구)을 찾았다면 find에 찾았다는 정보 저장
    global find

    if M[a][b] == 3:
        find.append(1)
        return

    # 델타함수
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 방문기록 글로벌선언
    global visited

    # 해당 부분이 1이면 루프 종료
    if M[a][b] == 1:
        return

    # 해당 부분이 False면 미탐색부분이므로 True로 바꿔주고
    # 이미 탐색한 부분이면 루프 종료
    if visited[a][b] == False:
        visited[a][b] = True
    else:
        return

    # 1도 아니고, 미탐색부분이었다면 루프 계속 진행

    for i in range(4):
        if 0 <= a + dx[i] < N and 0 <= b + dy[i] < N:
            find_road(a + dx[i], b + dy[i])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if M[i][j] == 2:
                first_x = i # 처음 값은 2의 x값
                first_y = j # 처음 값은 2의 y값
    visited = [[False] * (N) for _ in range(N)]
    find = []
    find_road(first_x, first_y)
    if find:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

