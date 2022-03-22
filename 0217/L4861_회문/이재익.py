import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # NxN 매트릭스, M은 회문의 길이
    matrix = [list(input().split()) for _ in range(N)] # 무작위 문장 리스트
    answer = []

    for row in range(N): # 가로 회문 찾기
        for col in range(N-M+1): # N-M+1만큼 앞에서 찾는 갯수 제한
            check_pel = 0
            check_list = []
            for i in range(M): #
                check_list.append(matrix[row][0][col+i])
            for k in range(int(N / 2)):
                if check_list[k] == check_list[-k-1]: # 회문 찾는 함수
                    check_pel += 1
                if check_pel == int(M / 2):
                    answer.append(check_list)
    for col in range(N):  # 세로 회문 찾기
        for row in range(N-M+1):
            check_pel = 0
            check_list = []
            for i in range(M):
                check_list.append(matrix[row+i][0][col])
            for k in range(int(N / 2)):
                if check_list[k] == check_list[-k - 1]:
                    check_pel += 1
                if check_pel == int(M / 2):
                    answer.append(check_list)
    answer2 = answer[0]
    print(f'#{tc}', end=' ')
    print(''.join(answer2))