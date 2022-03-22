import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    K = list(map(int, input().split()))
    cheese = []
    for i in range(M):
        cheese.append([i+1, K[i]])
    # 이 부분이 잘 이해가 안감
    oven = cheese[:N] # 인덱싱을 하면, 최초 오븐은 N번째까지 추가하게 됨
    remain = cheese[N:] # 남은 피자 목록
    while len(oven) >1: # 아직 오븐에 2개 이상 남아있을 때
        check = oven.pop(0) # 맨 앞에 것을 꺼내서 확인함
        check[1]//= 2 # 치즈 양을 바로 2로 나눠주고,
        if check[1] == 0: # 만약 2로 나눴을 때 0이 되면 꺼냄
            if remain: # 아직 남은 피자가 있다면
                oven.append(remain.pop(0)) # 오븐에 남은 첫번째 피자부터 더해줌
        else:
            oven.append(check) # 아직 치즈가 0이 안됐다면 오른쪽으로 다시 넣음

    print(f'#{tc} {oven[0][0]}') # 하나가 남았을 때 그것의 번호를 출력
