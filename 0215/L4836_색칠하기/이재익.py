import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    K = [list(map(int, input().split())) for _ in range(N)]
    matrix = [[0]*10  for _ in range(10)] # 매트릭스 만드는 법을 꼭 기억해두자.


    for i in range(N):
        if K[i][4] == 1: # 빨간색이면
            x1 = K[i][0]
            x2 = K[i][2]
            y1 = K[i][1]
            y2 = K[i][3]
            for j in range(y1, y2+1):
                for k in range(x1, x2+1):
                    matrix[j][k] = 1

    for i in range(N):
        if K[i][4] == 2: #파란색이면
            x1 = K[i][0]
            x2 = K[i][2]
            y1 = K[i][1]
            y2 = K[i][3]
            for j in range(y1, y2+1):
                for k in range(x1, x2+1):
                    matrix[j][k] += 2

    violet_cnt = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                violet_cnt += 1
    print(f'#{tc} {violet_cnt}')