import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    sum_list = []
    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            cnt += numbers[i+j]
        sum_list.append(cnt)
    print(f'#{tc} {max(sum_list)-min(sum_list)}')