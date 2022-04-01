import sys
sys.stdin = open('input.txt')
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N에서 갈 수 있는 곳을 N과 함께 tmp에 저장함.
    tmp = []
    tmp.append(N)
    if 0<=N+1<=1000000:
        tmp.append(N+1)
    if 0<=N-1<=1000000:
        tmp.append(N-1)
    if 0<=2*N<=1000000:
        tmp.append(2*N)
    if 0<=N-10<=1000000:
        tmp.append(N-10)
    visit = [0]*1000001
    queue = deque()
    queue.append(tmp)
    visit[tmp[0]] = 1
    while queue:
        # n에는 0번 index에 지금 장소, 1,2,3,4번에 갈 수 있는 곳이 있음.
        n = queue.popleft()
        for i in range(1, len(n)):
            tmp2 = []
            # 갈 수 있는 곳이 비어있다면
            if visit[n[i]] == 0:
                # 갈 수 있는 곳에 +1을 놔주고, tmp2에 갈 수 있는 곳의 번호+갈수 있는 곳에서
                # 또 갈 수 있는 곳을 저장
                visit[n[i]] = visit[n[0]]+1
                tmp2.append(n[i])
                if 0 <= n[i] + 1 <= 1000000:
                    tmp2.append(n[i] + 1)
                if 0 <= n[i] - 1 <= 1000000:
                    tmp2.append(n[i] - 1)
                if 0 <= 2 * n[i] <= 1000000:
                    tmp2.append(2 * n[i])
                if 0 <= n[i] - 10 <= 1000000:
                    tmp2.append(n[i] - 10)
                queue.append(tmp2)
        if visit[M] != 0:
            break
    print(f'#{tc} {visit[M]-1}')