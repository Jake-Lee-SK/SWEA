import sys
sys.stdin = open('input.txt')

# 가장 어려웠던 점은 역시 교수님 말씀대로

def service(K):
    global max_house # 손해 안보고 서비스 제공할 수 있는 최대 집
    global house_list # 집의 좌표
    price = K*K+(K-1)*(K-1) # 서비스 비용
    for i in range(N):
        for j in range(N):
            cnt = 0 # cnt 초기화
            for k in range(len(house_list)):
                if (abs(house_list[k][0]-i)+abs(house_list[k][1]-j)) <= K-1: # 특정 지점에서 K만큼 되는 범위의
                    # 서비스를 제공했을 때 서비스를 제공받을 수 있는 집이 있다면 cnt를 +1
                    cnt += 1
            # 총 제공받을 수 있는 집이 최대 집보다 많고, 가격도 손해를 보지 않는다면 답을 변경
            if cnt > max_house and cnt*M >= price:
                max_house = cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_house = 1
    house_list = []
    # 집의 좌표를 저장
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                house_list.append([i, j])
    # 1부터 여유롭게 N+3만큼 서비스 범위를 늘려가면서 search
    for i in range(1, N+3):
        service(i)
    # 최대 집의 갯수를 출력
    print(f'#{tc} {max_house}')