import sys
sys.stdin = open('input.txt')

T = int(input()) # TC 숫자

for tc in range(1, T+1):

    N, K = map(int, input().split()) # NxN 배열 숫자 # K 단어 길이
    matrix = [list(map(int, input().split())) for _ in range(N)] # NxN 크기만큼 형성
    count_row = 0 # 가로에서 K단어 길이만큼 1을 갖고 있는 빈칸의 수
    count_col = 0 # 세로에서 K단어 길이만큼 1을 갖고 있는 빈칸의 수
    list_row = [] # 0, 0, 3 , 0 ....
    list_col = []
    # row에 들어갈 수 있는 갯수 세기
    for i in range(N):
        list_row_imsi = 0
        for j in range(N):
            if matrix[i][j] == 1: # 1인 숫자가 연속될 때 imsi 값이 하나씩 증가.
                list_row_imsi += 1
            if j == N-1: # 마지막에 도달하면 그때까지 저장한 값을 row에 추가.
                list_row.append(list_row_imsi)
                list_row_imsi = 0 # 초기화를 안시켜줬더니, 그 다음 줄에서도 연속으로 작동함. 초기화.
            if matrix[i][j] == 0: # 0을 만나면 그 때까지 저장된 값을 row에 추가하고, 초기화.
                list_row.append(list_row_imsi)
                list_row_imsi = 0

    for j in range(N): # 세로는 가로와 배열이 반대니까, 간단하게 생각함.
        list_col_imsi = 0
        for i in range(N):
            if matrix[i][j] == 1:  # 1인 숫자가 연속될 때 imsi 값이 하나씩 증가.
                list_col_imsi += 1
                if i == N - 1:  # 마지막에 도달하면 그때까지 저장한 값을 col에 추가.
                    list_col.append(list_col_imsi)
                    list_col_imsi = 0  # 초기화를 안시켜줬더니, 그 다음 값에서도 작동함. 초기화 했음.
            if matrix[i][j] == 0:  # 0을 만나면 그 때까지 저장된 값을 col에 추가하고, 초기화.
                list_col.append(list_col_imsi)
                list_col_imsi = 0

    for idx in range(len(list_row)):
        if list_row[idx] == K:
            count_row += 1
        else:
            continue
    for idx in range(len(list_col)):
        if list_col[idx] == K:
            count_col += 1
        else:
            continue
    print(f'#{tc} {count_row+count_col}')
