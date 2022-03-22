import sys
sys.stdin = open('input.txt')

def my_max(numbers):
    my_max = 0
    for number in numbers:
        if number > my_max:
            my_max = number
    return my_max

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 NxN 형태, M은 MxM 파리채 크기
    matrix = [list(map(int, input().split())) for _ in range(N)] # 매트릭스 형태로 받아옴

    first_sum_list = []

    for i in range(N):
        for j in range(N-M+1):
            sum_list_imsi = 0
            for k in range(M):
                sum_list_imsi += matrix[i][j+k] # 매트릭스 가로 중 N-M+1의 길이에 해당하는 값을 더한 것을 저장
            first_sum_list.append(sum_list_imsi)
    print(first_sum_list)

    new_matrix = [[0]*(N-M+1)]*N
    for i in range(N):
            # new_matrix에 가로 크기를 N-M+1 크기로 분할해서 리스트에 저장
            new_matrix[i] = first_sum_list[(N-M+1)*i:(N-M+1)*i+N-M+1]
    print(new_matrix)
    top_list = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_count = 0
            for k in range(M):
                sum_count += new_matrix[i+k][j] # new_matrix에 있는 값 중 첫번 째 값마다, N-M+1씩 더한 값을 저장
                # 최대값을 구하는 것이므로 순서는 상관없음)
                if k == M-1:
                    top_list.append(sum_count)
                    sum_count = 0
    print(top_list)

    print(f'#{tc} {my_max(top_list)}') # max값을 리턴.