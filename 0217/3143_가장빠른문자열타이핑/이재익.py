import sys
sys.stdin = open('input.txt')

T = int(input())


# 메소드 이용

for tc in range(1, T+1):
    N, M = input().split()
    count_num = 0
    count_num = count_num + N.count(M)
    New_N = N.replace(M, '')
    count_num = count_num + len(New_N)
    print(f'#{tc} {count_num}')