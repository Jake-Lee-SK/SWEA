# greedy algo -> 실패(경우의 수를 전부 고려하기가 너무 힘들었음)
# DFS 접근

import sys
sys.stdin = open('input.txt')

def pool(month, money):
    global rates
    # 모든 달에서 각각 1일권, 1달권, 3달권 구매라는 선택권이 주어짐(물론 3달권 같은 경우는 선택권이 없음)
    # 각 경우의 수를 모두 탐색하는 함수를 생성(1년=12달밖에 안되서 경우의 수가 얼마 없음).
    if month>=12:
        if money < rates:
            rates = money
        return
    if date[month]:
        for i in range(3):
            if i == 0: # 첫번째라는 의미
                pool(month+1, money+(date[month]*rate[0]))
            elif i == 1:
                pool(month+1, money+rate[1])
            elif i == 2:
                pool(month+3, money+rate[2])
    else:
        pool(month+1, money)


T = int(input())
for tc in range(1, T+1):
    rate = list(map(int,input().split()))
    date = list(map(int,input().split()))
    rates = rate[3]
    pool(0, 0)
    print(f'#{tc} {rates}')

    # # 1달 이용권 or 1일 이용권
    # day_or_month = []
    # for i in range(12):
    #     # 일일이용권이 더 싸면 일일이용권으로 이용함
    #     if date[i]*rate[0] < rate[1]:
    #         day_or_month.append(date[i]*rate[0])
    #     # 한달이용권이 더 싸면 한달이용권으로 이용함
    #     else:
    #         day_or_month.append(rate[1])
    #
    #
    # # 1달or1일 이용권*3
    # date_check = []
    # date_three = []
    # for i in range(12):
    #     if date[i]>0:
    #         date_check.append(1)
    #     else:
    #         date_check.append(0)
    # for i in range(12):
    #     if i<=9:
    #         if date_check[i] > 0:
    #             a = (day_or_month[i])+(day_or_month[i+1])+(day_or_month[i+2])
    #             date_three.append(a)
    #         else:
    #             date_three.append(0)
    #     elif i==10:
    #         if date_check[i] > 0:
    #             date_three.append((day_or_month[i])+(day_or_month[i+1]))
    #         else:
    #             date_three.append(0)
    #     elif i==11:
    #         if date_check[i] > 0:
    #             date_three.append(day_or_month[i])
    #         else:
    #             date_three.append(0)
    #
    # # 3달 이용권
    # date_threeonly = []
    # for i in range(12):
    #     if i<=9:
    #         if date_check[i] > 0:
    #             date_threeonly.append(rate[2])
    #         else:
    #             date_threeonly.append(0)
    #     elif i==10:
    #         if date_check[i] > 0:
    #             date_threeonly.append(rate[2])
    #         else:
    #             date_threeonly.append(0)
    #     elif i==11:
    #         if date_check[i] > 0:
    #             date_threeonly.append(rate[2])
    #         else:
    #             date_threeonly.append(0)
    #
    # # 3달 이용권 reverse
    #
    # date_threeonlyreverse = []
    # for i in range(11, -1, -1):
    #     if i>=2:
    #         if date_check[i] > 0:
    #             date_threeonlyreverse.append(rate[2])
    #         else:
    #             date_threeonlyreverse.append(0)
    #     elif i==1:
    #         if date_check[i] > 0:
    #             date_threeonlyreverse.append(rate[2])
    #         else:
    #             date_threeonlyreverse.append(0)
    #     elif i==0:
    #         if date_check[i] > 0:
    #             date_threeonlyreverse.append(rate[2])
    #         else:
    #             date_threeonlyreverse.append(0)
    #
    #
    # # 1. 1년 이용권
    #
    # min_rate = rate[3]
    #
    #
    #
    # # 2. 1일 이용권 or 1달 이용권
    #
    # if sum(day_or_month) < min_rate:
    #     min_rate = sum(day_or_month)
    #
    # # 3. 3달 이용권만
    #
    # date_threeonlycheck = date_threeonly[:]
    # cnt = 0
    # for i in range(12):
    #     if i <= 9:
    #         if date_threeonlycheck[i]>0:
    #             cnt += date_threeonlycheck[i]
    #             date_threeonlycheck[i+1] = 0
    #             date_threeonlycheck[i+2] = 0
    #     if i == 10:
    #         if date_threeonlycheck[i] > 0:
    #             cnt += date_threeonlycheck[i]
    #             date_threeonlycheck[i+1] = 0
    #     if i == 11:
    #         if date_threeonlycheck[i] > 0:
    #             cnt += date_threeonlycheck[i]
    # if cnt < min_rate:
    #     min_rate = cnt
    #
    # # 4. 1일 이용권 / 1달 이용권 or 3달 이용권
    #
    # cnt = 0
    # date_threeonlycheck = date_threeonly[:]
    # date_threecheck = date_three[:]
    #
    # for i in range(12):
    #     if i <= 9:
    #         if date_threeonlycheck[i] < date_threecheck[i]:
    #             cnt += date_threeonlycheck[i]
    #             date_threeonlycheck[i+1] = 0
    #             date_threeonlycheck[i+2] = 0
    #             date_threecheck[i+1] = 0
    #             date_threecheck[i+2] = 0
    #         elif date_threeonlycheck[i] > date_threecheck[i]:
    #             cnt += date_threecheck[i]
    #             date_threeonlycheck[i+1] = 0
    #             date_threeonlycheck[i+2] = 0
    #             date_threecheck[i+1] = 0
    #             date_threecheck[i+2] = 0
    #         elif date_threeonlycheck[i] == date_threecheck[i] != 0:
    #             cnt += date_threecheck[i]
    #             date_threeonlycheck[i+1] = 0
    #             date_threeonlycheck[i+2] = 0
    #             date_threecheck[i+1] = 0
    #             date_threecheck[i+2] = 0
    #     if i == 10:
    #         if date_threeonlycheck[i] < date_threecheck[i]:
    #             cnt += date_threeonlycheck[i]
    #             date_threeonlycheck[i+1] = 0
    #             date_threecheck[i+1] = 0
    #         elif date_threeonlycheck[i] > date_threecheck[i]:
    #             cnt += date_threecheck[i]
    #             date_threeonlycheck[i+1] = 0
    #             date_threecheck[i+1] = 0
    #         elif date_threeonlycheck[i] == date_threecheck[i] != 0:
    #             cnt += date_threecheck[i]
    #             date_threeonlycheck[i+1] = 0
    #             date_threecheck[i+1] = 0
    #     if i == 11:
    #         if date_threeonlycheck[i] < date_threecheck[i]:
    #             cnt += date_threeonlycheck[i]
    #         elif date_threeonlycheck[i] > date_threecheck[i]:
    #             cnt += date_threecheck[i]
    # if cnt < min_rate:
    #     min_rate = cnt
    #
    # print(f'#{tc} {min_rate}')
    #
