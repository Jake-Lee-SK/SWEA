import sys
sys.stdin = open('input.txt')
def DFS(S, G, cnt):
    global max
    global can_go
    if S == G:
        if max > cnt:
            max = cnt
        return
    if S!=G and cnt >= max:
        return
    visit = []
    for i in can_go[S]:
        if i not in visit:
            visit.append(i)
            DFS(i, G, cnt+1)
    return

for tc in range(1, int(input())+1):
    stops = list(map(int,input().split()))
    # 정류장의 수
    N = stops[0]
    # 최초 지급 후 선택을 하는 경우의 수를 정리.
    can_go = [[] for _ in range(len(stops)+1)]
    max = 1000000000000000000000000000000
    for i in range(1, len(stops)):
        if stops[i] == 1:
            can_go[i].append(i+1)
        elif stops[i] > 1:
            for j in range(1, stops[i]+1):
                if i+j<=N:
                    can_go[i].append(i+j)
    DFS(1, N, -1)
    print(f'#{tc} {max}')

