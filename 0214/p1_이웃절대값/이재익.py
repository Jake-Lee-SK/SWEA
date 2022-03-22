import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    abs_number = 0
    for idx in range(0, 4): # idx는 dxs와 dys의 값들의 숫자와 그 한계를 같이함.
        for y in range(0, 5):
            for x in range(0, 5):
                new_x = x + dxs[idx]
                new_y = y + dys[idx]
                if 5 > new_x >= 0 and 5> new_y >= 0: # 한계를 5>new_x>=0으로 잡지 않고 단순히 new_x>=0으로 하면, new_x가 6이
                    # 되는 일이 생겨서, 5>를 따로 넣어주었음.
                    abs_number += abs(matrix[x][y] - matrix[new_x][new_y])
                else:
                    continue
    print(f'#{tc} {abs_number}')