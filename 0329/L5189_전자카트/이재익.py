import sys
sys.stdin = open('input.txt')
from itertools import permutations

# 1321
# 1231

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    where_go = [] # 0(시작), 1!, 2!
    for i in range(1, N):
        where_go.append(i)
    go = list(permutations(where_go, N-1)) # permutation 작성
    max_cnt = 1000000000000000000000000
    # 1-2, 2-3, 3-1 / 1-3, 3-2, 2-1
    for i in range(len(go)):
        cnt = 0 # 가는 데 걸리는 시간을 저장
        cnt += matrix[0][go[i][0]] # 0-1
        for j in range(N-2):
            # 1-2
            cnt += matrix[go[i][j]][go[i][j+1]]
        cnt += matrix[go[i][-1]][0] # 2-0
        if max_cnt > cnt:
            max_cnt = cnt
    print(f'#{tc} {max_cnt}')
