import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # NxN 행렬
    M = [list(map(int, input().split())) for _ in range(N)]
    first_M = [list([0]*N) for _ in range(N)]
    second_M = [list([0]*N) for _ in range(N)]
    third_M = [list([0]*N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            first_M[i][j] = M[-j-1][i]
    for i in range(N):
        for j in range(N):
            second_M[i][j] = first_M[-j-1][i]
    for i in range(N):
        for j in range(N):
            third_M[i][j] = second_M[-j-1][i]
    for i in range(N):
        for j in range(N):
            first_M[i][j] = str(first_M[i][j])
            second_M[i][j] = str(second_M[i][j])
            third_M[i][j] = str(third_M[i][j])
    print(f'#{tc}')
    for i in range(N):
        print(''.join(first_M[i]), end=' ')
        print(''.join(second_M[i]), end=' ')
        print(''.join(third_M[i]))