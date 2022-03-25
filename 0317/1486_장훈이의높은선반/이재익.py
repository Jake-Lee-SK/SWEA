import sys
sys.stdin = open('input.txt')
from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    sellers = list(map(int, input().split()))
    mans = []
    for i in range(1, N+1):
        subset = list(combinations(sellers, i))
        for sets in subset:
            if sum(sets) >= B:
                mans.append(sum(sets))
    print(f'#{tc} {min(mans)-B}')