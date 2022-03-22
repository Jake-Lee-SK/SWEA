import sys
sys.stdin = open('input.txt')

T = 10

for _ in range(1, 11):
    tc = int(input())
    matrix =  [input() for i in range(100)]
    pal_list = []
    for row in range(100):
        for first_char in range(100): #첫 글자부터
            for last_char in range(101): # 마지막 글자까지(단, 범위는 0~'100'까지 변동)
                # 왜 101까지 해야 하는 걸까...?
                word = matrix[row][first_char:last_char]
                pal_count = 0
                if len(word) == 1:
                    pal_list.append(1)
                else:
                    for check_pal in range(int(len(word)/2)):
                        if word[check_pal] == word[-check_pal-1]:
                            pal_count += 1
                        if pal_count == int(len(word)/2):
                            pal_list.append(len(word))

    print(f'#{tc} {max(pal_list)}')

    # 세로줄 리스트로 다시 가져오기
    col_list = []
    for col in range(100):
        col_list_row = []
        for row in range(100):
            col_list_row.append(matrix[row][col])
        join_row = ''.join(col_list_row)
        col_list.append(join_row)

    for row in range(100):
        for first_char in range(100):
            for last_char in range(101): # 마지막 글자
                word = col_list[row][first_char:last_char]
                pal_count = 0
                if len(word) == 1:
                    pal_list.append(1)
                else:
                    for check_pal in range(int(len(word)/2)):
                        if word[check_pal] == word[-check_pal-1]:
                            pal_count += 1
                        if pal_count == int(len(word)/2):
                            pal_list.append(len(word))

    print(f'#{tc} {max(pal_list)}')