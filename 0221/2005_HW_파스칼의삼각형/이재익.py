import sys
sys.stdin = open('input.txt')

def pascal(number):
    M = [[] for i in range(number)]
    if number == 1: # 1번째 pascal
        print(f'#{tc}')
        print(1)
    if number == 2: # 2번째 pascal
        print(f'#{tc}')
        print(1)
        print(1, 1)
    if number > 2: # 3번째부터의 pascal
        M[0].append(1) # 첫째줄
        M[1].append(1)
        M[1].append(1) # 둘째줄
        for i in range(2, number): # 셋째줄 부터는 둘째줄의 1,2번째와 2,1번째...를 더한 값을 중간값으로 가짐.
            M[i].append(1) # 첫번째 칸에는 무조건 1
            for j in range(i-1): # 중간 칸에는 위의 칸의 왼쪽부터 두개씩을 더함.
                M[i].append(M[i-1][j] + M[i-1][j+1])
            M[i].append(1) # 마지막 칸에는 무조건 1

        print(f'#{tc}')
        for i in range(number):
            for j in range(i+1):
                print(M[i][j], end = ' ')
            print()

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pascal(N)