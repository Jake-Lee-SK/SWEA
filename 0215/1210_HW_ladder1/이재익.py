import sys
sys.stdin = open('input.txt')

T=10

for _ in range(1, T+1):
    tc = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]
    answer = 0 # 답인 i번째 줄을 기억해 놓기 위함.
    for i in range(100):
        col = 0
        row = i + 0
        direction = 3  # 0 : 하강, 1 : 좌측 , 2 : 우측, 3 : 기본

        for x in range(1000):  # 루트 숫자(아무 큰 숫자나 생각해도 됨. 그냥 진행시키기 위함.)

            # 0일 경우 순서 넘김.
            if mat[col][row] == 0:
                break

            # 끝 줄에 다다랐을 때 숫자 계산
            if col == 99:
                if mat[col][row] == 2: # 답일 때, i번째(출발점)을 저장.
                    answer = i



                else: # 답이 아닐 때, 스킵
                    continue

            # 맨 왼쪽 줄의 경우

            if row == 0:

                # 오른쪽이 0인 경우 하강
                if mat[col][row] == 1 and mat[col][row + 1] == 0:
                    col += 1
                    direction = 0
                    continue

                # 오른쪽에 1이 있고, 하강하고있던 경우 우회전
                if mat[col][row] == 1 and direction == 0:
                    row += 1
                    direction = 2
                    continue

                # 오른쪽에 1이 있지만, 들어오고 있던 경우 하강
                if mat[col][row] == 1 and mat[col+1][row] == 1 and direction == 1:
                    col += 1
                    direction = 0
                    continue

            if 0 < row < 99:

                # 양쪽이 0인 경우 하강
                if mat[col][row] == 1 and mat[col][row+1] == 0 and mat[col][row-1] == 0:
                    col += 1
                    direction = 0
                    continue

                # 하강하고 있던 경우 우회전
                if mat[col][row] == 1 and mat[col][row+1] == 1 and direction == 0:
                    row += 1
                    direction = 2
                    continue

                # 오른쪽에 1이 있고 우측 진행하고 있는 경우 계속 우측 진행
                if mat[col][row+1] == 1 and direction == 2:
                    row += 1
                    direction = 2
                    continue
                # 우측 진행 중 하강 번호를 만날 경우
                if mat[col][row + 1] == 0 and direction == 2 and mat[col + 1][row] == 1:
                    col += 1
                    direction = 0
                    continue
                # 왼쪽에 1이 있고 하강하고 있던 경우 좌회전
                if mat[col][row - 1] == 1 and direction == 0:
                    row -= 1
                    direction = 1
                    continue
                # 왼쪽에 1이 있고 좌측 진행하고 있는 경우 계속 좌측 진행
                if mat[col][row - 1] == 1 and direction == 1:
                    row -= 1
                    direction = 1
                    continue
                # 좌측 진행 중 하강 번호를 만날 경우
                if mat[col][row - 1] == 0 and direction == 1 and mat[col - 1][row] == 1:
                    col += 1
                    direction = 0
                    continue
            # 맨 오른쪽 줄의 경우
            if row == 99:
                # 왼편이 0인 경우 하강
                if mat[col][row] == 1 and mat[col][row - 1] == 0:
                    col += 1
                    direction = 0
                    continue
                # 하강 중 좌회전하는 경우
                if mat[col][row - 1] == 1 and direction == 0:
                    row -= 1
                    direction = 1
                    continue
                # 오른쪽으로 들어오던 중 하강하는 경우
                if mat[col][row - 1] == 1 and direction == 2 and mat[col + 1][row] == 1:
                    col += 1
                    direction = 0
                    continue

    print(f'#{tc} {answer}')