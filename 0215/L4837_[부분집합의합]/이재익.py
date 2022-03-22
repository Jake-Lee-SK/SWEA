import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    N, M = map(int, input().split()) # N은 원소의 수, M은 원소의 합
    idx = 0
    for i in range(2**len(A)):
        subset = []
        for j in range(len(A)):
            if i & (1<<j):
                subset.append(A[j])
        if len(subset) == N and sum(subset) == M:
            idx += 1
    print(f'#{tc} {idx}')