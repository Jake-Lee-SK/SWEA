import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    for i in range(1, N+1):
        if i*i*i>N:
            print(f'#{tc} -1')
            break
        elif i*i*i == N:
            print(f'#{tc} {i}')
            break