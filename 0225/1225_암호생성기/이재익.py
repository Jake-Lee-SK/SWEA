import sys
sys.stdin = open('input.txt')
from collections import deque #double-end queue 기능 호출

for tc in range(1, 11):
    N = int(input())
    deq = deque(list(map(int, input().split())))

    # 한 사이클
    while deq[7] > 0:
        for i in range(1, 6):
            deq.append(deq.popleft()-i)
            if deq[7] <= 0:
                deq[7] = 0
                break

    print(f'#{tc}', end = ' ')
    for i in range(8):
        print(deq[i], end = ' ')
    print()
