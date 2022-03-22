import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    M = [] # 숫자 저장용 통
    for i in range(N):
        M.append(numbers[i])

    for i in range(N): # 크기대로 소팅
        for j in range(N-i-1):
            if M[j] > M[j+1]:
                M[j], M[j+1] = M[j+1], M[j]
    if N % 2: # N이 홀수일 때
        for i in range(int(N/2)+1): # 큰 수 저장, 큰 수부터 나오니 마지막도 큰 수이다.
            numbers[2*i] = M[-i]
        for i in range(int(N/2)+1):
            numbers[(2*i)-1] = M[i]
    else:
        for i in range(int(N/2)):
            numbers[2*i] = M[-i-1]
        for i in range(int(N/2)+1):
            numbers[(2*i)-1] = M[i-1]

    print(f'#{tc}', end=' ')
    for i in range(10):
        print(numbers[i], end=' ')
    print()