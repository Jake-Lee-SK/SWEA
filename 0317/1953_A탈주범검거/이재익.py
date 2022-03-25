import sys
sys.stdin = open('input.txt')
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    pipes = [[] for _ in range(M*N)]
    for i in range(N):
        for j in range(M):
            a = M*i
            b = j
            if matrix[i][j] != 0:
                # + 파이프
                if matrix[i][j] == 1:

                    # 아래로 갈 때
                    if 0<=i+1<N:
                        if matrix[i+1][j] == 1 or matrix[i+1][j] == 2 or matrix[i+1][j] == 4 or matrix[i+1][j] == 7:
                            pipes[a+b].append(a+b+M)

                    # 위쪽으로 갈 때
                    if 0 <=i-1< N:
                        if matrix[i-1][j] == 1 or matrix[i-1][j] == 2 or matrix[i-1][j] == 5 or matrix[i-1][j] == 6:
                            pipes[a+b].append(a+b-M)

                    # 왼쪽으로 갈 때
                    if 0 <= j - 1 < M:
                        if matrix[i][j-1] == 1 or matrix[i][j-1] == 3 or matrix[i][j-1] == 4 or matrix[i][j-1] == 5:
                            pipes[a+b].append(a+b-1)

                    # 오른쪽으로 갈 때
                    if 0 <= j + 1 < M:
                        if matrix[i][j + 1] == 1 or matrix[i][j + 1] == 3 or matrix[i][j + 1] == 6 or matrix[i][j + 1] ==7:
                            pipes[a+b].append(a+b+1)

                # ㅣ 파이프
                elif matrix[i][j] == 2:
                    # 아래로 갈 때
                    if 0<=i+1<N:
                        if matrix[i+1][j] == 1 or matrix[i+1][j] == 2 or matrix[i+1][j] == 4 or matrix[i+1][j] == 7:
                            pipes[a+b].append(a+b+M)

                    # 위쪽으로 갈 때
                    if 0 <= i - 1 < N:
                        if matrix[i-1][j] == 1 or matrix[i-1][j] == 2 or matrix[i-1][j] == 5 or matrix[i-1][j] == 6:
                            pipes[a+b].append(a+b-M)
                # ㅡ 파이프
                elif matrix[i][j] == 3:
                    # 왼쪽으로 갈 때
                    if 0 <= j - 1 < M:
                        if matrix[i][j-1] == 1 or matrix[i][j-1] == 3 or matrix[i][j-1] == 4 or matrix[i][j-1] == 5:
                            pipes[a+b].append(a+b-1)

                    # 오른쪽으로 갈 때
                    if 0 <= j + 1 < M:
                        if matrix[i][j + 1] == 1 or matrix[i][j + 1] == 3 or matrix[i][j + 1] == 6 or matrix[i][j + 1] ==7:
                            pipes[a+b].append(a+b+1)

                # 위쪽, 오른쪽 파이프

                elif matrix[i][j] == 4:

                    # 위쪽으로 갈 때
                    if 0 <= i - 1 < N:
                        if matrix[i-1][j] == 1 or matrix[i-1][j] == 2 or matrix[i-1][j] == 5 or matrix[i-1][j] == 6:
                            pipes[a+b].append(a+b-M)
                    # 오른쪽으로 갈 때
                    if 0 <= j + 1 < M:
                        if matrix[i][j + 1] == 1 or matrix[i][j + 1] == 3 or matrix[i][j + 1] == 6 or matrix[i][j + 1] ==7:
                            pipes[a+b].append(a+b+1)

                # 오른쪽, 아래쪽 파이프

                elif matrix[i][j] == 5:
                    # 오른쪽으로 갈 때
                    if 0 <= j + 1 < M:
                        if matrix[i][j + 1] == 1 or matrix[i][j + 1] == 3 or matrix[i][j + 1] == 6 or matrix[i][j + 1] ==7:
                            pipes[a+b].append(a+b+1)
                    # 아래로 갈 때
                    if 0<=i+1<N:
                        if matrix[i+1][j] == 1 or matrix[i+1][j] == 2 or matrix[i+1][j] == 4 or matrix[i+1][j] == 7:
                            pipes[a+b].append(a+b+M)

                # 아래쪽, 왼쪽 파이프

                elif matrix[i][j] == 6:
                    # 아래로 갈 때
                    if 0<=i+1<N:
                        if matrix[i+1][j] == 1 or matrix[i+1][j] == 2 or matrix[i+1][j] == 4 or matrix[i+1][j] == 7:
                            pipes[a+b].append(a+b+M)

                    # 왼쪽으로 갈 때
                    if 0 <= j - 1 < M:
                        if matrix[i][j-1] == 1 or matrix[i][j-1] == 3 or matrix[i][j-1] == 4 or matrix[i][j-1] == 5:
                            pipes[a+b].append(a+b-1)

                # 왼쪽, 위쪽 파이프

                elif matrix[i][j] == 7:
                    # 왼쪽으로 갈 때
                    if 0 <= j - 1 < M:
                        if matrix[i][j-1] == 1 or matrix[i][j-1] == 3 or matrix[i][j-1] == 4 or matrix[i][j-1] == 5:
                            pipes[a+b].append(a+b-1)

                    # 위쪽으로 갈 때
                    if 0 <= i - 1 < N:
                        if matrix[i-1][j] == 1 or matrix[i-1][j] == 2 or matrix[i-1][j] == 5 or matrix[i-1][j] == 6:
                            pipes[a+b].append(a+b-M)
    # 파이프로 연결된 곳 리스트에 정렬하기

    queue = deque(pipes[M*R+C])
    check = [0]*M*N
    check[M*R+C] = 1
    for i in pipes[M*R+C]:
        check[i] += 2
    while queue:
        n = queue.popleft()
        for i in pipes[n]:
            if check[i] == 0:
                queue.append(i)
                check[i] = check[n]+1
    cnt = 0
    for i in range(M*N):
        if 0 < check[i] <= L:
            cnt += 1

    print(f'#{tc} {cnt}')