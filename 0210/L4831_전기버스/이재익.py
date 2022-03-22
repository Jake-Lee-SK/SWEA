import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))
    bus_stop = 0 # 현재 버스 정류장의 위치
    answer = 0 # 충전 횟수
    # 출발점과 첫번째 충전소와의 거리가 최대 이동 거리보다 크면 무효
    if charger[0] - 0 > K:
        print(f'#{tc} {answer}')
        continue
    # 충전소 사이의 거리가 최대 이동 거리보다 크면 무효
    for i in range(1, len(charger)):
        if charger[i] - charger[i-1] > K:
            print(f'#{tc} {answer}')
            continue

    for i in range(50): # range 안의 수는 아무거나 큰 수를 제출
        bus_stop = bus_stop + K # 한번에 K만큼 이동
        # 마지막 정류장 이상 이동하면 멈추고 충전횟수 return
        if bus_stop >= N:
            print(f'#{tc} {answer}')
            break

        # 만약 최대 거리를 이동했을 때 충전소가 바로 나오면, 바로 충전
        if bus_stop in charger:
            for k in range(M):
                if bus_stop == charger[k]:
                    answer += 1
                else:
                    continue
        # 만약 최대 거리를 이동했는데 충전소가 나오지 않으면, 그 전 가장 가까운
        # 충전소에서 충전
        if bus_stop not in charger:
            for k in range(M-1):
                if charger[k] < bus_stop < charger[k+1]:
                    bus_stop = charger[k]
                    answer += 1
        # 위 if의 경우 마지막 충전소는 탐색할 수 없으므로, 마지막 충전소와
        # 최종 정류장 사이에 버스가 위치했을 경우 마지막 충전소에서 충전하는 조건
        if charger[-1] < bus_stop < N:
            bus_stop = charger[-1]
            answer += 1