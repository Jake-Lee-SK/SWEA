import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    two = input()
    three = input()

    # 10진수 형태로 일단 저장
    inttwo = 0
    intthree = 0

    for i in range(-1, -len(two)-1, -1):
        if two[i] == '1':
            inttwo += 2**(-i-1)

    for i in range(-1, -len(three)-1, -1):
        if three[i] == '1':
            intthree += 3**(-i-1)
        elif three[i] == '2':
            intthree += 3**(-i-1)*2

    # 답 저장할 곳
    ans = 0

    # 이진수, 삼진수를 각각 뒤에서부터 변경해보면서 bruteforce를 이용
    for i in range(-1, -len(two)-1, -1):

        check1 = 0
        # 자릿수가 1이면 0으로, 0이면 1로 변경한 10진수 숫자를 check1에 저장
        if two[i] == '1':
            check1 = inttwo - 2 ** (-i - 1)
        else:
            check1 = inttwo + 2 ** (-i - 1)

        # 3진수는 자릿수가 0이면 1 혹은 2, 1이면 2 혹은 0, 2이면 0 혹은 1로 경우의 수를 나눠서 모두 대입해봄.
        # check1(자릿수 바꿔본 이진수)과 check2(자릿수 바꿔본 삼진수)가 서로 맞으면 그것이 정답임.
        for j in range(-1, -len(three)-1, -1):
            check2 = 0

            if three[j] == '0':
                # 1
                check2 = intthree + 3**(-j-1)
                if check2 == check1:
                    ans = check1

                check2 = 0

                # 2
                check2 = intthree + 3**(-j-1)*2
                if check2 == check1:
                    ans = check1

            elif three[j] == '1':

                # 0
                check2 = intthree - 3**(-j-1)
                if check2 == check1:
                    ans = check1
                check2 = 0
                # 2
                check2 = intthree + 3**(-j-1)
                if check2 == check1:
                    ans = check1

            else:

                # 0
                check2 = intthree - 3**(-j-1)*2
                if check2 == check1:
                    ans = check1
                check2 = 0
                # 1
                check2 = intthree - 3**(-j-1)
                if check2 == check1:
                    ans = check1



    print(f'#{tc} {ans}')