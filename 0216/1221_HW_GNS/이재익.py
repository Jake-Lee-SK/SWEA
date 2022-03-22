import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())

for tc in range(1, T+1):
    testcase, number = input().split()
    case = list(input().split())
    # 값을 숫자로 바꿔주는 딕셔너리 num_invert 생성
    num_invert = {'ZRO' : 0 , 'ONE' : 1 , 'TWO' : 2 , 'THR' : 3 , 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}
    # 딕셔너리 값으로 case 속의 str들을 int로 대체
    for i in range(len(case)):
        case[i] = num_invert.get(case[i])
    # 버블 소팅을 이용해 int 형태 자료를 정렬
    for i in range(len(case)):
        for j in range(len(case)-i-1):
            if case[j] > case[j+1]:
                case[j], case[j+1] = case[j+1], case[j]
    # str 형태로 자료가 다시 나와야 하므로, int 형태를 다시 str로 바꿔주는 딕셔너리 생성
    num_invert2 = {'0': 'ZRO', '1' : 'ONE', '2' : 'TWO', '3': 'THR', '4': 'FOR', '5': 'FIV', '6': 'SIX', '7':'SVN', '8': 'EGT', '9': 'NIN'}
    # str 형태로 바뀐 case를 저장할 case2 리스트 생성, 이 list는 int 형태를 str 형태로 바꿔서 딕셔너리 값 탐색이 가능하게 함.
    case2 = list(map(str, case))
    # int 형태를 str로 바꿔줌
    for i in range(len(case)):
        case2[i] = num_invert2.get(case2[i])
    # print
    print(f'{testcase}')
    # case2를 그냥 print 하면 값이 하나씩 나오지 않으므로, for문을 한번 더 돌림.
    for i in range(len(case)):
        print(case2[i], end=' ')
    print()