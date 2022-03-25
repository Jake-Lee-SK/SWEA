import sys
sys.stdin = open('input.txt')

# 맨 끝에 0이 있으면 바꾸면 안되고
# 맨 끝에 같은 숫자가 있어야 바꿀 수 있음

def othello(y, x, P):
    if P == 1:
        K = 2
    else:
        K = 1
    # 상
    change = []
    q = y
    while 1:
        if 0<=q-1<N:
            if matrix[q-1][x] == K:
                change.append([q-1, x])
                q -= 1
            elif matrix[q-1][x] == 0:
                break
            elif matrix[q-1][x] == P:
                for i in range(len(change)):
                    matrix[change[i][0]][change[i][1]] = P
                break
        else:
            break

    # 하
    change = []
    q = y
    while 1:
        if 0<=q+1<N:
            if matrix[q+1][x] == K:
                change.append([q+1, x])
                q += 1
            elif matrix[q+1][x] == 0:
                break
            elif matrix[q+1][x] == P:
                for i in range(len(change)):
                    matrix[change[i][0]][change[i][1]] = P
                break
        else:
            break

    # 좌
    change = []
    p = x
    while 1:
        if 0<=p-1<N:
            if matrix[y][p-1] == K:
                change.append([y, p-1])
                p -= 1
            elif matrix[y][p-1] == 0:
                break
            elif matrix[y][p-1] == P:
                for i in range(len(change)):
                    matrix[change[i][0]][change[i][1]] = P
                break
        else:
            break
    # 우
    change = []
    p = x
    while 1:
        if 0<=p+1<N:
            if matrix[y][p+1] == K:
                change.append([y, p+1])
                p += 1
            elif matrix[y][p+1] == 0:
                break
            elif matrix[y][p+1] == P:
                for i in range(len(change)):
                    matrix[change[i][0]][change[i][1]] = P
                break
        else:
            break

    # 대각선 우상
    change = []
    q = y
    p = x
    while 1:
        if 0<=q-1<N and 0<=p+1<N:
            if matrix[q-1][p+1] == K:
                change.append([q-1, p+1])
                q -= 1
                p += 1
            elif matrix[q-1][p+1] == 0:
                break
            elif matrix[q-1][p+1] == P:
                for i in range(len(change)):
                    matrix[change[i][0]][change[i][1]] = P
                break
        else:
            break

    # 대각선 우하
    change = []
    q = y
    p = x
    while 1:
        if 0<=q+1<N and 0<=p+1<N:
            if matrix[q+1][p+1] == K:
                change.append([q+1, p+1])
                q += 1
                p += 1
            elif matrix[q+1][p+1] == 0:
                break
            elif matrix[q+1][p+1] == P:
                for i in range(len(change)):
                    matrix[change[i][0]][change[i][1]] = P
                break
        else:
            break

    # 대각선 좌상
    change = []
    q = y
    p = x
    while 1:
        if 0<=q-1<N and 0<=p-1<N:
            if matrix[q-1][p-1] == K:
                change.append([q-1, p-1])
                q -= 1
                p -= 1
            elif matrix[q-1][p-1] == 0:
                break
            elif matrix[q-1][p-1] == P:
                for i in range(len(change)):
                    matrix[change[i][0]][change[i][1]] = P
                break
        else:
            break

    # 대각선 좌하
    change = []
    q = y
    p = x
    while 1:
        if 0<=q+1<N and 0<=p-1<N:
            if matrix[q+1][p-1] == K:
                change.append([q+1, p-1])
                q += 1
                p -= 1
            elif matrix[q+1][p-1] == 0:
                break
            elif matrix[q+1][p-1] == P:
                for i in range(len(change)):
                    matrix[change[i][0]][change[i][1]] = P
                break
        else:
            break

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    matrix = [[0]*(N) for _ in range(N)]
    if N == 4:
        matrix[1][1] = 2
        matrix[1][2] = 1
        matrix[2][2] = 2
        matrix[2][1] = 1
    if N == 6:
        matrix[2][2] = 2
        matrix[2][3] = 1
        matrix[3][3] = 2
        matrix[3][2] = 1
    if N == 8:
        matrix[3][3] = 2
        matrix[3][4] = 1
        matrix[4][4] = 2
        matrix[4][3] = 1
    for i in range(M):
        Y, X, P = map(int,input().split())
        matrix[Y-1][X-1] = P
        othello(Y-1, X-1, P)
    black = 0
    white = 0
    # 만약 else문으로 처리하면 '0'이 있는 공간도 white 갯수로 들어가게 된다.
    # 예외문 생각 안하면 틀리는 오류... 조심하자.
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                black += 1
            elif matrix[i][j] == 2:
                white += 1
    print(f'#{tc} {black} {white}')
