import sys
sys.stdin = open('input.txt')
from operator import itemgetter
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    times = [list(map(int,input().split())) for i in range(N)]
    # 끝나는 시간을 기준으로 정렬
    times.sort(key=itemgetter(1))
    dork = []
    dork.append(times[0])
    for i in range(1, len(times)):
        # 만약 맨 나중에 끝나는 시간보다 시작 시간이 빠르면, 넘어가고
        if times[i][0]<dork[-1][1]:
            continue
        # 그렇지 않다면 dork 사용 명단에 추가.
        else:
            dork.append(times[i])
    print(f'#{tc} {len(dork)}')