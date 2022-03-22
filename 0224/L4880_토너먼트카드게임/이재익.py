import sys
sys.stdin = open('input.txt')

def MakeGame(numbers): # 대진 표를 만드는 함수

    global daejin

    k = len(numbers)
    left = []
    right = []
    pivot = numbers[k // 2] # pivot을 기준으로 좌우로 나뉘게 되므로
    # basecase
    if len(numbers) == 1: # 대진표에 자기 혼자면 그대로 대진표 참여
        return daejin.append(numbers) and who_win.remove(numbers[0])
    if len(numbers) == 2: # 대진표에 둘이면 그 둘 그대로 대진표 참여
        return daejin.append(numbers) and who_win.remove(numbers[0]) and who_win.remove(numbers[1])
    # loop
    for i in numbers: # pivot을 기준으로 좌우에 정렬
        if i < pivot:
            left.append(i)
        if i >= pivot:
            right.append(i)

    MakeGame(left) # left와 right 둘 다 하나, 혹은 둘로 정렬될때까지 반복
    MakeGame(right)

def TCG(who_win): # 승자를 골라내는 함수

    while len(who_win) > 1: # 참가자가 1명 이상일때 계속 반복

        MakeGame(who_win) # MakeGame 함수를 통해 대진표를 생성

        for i in range(len(daejin)): # 가위바위보로 승자 결정

            if len(daejin[i]) > 1:
                    if M[daejin[i][0]-1] == 1: # 가위
                        if M[daejin[i][1]-1] == 1: # 가위
                            daejin[i].pop(1)
                        elif M[daejin[i][1]-1] == 2: # 바위
                            daejin[i].pop(0)
                        elif M[daejin[i][1]-1] == 3: #보
                            daejin[i].pop(1)
                    elif M[daejin[i][0]-1] == 2: # 바위
                        if M[daejin[i][1]-1] == 1: # 가위
                            daejin[i].pop(1)
                        elif M[daejin[i][1]-1] == 2: # 바위
                            daejin[i].pop(1)
                        elif M[daejin[i][1]-1] == 3: #보
                            daejin[i].pop(0)
                    elif M[daejin[i][0]-1] == 3: # 보
                        if M[daejin[i][1]-1] == 1: # 가위
                            daejin[i].pop(0)
                        elif M[daejin[i][1]-1] == 2: # 바위
                            daejin[i].pop(1)
                        elif M[daejin[i][1]-1] == 3: #보
                            daejin[i].pop(1)
            else:
                continue

        next_who_win = []

        for i in range(len(daejin)): # 이긴 사람을 다시 다음 참가 명단에 추가함.
            next_who_win.append(daejin[i][0])
        del((who_win)[0:len(who_win)])  # 참가 명단 초기화.
        who_win = next_who_win # 다음 참가자를 참가 명단으로 변경.
        del((daejin)[0:len(daejin)]) # 대진표 초기화

    if len(who_win) == 1:  # 참가 명단에 한 사람만 남으면 승자.
        print(f'#{tc} {who_win[0]}')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    M = list(map(int, input().split()))
    who_win = [] # 참가 번호를 저장해두는 곳
    daejin = [] # 대진표를 저장하는 곳
    for i in range(1, len(M)+1):
        who_win.append(i)

    TCG(who_win)
