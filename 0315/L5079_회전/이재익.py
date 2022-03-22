import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    D = list(map(int, input().split()))
    E = deque(D)
    for i in range(M):
        E.append(E.popleft())
    print(f'#{tc} {E[0]}')