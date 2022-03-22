import sys
sys.stdin = open('input.txt')

def my_max(numbers): #max 함수 설정
    my_max = numbers[0]
    for number in numbers:
        if my_max < number:
            my_max = number

    return my_max

def my_sum(numbers):
    my_sum = 0
    for number in numbers:
        my_sum += number
    
    return my_sum

for tc in range(1, 11): # 10개 테스트 케이스가 주어짐. range(10)으로 해도 무방했을 것 같다.
    T = int(input()) # 테스트 케이스 번호 입력.
    matrix = [list(map(int, input().split())) for _ in range(100)] # 매트릭스는 100x100이므로 range(100)짜리
    col_list = [0] * 100 # 세로 값의 합을 저장할 빈 arr 생성
    max_row = 0 # 가로 값 중 가장 큰 값
    daegaksun_left = 0 # 왼쪽 위부터 시작하는 대각선의 합
    daegaksun_right = 0 #오른쪽 위부터 시작하는 대각선의 합
    max_value = [] # 네 값을 모두 모아놓을 리스트
    for i in range(100):
        if my_sum(matrix[i]) > max_row:
            max_row = my_sum(matrix[i]) # 가로 값의 합은 리스트 속의 리스트의 max 값과 동일함.
    for j in range(100):
        for k in range(100):
            col_list[j] += (matrix[k][j]) # 세로 값의 합은 각 리스트의 첫번째 값, 두번째 값...들의 합임.
    for l in range(100):
        daegaksun_left += matrix[l][l] # 왼쪽 위부터 시작하는 대각선 값의 합은 매트릭스의 0,0 1,1...의 합
    for m in range(100):
        daegaksun_right += matrix[99-m][m] #오른쪽 위부터 시작하는 대각선 값의 합은 99,0 98,1 ...의 합

    max_col = my_max(col_list) # col_list에 저장되어 있는 세로 값의 합 중 최대값을 저장
    max_value.append(max_col)
    max_value.append(max_row)
    max_value.append(daegaksun_left)
    max_value.append(daegaksun_right)
    print(f'#{T} {my_max(max_value)}') # max_value 안에 있는 값 중 최대값을 구해 계산.