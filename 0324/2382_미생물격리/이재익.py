import sys
sys.stdin = open('input.txt')

def move(array):
    # 움직이기

    for i in range(K):

        Y = array[i][0]
        X = array[i][1]
        C = array[i][2]
        D = array[i][3]

        #상향
        if D == 1:
            # 벽 바로 전일 때
            if Y == 1:
                array[i][0] += -1
                array[i][2] //= 2
                array[i][3] = 2
            else:
                array[i][0] += -1
        #하향
        elif D == 2:
            if Y == N-2:
                array[i][0] += 1
                array[i][2] //= 2
                array[i][3] = 1
            else:
                array[i][0] += 1
        #좌향
        elif D == 3:
            if X == 1:
                array[i][1] += -1
                array[i][2] //= 2
                array[i][3] = 4
            else:
                array[i][1] += -1
        #우향
        elif D == 4:
            if X == N-2:
                array[i][1] += 1
                array[i][2] //= 2
                array[i][3] = 3
            else:
                array[i][1] += 1

    # 합치기

    for i in range(K):
        if array[i][2] != 0:
            a, b, c, d = array[i][0], array[i][1], array[i][2], array[i][3]
            for j in range(i+1, K):
                if array[j][0] == a and array[j][1] == b:
                    array[i][2] += array[j][2]
                    array[j] = [0,0,0,0]

    # 재정렬
    matrix.sort(key=lambda x: x[2], reverse=True)

T = int(input())
for tc in range(1, T+1):
    # N = 정사각형 NxN, M = 격리시간, K = 미생물 군집 갯수
    N, M, K = map(int, input().split())
    matrix = [[0,0,0,0] for _ in range(K)]
    for i in range(K):
        Y, X, C, P  = map(int, input().split())
        matrix[i] = [Y,X,C,P]
    matrix.sort(key=lambda x: x[2], reverse=True)

    for i in range(M):
        move(matrix)
    cnt = 0
    for i in range(K):
        cnt += matrix[i][2]
    print(f'#{tc} {cnt}')