import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 5):
    N = int(input())+1
    matrix = list([0]*N for _ in range(N))
    x, y = 0, 0
    direction = 6 # 6은 우회전, 8은 위, 2는 아래, 4는 왼쪽
    for i in range(1, (N-1)**2+1): # 총 갯수만큼 진행
        if direction == 6: # 우측으로 갈 때
            if x == 0: # 첫번째 줄에서는
                if y == N-2: # 맨 오른쪽에 다다르면
                    matrix[x][y] = i
                    direction = 2 # 방향 아래로 전환
                    x += 1 # x 값을 하나 추가
                    continue
                else:
                    matrix[x][y] = i
                    y += 1
                    continue
            else: # 첫번째 줄이 아닐 때 오른쪽으로 가면
                if matrix[x][y+1] != 0: # 그 다음이 숫자라면
                    matrix[x][y] = i # 우선은 저장
                    direction = 2 # 방향을 아래로 변경
                    x += 1 # x값을 하나 추가
                    continue
                else:
                    matrix[x][y] = i
                    y += 1
                    continue

        if direction == 2: # 아래로 내려갈 때
            if y == N-2: # 맨 오른쪽 줄에서는
                if x == N-2: # x값이 맨 밑이라면
                    matrix[x][y] = i
                    direction = 4
                    y -= 1 # 왼쪽으로 이동
                    continue
                else:
                    matrix[x][y] = i
                    x += 1
                    continue
            else: # 그외에서는
                if matrix[x+1][y] != 0:
                    matrix[x][y] = i
                    direction = 4
                    y -= 1
                    continue
                else:
                    matrix[x][y] = i
                    x+= 1
                    continue

        if direction == 4: #좌향
            if x == N-2: #맨 아래쪽 줄에서는
                if y == 0:  # y값이 맨 왼쪽이라면
                    matrix[x][y] = i
                    direction = 8 #상향으로 변경
                    x -= 1  # 위쪽으로 이동
                    continue
                else: # 아직 맨 왼쪽 전이라면
                    matrix[x][y] = i
                    y -= 1
                    continue
            else:            
                if matrix[x][y-1] != 0: # 다른 숫자에 다다르면
                    matrix[x][y] = i
                    direction = 8
                    x -= 1
                    continue
                else:
                    matrix[x][y] = i
                    y -= 1
                    continue
        if direction == 8: # 상향
            if matrix[x-1][y] != 0:
                matrix[x][y] = i
                direction = 6
                y += 1
                continue
            else:
                matrix[x][y] = i
                x -= 1
                continue

    N_matrix = list([0]*(N-1) for _ in range(N-1))
    for i in range(N-1):
        for j in range(N-1):
            N_matrix[i][j] = matrix[i][j]
    print(f'#{tc}')
    for i in range(N-1):
        for j in range(N-1):
            print(N_matrix[i][j], end = ' ')
        print()