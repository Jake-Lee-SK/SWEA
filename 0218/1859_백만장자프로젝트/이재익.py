import sys
sys.stdin = open('input.txt')

# 생각지도 못한 방법으로 푸는 사람들의 정답이 눈에 띔

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 연속 N일 동안의 매매가
    price = list(map(int, input().split()))
    bank = 0 # 현재 갖고 있는 갯수
    profit = 0 # 이익
    jichul = 0 # 현재까지 지출한 금액
    day_highest = 0
    price_highest = 0
    for i in range(N):
        price_highest = max(price)

        if price[i] < price_highest:
            bank += 1 # 매물 쌓기
            jichul += price[i] # 지출 쌓기
            price[i] = 0

        if price[i] == price_highest:
            profit += ((bank * price[i]) - jichul) # 이익 내기
            bank = 0 # 매물 초기화
            jichul = 0 # 지출 초기화
            price_highest = 0
            day_highest = 0
            price[i] = 0



    print(f'#{tc} {profit}')
