import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    M = [list(map(int, input().split())) for _ in range(9)]
    cnt_answer = 0
    for i in range(9): # 가로 검증
        cnt = 9
        for j in range(1, 10):
            if j in M[i]:
                cnt -= 1
        if cnt > 0:
            cnt_answer += 1


    for i in range(9): # 세로 검증
        cnt = []
        for j in range(9):
            if M[j][i] in cnt:
                cnt_answer += 1
            cnt.append(M[j][i])

    for t in range(3):
        for i in range(3): # 3x3 매트릭스 검증
            cnt = []
            for j in range(3):
                for k in range(3):
                    if M[j + (3 * t)][k + (3 * i)] in cnt:
                        cnt_answer += 1
                    cnt.append(M[j+(3*t)][k+(3*i)])
    if cnt_answer == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')