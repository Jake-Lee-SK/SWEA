import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(Q)]
    box = [0]*N
    for i in range(Q):
        for j in range(LR[i][0]-1, LR[i][1]):
            box[j] = i+1

    print(f'#{tc}', end=' ')
    for i in range(N):
        print(box[i], end = ' ')
    print()