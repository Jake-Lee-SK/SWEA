import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())

for tc in range(1, T+1):
    N,M,K = map(int, input().split()) # N = 사람 숫자, M = 만드는 데 걸리는 시간, K = 만드는 갯수
    people = list(map(int, input().split())) # 아직 안 온 사람들
    people.sort()
    queue = deque(people)
    # 개시하기 전 오는 손님이 있는지 확인
    # 장사 개시
    bread = 0
    time = M
    while 1:
        while queue:
            stack = queue.popleft()
            if stack < time:
                bread -= 1
            else:
                queue.appendleft(stack)
                break
        if bread < 0:
            print(f'#{tc} Impossible')
            break
        elif bread >= 0:
            if len(queue) == 0:
                print(f'#{tc} Possible')
                break
        bread += K
        time += M