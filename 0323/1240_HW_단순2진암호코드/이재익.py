import sys
sys.stdin = open('input.txt')
T = int(input())
from collections import deque
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input())) for i in range(N)]
    number = deque()
    for i in range(N):
        if sum(matrix[i]) == 0:
            continue

        else:
            for j in range(M-1, 5, -1):
                # 0
                if matrix[i][j] == 1 and matrix[i][j-1] == 0 and matrix[i][j-2] == 1 and matrix[i][j-3] == 1 and matrix[i][j-4] == 0 and matrix[i][j-5] == 0 and matrix[i][j-6] == 0:
                    number.appendleft(0)
                    matrix[i][j] = 2
                    matrix[i][j - 1] = 2
                    matrix[i][j - 2] = 2
                    matrix[i][j - 3] = 2
                    matrix[i][j - 4] = 2
                    matrix[i][j - 5] = 2
                    matrix[i][j - 6] = 2
                # 1
                elif matrix[i][j] == 1 and matrix[i][j-1] == 0 and matrix[i][j-2] == 0 and matrix[i][j-3] == 1 and matrix[i][j-4] == 1 and matrix[i][j-5] == 0 and matrix[i][j-6] == 0:
                    number.appendleft(1)
                    matrix[i][j] = 2
                    matrix[i][j - 1] = 2
                    matrix[i][j - 2] = 2
                    matrix[i][j - 3] = 2
                    matrix[i][j - 4] = 2
                    matrix[i][j - 5] = 2
                    matrix[i][j - 6] = 2

                # 2
                elif matrix[i][j] == 1 and matrix[i][j-1] == 1 and matrix[i][j-2] == 0 and matrix[i][j-3] == 0 and matrix[i][j-4] == 1 and matrix[i][j-5] == 0 and matrix[i][j-6] == 0:
                    number.appendleft(2)
                    matrix[i][j] = 2
                    matrix[i][j - 1] = 2
                    matrix[i][j - 2] = 2
                    matrix[i][j - 3] = 2
                    matrix[i][j - 4] = 2
                    matrix[i][j - 5] = 2
                    matrix[i][j - 6] = 2
                # 3
                elif matrix[i][j] == 1 and matrix[i][j-1] == 0 and matrix[i][j-2] == 1 and matrix[i][j-3] == 1 and matrix[i][j-4] == 1 and matrix[i][j-5] == 1 and matrix[i][j-6] == 0:
                    number.appendleft(3)
                    matrix[i][j] = 2
                    matrix[i][j - 1] = 2
                    matrix[i][j - 2] = 2
                    matrix[i][j - 3] = 2
                    matrix[i][j - 4] = 2
                    matrix[i][j - 5] = 2
                    matrix[i][j - 6] = 2
                # 4
                elif matrix[i][j] == 1 and matrix[i][j-1] == 1 and matrix[i][j-2] == 0 and matrix[i][j-3] == 0 and matrix[i][j-4] == 0 and matrix[i][j-5] == 1 and matrix[i][j-6] == 0:
                    number.appendleft(4)
                    matrix[i][j] = 2
                    matrix[i][j - 1] = 2
                    matrix[i][j - 2] = 2
                    matrix[i][j - 3] = 2
                    matrix[i][j - 4] = 2
                    matrix[i][j - 5] = 2
                    matrix[i][j - 6] = 2
                # 5
                elif matrix[i][j] == 1 and matrix[i][j-1] == 0 and matrix[i][j-2] == 0 and matrix[i][j-3] == 0 and matrix[i][j-4] == 1 and matrix[i][j-5] == 1 and matrix[i][j-6] == 0:
                    number.appendleft(5)
                    matrix[i][j] = 2
                    matrix[i][j - 1] = 2
                    matrix[i][j - 2] = 2
                    matrix[i][j - 3] = 2
                    matrix[i][j - 4] = 2
                    matrix[i][j - 5] = 2
                    matrix[i][j - 6] = 2
                # 6
                elif matrix[i][j] == 1 and matrix[i][j-1] == 1 and matrix[i][j-2] == 1 and matrix[i][j-3] == 1 and matrix[i][j-4] == 0 and matrix[i][j-5] == 1 and matrix[i][j-6] == 0:
                    number.appendleft(6)
                    matrix[i][j] = 2
                    matrix[i][j - 1] = 2
                    matrix[i][j - 2] = 2
                    matrix[i][j - 3] = 2
                    matrix[i][j - 4] = 2
                    matrix[i][j - 5] = 2
                    matrix[i][j - 6] = 2
                # 7
                elif matrix[i][j] == 1 and matrix[i][j-1] == 1 and matrix[i][j-2] == 0 and matrix[i][j-3] == 1 and matrix[i][j-4] == 1 and matrix[i][j-5] == 1 and matrix[i][j-6] == 0:
                    number.appendleft(7)
                    matrix[i][j] = 2
                    matrix[i][j - 1] = 2
                    matrix[i][j - 2] = 2
                    matrix[i][j - 3] = 2
                    matrix[i][j - 4] = 2
                    matrix[i][j - 5] = 2
                    matrix[i][j - 6] = 2
                # 8
                elif matrix[i][j] == 1 and matrix[i][j-1] == 1 and matrix[i][j-2] == 1 and matrix[i][j-3] == 0 and matrix[i][j-4] == 1 and matrix[i][j-5] == 1 and matrix[i][j-6] == 0:
                    number.appendleft(8)
                    matrix[i][j] = 2
                    matrix[i][j - 1] = 2
                    matrix[i][j - 2] = 2
                    matrix[i][j - 3] = 2
                    matrix[i][j - 4] = 2
                    matrix[i][j - 5] = 2
                    matrix[i][j - 6] = 2
                # 9
                elif matrix[i][j] == 1 and matrix[i][j-1] == 1 and matrix[i][j-2] == 0 and matrix[i][j-3] == 1 and matrix[i][j-4] == 0 and matrix[i][j-5] == 0 and matrix[i][j-6] == 0:
                    number.appendleft(9)
                    matrix[i][j] = 2
                    matrix[i][j - 1] = 2
                    matrix[i][j - 2] = 2
                    matrix[i][j - 3] = 2
                    matrix[i][j - 4] = 2
                    matrix[i][j - 5] = 2
                    matrix[i][j - 6] = 2

        break
    cnt = 0
    for i in range(7):
        if i % 2: # 짝수일 때
            cnt += number[i]
        else:
            cnt += number[i]*3
    cnt += number[7]
    if cnt % 10:
        print(f'#{tc} 0')
    else:
        cnt = 0
        for i in range(8):
            cnt += number[i]
        print(f'#{tc} {cnt}')
